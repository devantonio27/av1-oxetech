# Relatório de Refatoração do Sistema Legado

## A. Qualidade e Code Smells

* **Nomes inadequados:** atributos e variáveis como `d`, `u` e `emp` dificultavam a compreensão do código.
* **Números mágicos:** valores de limite, prazo e multa estavam diretamente espalhados na lógica.
* **Código duplicado:** as regras de limite, prazo e multa eram verificadas repetidamente por meio de `if/elif`.

**Justificativa:** os nomes foram tornados mais claros e as regras específicas foram centralizadas nas classes de usuário, reduzindo duplicação e facilitando a manutenção.

## B. Nomenclatura e Funções Pequenas

* **Função gigante:** `emprestar()` concentrava validações, regras de negócio, alteração de estoque e criação do empréstimo.
* **Responsabilidades excessivas:** a lógica de busca de empréstimos foi extraída para `_encontrar_emprestimo_ativo()`.

**Justificativa:** a divisão das responsabilidades tornou as funções menores, mais legíveis e com objetivos claros.

## C. Aninhamento e Tratamento de Erros

* **Aninhamento excessivo:** vários `if` encadeados foram substituídos por guard clauses.
* **Erro engolido:** o `except: pass` foi removido para que erros não fossem silenciosamente ignorados.
* **Ordem incorreta de validação:** o código acessava dados do usuário antes de verificar sua existência.

**Bug corrigido:** ao tentar realizar um empréstimo para um usuário inexistente, o código acessava `self.u[id_u]["cpf"]` antes de verificar se o usuário existia, causando um `KeyError`. A validação da existência do usuário foi colocada antes do acesso aos seus dados, corrigindo o problema.

**Justificativa:** as guard clauses simplificaram o fluxo e garantiram que as validações fossem executadas na ordem correta.

## D. Logging e Princípios

* **Uso excessivo de `print`:** mensagens de operação e erro foram substituídas por logging.
* **Exposição de dados pessoais:** CPF e email, presentes nas mensagens do código legado, foram removidos dos logs.
* **DRY:** regras de limite, prazo e multa foram centralizadas nos tipos de usuário.
* **KISS:** foi mantida uma estrutura simples, evitando abstrações desnecessárias.
* **YAGNI:** foram implementadas somente as funcionalidades exigidas pela atividade.

**Justificativa:** o logging permite controlar melhor as mensagens do sistema e evita a exposição desnecessária de dados pessoais, enquanto DRY, KISS e YAGNI mantêm o código simples e sustentável.

## E. SOLID

* **SRP:** a classe `Sistema` realizava regras de negócio e também a formatação dos relatórios.
* **OCP:** a inclusão de novos tipos de usuário exigia alterações em vários `if/elif`.

**Justificativa:** a formatação dos relatórios foi separada em `RelatorioBiblioteca` e as regras dos usuários foram implementadas por polimorfismo, permitindo adicionar novos tipos sem alterar a lógica de empréstimo.

## Conclusão

A refatoração preservou o comportamento válido do sistema, incluindo empréstimos, devoluções e cálculo de multas. O único comportamento alterado foi a correção do bug de empréstimo para usuário inexistente. Também foram adicionados os tipos `Professor`, o relatório resumido e o sistema de reservas.

