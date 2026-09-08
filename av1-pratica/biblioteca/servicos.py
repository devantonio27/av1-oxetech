import logging

from datetime import date, timedelta

from biblioteca.modelos import Emprestimo, Livro, Reserva
from biblioteca.usuarios import Usuario

logger = logging.getLogger(__name__)

class BibliotecaService:

    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = []
        self.reservas = []

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

    def emprestar(self, usuario_id: str, livro_id: str):
        if usuario_id not in self.usuarios:
            logger.warning("Usuário não encontrado")
            return False

        if livro_id not in self.livros:
            logger.warning("Livro não encontrado")
            return False

        usuario = self.usuarios[usuario_id]
        livro = self.livros[livro_id]

        if usuario.bloqueado:
            logger.warning("Usuário bloqueado")
            return False

        if livro.quantidade <= 0:
            logger.warning("Livro indisponivel")
            return False

        if usuario.emprestimos_ativos >= usuario.limite_emprestimos:
            logger.warning("Usuário atingiu o limite de empréstimos")
            return False

        livro.quantidade -= 1
        usuario.emprestimos_ativos += 1

        vencimento = date.today() + timedelta(days=usuario.prazo_emprestimo)

        emprestimo = Emprestimo(
            usuario_id=usuario_id,
            livro_id=livro_id,
            vencimento=vencimento
        )

        self.emprestimos.append(emprestimo)
        logger.info("Empréstimo realizado com sucesso")

        return True

    def devolver(self, usuario_id: str, livro_id: str):
        emprestimo = self._encontrar_emprestimo_ativo(usuario_id, livro_id)

        if emprestimo is None:
            logger.warning("Empréstimo não encontrado")
            return -1

        livro = self.livros[livro_id]
        usuario = self.usuarios[usuario_id]

        emprestimo.devolvido = True
        livro.quantidade += 1
        usuario.emprestimos_ativos -= 1

        hoje = date.today()

        if hoje <= emprestimo.vencimento:
            logger.info("Livro devolvido sem multa")
            return 0

        dias_atraso = (hoje - emprestimo.vencimento).days
        multa = dias_atraso * usuario.multa_por_dia

        logger.info(f"Livro devolvido com {dias_atraso} dias de atraso. Multa: R$ {multa:.2f}")
        return multa

    def _encontrar_emprestimo_ativo(self, usuario_id: str, livro_id: str):
        for emprestimo in self.emprestimos:
            if (
                emprestimo.usuario_id == usuario_id
                and emprestimo.livro_id == livro_id
                and not emprestimo.devolvido
            ):
                return emprestimo

        return None

    def reservar(self, usuario_id: str, livro_id: str):
        if usuario_id not in self.usuarios:
            return False

        if livro_id not in self.livros:
            return False

        livro = self.livros[livro_id]

        if livro.quantidade > 0:
            return False

        reserva = Reserva(
            usuario_id=usuario_id,
            livro_id=livro_id
        )

        self.reservas.append(reserva)

        return True