from dataclasses import dataclass
from datetime import date


@dataclass
class Livro:
    id: str
    titulo: str
    autor: str
    categoria: str
    quantidade: int
    quantidade_total: int


@dataclass
class Emprestimo:
    usuario_id: str
    livro_id: str
    vencimento: date
    devolvido: bool = False