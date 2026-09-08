# Diagrama de Classes

```mermaid
classDiagram

    class BibliotecaService {
        -livros
        -usuarios
        -emprestimos
        -reservas
        +adicionar_livro()
        +adicionar_usuario()
        +emprestar()
        +devolver()
        +reservar()
        -_encontrar_emprestimo_ativo()
    }

    class RelatorioBiblioteca {
        -biblioteca
        +gerar_relatorio()
        +gerar_resumo()
    }

    class Livro {
        +id
        +titulo
        +autor
        +categoria
        +quantidade
        +quantidade_total
    }

    class Emprestimo {
        +usuario_id
        +livro_id
        +vencimento
        +devolvido
    }

    class Reserva {
        +usuario_id
        +livro_id
    }

    class Usuario {
        +id
        +nome
        +cpf
        +email
        +emprestimos_ativos
        +bloqueado
        +limite_emprestimos
        +prazo_emprestimo
        +multa_por_dia
    }

    class UsuarioComum {
        +limite_emprestimos
        +prazo_emprestimo
        +multa_por_dia
    }

    class UsuarioPremium {
        +limite_emprestimos
        +prazo_emprestimo
        +multa_por_dia
    }

    class Funcionario {
        +limite_emprestimos
        +prazo_emprestimo
        +multa_por_dia
    }

    class Professor {
        +limite_emprestimos
        +prazo_emprestimo
        +multa_por_dia
    }

    Usuario <|-- UsuarioComum
    Usuario <|-- UsuarioPremium
    Usuario <|-- Funcionario
    Usuario <|-- Professor

    BibliotecaService --> Livro
    BibliotecaService --> Usuario
    BibliotecaService --> Emprestimo
    BibliotecaService --> Reserva
    RelatorioBiblioteca --> BibliotecaService
    Emprestimo --> Usuario
    Emprestimo --> Livro
    Reserva --> Usuario
    Reserva --> Livro
```

## Descrição

O sistema utiliza **herança e polimorfismo** para representar os diferentes tipos de usuários. Cada tipo de usuário possui suas próprias regras de limite de empréstimos, prazo e multa, evitando condicionais espalhadas pela lógica principal.

A `BibliotecaService` concentra as operações do sistema, enquanto `RelatorioBiblioteca` é responsável exclusivamente pela geração dos relatórios.
