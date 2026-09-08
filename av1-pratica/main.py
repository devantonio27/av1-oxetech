from datetime import date, timedelta

from biblioteca.servicos import BibliotecaService
from biblioteca.usuarios import (
    Funcionario,
    Professor,
    UsuarioComum,
    UsuarioPremium,
)
from biblioteca.relatorios import RelatorioBiblioteca


biblioteca = BibliotecaService()

# Livros
biblioteca.adicionar_livro(
    "L1", "Clean Code", "Robert Martin", "tecnico", 2
)

biblioteca.adicionar_livro(
    "L2", "O Hobbit", "Tolkien", "ficcao", 1
)

biblioteca.adicionar_livro(
    "L3", "SICP", "Abelson", "tecnico", 3
)

# Usuários
biblioteca.adicionar_usuario(
    UsuarioComum(
        "U1", "Ana", "11122233344", "ana@email.com"
    )
)

biblioteca.adicionar_usuario(
    UsuarioPremium(
        "U2", "Bruno", "55566677788", "bruno@email.com"
    )
)

biblioteca.adicionar_usuario(
    Funcionario(
        "U3", "Carla", "99988877766", "carla@email.com"
    )
)

biblioteca.adicionar_usuario(
    Professor(
        "U4", "Carlos", "12345678900", "carlos@email.com"
    )
)


print("========== CENARIO 1: emprestimos normais ==========")

print(biblioteca.emprestar("U1", "L1"))
print(biblioteca.emprestar("U2", "L2"))
print(biblioteca.emprestar("U3", "L3"))


print()
print("========== CENARIO 2: livro esgotado ==========")

print(biblioteca.emprestar("U1", "L2"))


print()
print("========== CENARIO 3: limite de emprestimos ==========")

biblioteca.adicionar_livro(
    "L4", "Livro Extra 1", "Autor", "geral", 5
)

biblioteca.adicionar_livro(
    "L5", "Livro Extra 2", "Autor", "geral", 5
)

biblioteca.adicionar_livro(
    "L6", "Livro Extra 3", "Autor", "geral", 5
)

print(biblioteca.emprestar("U1", "L4"))
print(biblioteca.emprestar("U1", "L5"))
print(biblioteca.emprestar("U1", "L6"))


print()
print("========== CENARIO 4: devolucao no prazo ==========")

print(biblioteca.devolver("U1", "L1"))


print()
print("========== CENARIO 5: devolucao com atraso ==========")

for emprestimo in biblioteca.emprestimos:
    if (
        emprestimo.usuario_id == "U1"
        and emprestimo.livro_id == "L4"
    ):
        emprestimo.vencimento = (
            date.today() - timedelta(days=5)
        )

print("Multa Ana:", biblioteca.devolver("U1", "L4"))


for emprestimo in biblioteca.emprestimos:
    if (
        emprestimo.usuario_id == "U2"
        and emprestimo.livro_id == "L2"
    ):
        emprestimo.vencimento = (
            date.today() - timedelta(days=10)
        )

print("Multa Bruno:", biblioteca.devolver("U2", "L2"))


for emprestimo in biblioteca.emprestimos:
    if (
        emprestimo.usuario_id == "U3"
        and emprestimo.livro_id == "L3"
    ):
        emprestimo.vencimento = (
            date.today() - timedelta(days=20)
        )

print("Multa Carla:", biblioteca.devolver("U3", "L3"))


print()
print("========== CENARIO 6: reserva ==========")

print(biblioteca.reservar("U4", "L2"))


print()
print("========== CENARIO 7: relatorio ==========")

relatorio = RelatorioBiblioteca(biblioteca)

print(relatorio.gerar_relatorio())

print()
print("========== RESUMO ==========")

print(relatorio.gerar_resumo())