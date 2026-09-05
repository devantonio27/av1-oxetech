from dataclasses import dataclass


@dataclass
class Usuario:
    id: str
    nome: str
    cpf: str
    email: str
    emprestimos_ativos: int = 0
    bloqueado: bool = False

    @property
    def limite_emprestimos(self):
        return 1

    @property
    def prazo_emprestimo(self):
        return 3

    @property
    def multa_por_dia(self):
        return 3


@dataclass
class UsuarioComum(Usuario):

    @property
    def limite_emprestimos(self):
        return 3

    @property
    def prazo_emprestimo(self):
        return 7

    @property
    def multa_por_dia(self):
        return 2