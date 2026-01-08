## Lista de Tarefas (Python)

Este projeto consiste em um sistema simples de gerenciamento de tarefas, foi desenvolvido em Python, com o objetivo de praticar os conceitos e aplicação de padrões de projeto com  Programação Orientada a Objetos, conforme proposto na Atividade 3 da disciplina de Engenharia de Software.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- Adicionar tarefas contendo nome, descrição e status
- Listar todas as tarefas cadastradas
- Remover tarefas pelo índice
- Alterar o status de uma tarefa

Os status disponíveis para as tarefas são:
- Disponível
- Fazendo
- Feita

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Estruturas de controle
- Listas para armazenamento em memória

## Padrões de Projeto Utilizados

Os Padrões de projeto são soluções consolidadas para problemas recorrentes no desenvolvimento de software.  
Neste projeto, eles foram utilizados com o objetivo de melhorar a organização do código, facilitar a manutenção e tornar a solução mais flexível.

Foram aplicados os seguintes padrões de projeto:

### Strategy

O padrão Strategy foi utilizado para representar os diferentes status de uma tarefa.

Cada status do sistema foi modelado como uma classe distinta, todas derivadas de uma classe base chamada `Status`.  
Os status implementados são: `Disponivel`, `Fazendo` e `Feita`.

Dessa forma, o status de uma tarefa não é representado por uma string ou valor fixo, mas sim por um objeto.  
Quando o usuário altera o status de uma tarefa, o sistema apenas substitui o objeto de status associado a ela.

Esse padrão foi escolhido porque:
- Evita o uso excessivo de estruturas condicionais (`if/else`)
- Facilita a adição de novos status
- Torna o código mais organizado e extensível

Arquivo relacionado: 
 `status/status.py`

### Singleton

O padrão Singleton foi utilizado para garantir que exista apenas um gerenciador de tarefas em toda a aplicação.

A classe `GerenciadorTarefas` foi implementada de forma que apenas uma instância dessa classe seja criada durante a execução do programa.  
Essa instância é responsável por armazenar e gerenciar todas as tarefas do sistema.

Sempre que o gerenciador é utilizado, o programa acessa essa mesma instância, garantindo que todas as partes da aplicação trabalhem com a mesma lista de tarefas.

Esse padrão foi escolhido porque:
- Evita a criação de múltiplas listas de tarefas
- Mantém o estado da aplicação consistente
- Centraliza o controle das tarefas

**Arquivo relacionado:**  
- `services/gerenciador.py`

## Separação por Camadas

O projeto foi organizado em camadas para melhorar a estrutura e facilitar o entendimento do código:

- `models` → contém a classe `Tarefa`, responsável por representar a entidade do sistema
- `status` → contém as classes responsáveis pelos status das tarefas
- `services` → contém o gerenciador de tarefas
- `main.py` → responsável pela interface com o usuário via terminal

## Como Executar o Projeto

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de que o Python 3 está instalado
2. Execute o arquivo principal no terminal:

```bash
python main.py
