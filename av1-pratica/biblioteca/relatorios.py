from biblioteca.servicos import BibliotecaService


class RelatorioBiblioteca:

    def __init__(self, biblioteca: BibliotecaService):
        self.biblioteca = biblioteca

    def gerar_relatorio(self):
        linhas = ["=== RELATORIO DA BIBLIOTECA ==="]

        for livro in self.biblioteca.livros.values():
            linhas.append(
                f"Livro: {livro.titulo} | "
                f"Disponivel: {livro.quantidade}/"
                f"{livro.quantidade_total}"
            )

        for usuario in self.biblioteca.usuarios.values():
            linhas.append(
                f"Usuario: {usuario.nome} | "
                f"Emprestimos: {usuario.emprestimos_ativos}"
            )

        return "\n".join(linhas)