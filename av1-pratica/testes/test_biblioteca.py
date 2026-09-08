from datetime import date, timedelta

from biblioteca.servicos import BibliotecaService
from biblioteca.usuarios import (
Funcionario,
Professor,
UsuarioComum,
UsuarioPremium,
)

def criar_biblioteca():
    biblioteca = BibliotecaService()

    biblioteca.adicionar_livro(
        "L1", "Clean Code", "Robert Martin", "tecnico", 2
    )

    biblioteca.adicionar_livro(
        "L2", "O Hobbit", "Tolkien", "ficcao", 1
    )

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

    return biblioteca

def test_emprestimo_usuario_comum():
    biblioteca = criar_biblioteca()

    resultado = biblioteca.emprestar("U1", "L1")

    assert resultado is True
    assert biblioteca.livros["L1"].quantidade == 1
    assert biblioteca.usuarios["U1"].emprestimos_ativos == 1

def test_emprestimo_usuario_premium():
    biblioteca = criar_biblioteca()

    resultado = biblioteca.emprestar("U2", "L2")

    assert resultado is True
    assert biblioteca.livros["L2"].quantidade == 0

def test_emprestimo_funcionario():
    biblioteca = criar_biblioteca()

    resultado = biblioteca.emprestar("U3", "L1")

    assert resultado is True
    assert biblioteca.usuarios["U3"].emprestimos_ativos == 1

def test_limite_usuario_comum():
    biblioteca = criar_biblioteca()
    for numero in range(3):
        biblioteca.adicionar_livro(
            f"L{numero + 3}",
            f"Livro {numero + 3}",
            "Autor",
            "geral",
            1
    )

    assert biblioteca.emprestar("U1", "L1") is True
    assert biblioteca.emprestar("U1", "L3") is True
    assert biblioteca.emprestar("U1", "L4") is True

    assert biblioteca.emprestar("U1", "L5") is False

def test_devolucao_no_prazo():
    biblioteca = criar_biblioteca()
    biblioteca.emprestar("U1", "L1")

    resultado = biblioteca.devolver("U1", "L1")

    assert resultado == 0
    assert biblioteca.livros["L1"].quantidade == 2
    assert biblioteca.usuarios["U1"].emprestimos_ativos == 0

def test_devolucao_com_multa():
    biblioteca = criar_biblioteca()

    biblioteca.emprestar("U1", "L1")

    emprestimo = biblioteca.emprestimos[0]
    emprestimo.vencimento = date.today() - timedelta(days=5)

    resultado = biblioteca.devolver("U1", "L1")

    assert resultado == 10

def test_professor():
    biblioteca = criar_biblioteca()
    professor = biblioteca.usuarios["U4"]

    assert professor.limite_emprestimos == 15
    assert professor.prazo_emprestimo == 60
    assert professor.multa_por_dia == 0

def test_reserva_livro_indisponivel():
    biblioteca = criar_biblioteca()

    biblioteca.emprestar("U2", "L2")
    resultado = biblioteca.reservar("U4", "L2")

    assert resultado is True
    assert len(biblioteca.reservas) == 1

def test_reserva_livro_disponivel():
    biblioteca = criar_biblioteca()
    resultado = biblioteca.reservar("U4", "L1")
    assert resultado is False

def test_usuario_inexistente():
    biblioteca = criar_biblioteca()


    resultado = biblioteca.emprestar("U999", "L1")

    assert resultado is False

