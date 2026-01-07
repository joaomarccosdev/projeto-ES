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

## 📦 Conceitos e Padrões

Singleton -> 
Gerenciador possui somente uma instância para controlar todas as tarefas

Strategy -> 
Status é representado por classes diferentes e pode ser trocado em tempo de execução

## Separação por camadas:

- models → classe Tarefa

- status → classes de status

- services → gerenciador de tarefas

- main.py → interface via terminal

## ▶️ Como executar


```
bash
python main.py