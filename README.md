# AtividadeMicrosservicos

Este projeto é uma aplicação acadêmica ou de teste que implementa uma arquitetura de microsserviços em Python. O sistema simula um fluxo de e-commerce simplificado, separando as responsabilidades de negócio em serviços independentes e utilizando um padrão de orquestração para a comunicação.

## Estrutura do Projeto

O projeto é composto pelos seguintes componentes principais:

* **`catalogo.py`**: Microsserviço responsável por gerenciar os produtos. Ele lida com a listagem, busca e detalhes dos itens disponíveis para compra.
* **`carrinho.py`**: Microsserviço dedicado ao gerenciamento do carrinho de compras. Responsável por adicionar, remover e listar os itens que o usuário deseja adquirir.
* **`orquestrador.py`**: Serviço central que atua como o *API Gateway* ou Orquestrador. Ele recebe as requisições externas e coordena as chamadas necessárias entre o `catalogo.py` e o `carrinho.py` para completar operações complexas.

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Comunicação:** HTTP/REST

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. 
```bash
# Instale as dependências
pip install -r requirements.txt
```
Para executar o sistema, abra terminais separados e inicie cada microsserviço individualmente:
```bash
python catalogo.py
python carrinho.py
python orquestrador.py
```