# Refatoração de Sistema Legado — Biblioteca

Projeto desenvolvido para a atividade **AV1 — Refatoração de Sistema Legado**, com o objetivo de melhorar a qualidade, organização e manutenibilidade de um sistema de biblioteca existente, preservando seu comportamento válido.

## Objetivo

Refatorar um sistema legado aplicando boas práticas de programação e princípios de desenvolvimento de software, corrigindo problemas identificados no código original sem alterar as funcionalidades que já funcionavam corretamente.

## Funcionalidades

* Cadastro de livros;
* Cadastro de usuários;
* Diferentes tipos de usuários:

  * Usuário comum;
  * Usuário premium;
  * Funcionário;
  * Professor;
* Empréstimo de livros;
* Devolução de livros;
* Cálculo de multas por atraso;
* Reserva de livros indisponíveis;
* Relatório detalhado da biblioteca;
* Relatório resumido;
* Logging das operações;
* Testes automatizados.

## Principais melhorias

Durante a refatoração foram aplicadas as seguintes melhorias:

* Melhoria da nomenclatura de variáveis e atributos;
* Remoção de números mágicos;
* Redução de código duplicado;
* Divisão de responsabilidades;
* Uso de funções menores;
* Substituição de aninhamentos excessivos por guard clauses;
* Remoção de `except: pass`;
* Correção do erro ao tentar emprestar um livro para usuário inexistente;
* Substituição de `print` por logging;
* Remoção de CPF e email dos logs;
* Aplicação dos princípios DRY, KISS e YAGNI;
* Aplicação dos princípios SRP e OCP;
* Uso de herança e polimorfismo para os tipos de usuários.

## Estrutura do projeto

```text
av1-pratica/
├── biblioteca/
│   ├── __init__.py
│   ├── logging_config.py
│   ├── modelos.py
│   ├── relatorios.py
│   ├── servicos.py
│   └── usuarios.py
│
├── legado/
│   └── biblioteca-legado.py
│
├── testes/
│   ├── __init__.py
│   └── test_biblioteca.py
│
├── main.py
├── README.md
├── diagrama-classes.md
├── relatorio.md
└── refatoracao-sistema-legado.md
```

## Como executar

Clone o repositório e acesse a pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd av1-pratica
```

Execute o sistema:

```bash
python main.py
```

## Executando os testes

O projeto utiliza `pytest` para os testes automatizados.

Instale o pytest, caso necessário:

```bash
pip install pytest
```

Execute:

```bash
pytest
```

Os testes verificam funcionalidades como:

* Empréstimos;
* Limite de empréstimos;
* Devoluções;
* Cálculo de multas;
* Tipos de usuários;
* Reservas;
* Tratamento de usuário inexistente.

## Documentação

### Relatório de refatoração

O relatório apresenta os principais problemas encontrados no sistema legado e as soluções aplicadas:

[Relatório de Refatoração](relatorio.md)

### Diagrama de classes

O projeto possui um diagrama de classes utilizando Mermaid:

[Diagrama de Classes](diagrama-classes.md)

## Tecnologias

* Python
* Pytest
* Git
* GitHub
* Mermaid

## Status

Projeto concluído para a atividade de **Refatoração de Sistema Legado — AV1**.
