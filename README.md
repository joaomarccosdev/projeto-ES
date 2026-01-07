## 📝 Lista de Tarefas (Python)

Sistema simples de gerenciamento de tarefas desenvolvido em Python para prática de padrões de projeto.

## 📋 Funcionalidades

- Adicionar tarefas

- Listar tarefas cadastradas

- Remover tarefas pelo índice

- Alterar status da tarefa:

- Disponível

- Fazendo

- Feita

## 🛠️ Tecnologias

- Python 3

- Programação Orientada a Objetos

- Estruturas de controle

- Listas (armazenamento em memória)

## 🧠 Padrões de Projeto Utilizados

Padrões de projeto são soluções já conhecidas para problemas comuns no desenvolvimento de software.  
Neste projeto, eles foram utilizados para melhorar a organização do código e facilitar sua manutenção.

Foram aplicados os seguintes padrões:

---

### 🔹 Strategy

O padrão **Strategy** foi utilizado para representar os diferentes status de uma tarefa.

Cada status do sistema foi modelado como uma classe diferente, todas derivadas de uma classe base chamada `Status`.  
Os status disponíveis são: `Disponivel`, `Fazendo` e `Feita`.

Dessa forma, o status de uma tarefa não é representado por uma string ou número, mas sim por um objeto.  
Quando o usuário altera o status de uma tarefa, o sistema apenas troca o objeto de status associado a ela.

Esse padrão foi escolhido porque:
- Evita o uso excessivo de estruturas condicionais (`if/else`)
- Facilita a adição de novos status no futuro
- Torna o código mais organizado e legível

**Arquivo relacionado:**  
- `status/status.py`

---

### 🔹 Singleton

O padrão **Singleton** foi utilizado para garantir que exista apenas um gerenciador de tarefas em toda a aplicação.

A classe `GerenciadorTarefas` foi implementada de forma que apenas uma instância dela seja criada.  
Essa instância é responsável por armazenar e gerenciar todas as tarefas do sistema.

Sempre que o gerenciador é utilizado, o programa acessa essa mesma instância, garantindo que todas as partes do sistema trabalhem com a mesma lista de tarefas.

Esse padrão foi escolhido porque:
- Evita a criação de múltiplas listas de tarefas
- Mantém o estado do sistema consistente
- Centraliza o controle das tarefas

**Arquivo relacionado:**  
- `services/gerenciador.py`

## Separação por camadas:

- models → classe Tarefa

- status → classes de status

- services → gerenciador de tarefas

- main.py → interface via terminal

## ▶️ Como executar


```
bash
python main.py