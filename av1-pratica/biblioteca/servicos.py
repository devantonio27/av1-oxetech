from datetime import date, timedelta

from biblioteca.modelos import Emprestimo, Livro
from biblioteca.usuarios import Usuario


class BibliotecaService:

    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = []

    def adicionar_livro(
        self,
        livro_id: str,
        titulo: str,
        autor: str,
        categoria: str,
        quantidade: int
    ):
        livro = Livro(
            id=livro_id,
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            quantidade=quantidade,
            quantidade_total=quantidade
        )

        self.livros[livro_id] = livro

    def adicionar_usuario(self, usuario: Usuario):
        self.usuarios[usuario.id] = usuario