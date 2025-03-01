# Modelagem de Banco de Dados para Cassino Fictício com SQLAlchemy
Este projeto teve como objetivo a criação de um modelo de banco de dados relacional para um cassino fictício, utilizando a biblioteca SQLAlchemy em Python.

A biblioteca SQLAlchemy foi utilizada para mapear as entidades do modelo para classes Python, representando tabelas no banco de dados. As colunas das tabelas foram definidas como atributos das classes, com seus respectivos tipos de dados e restrições.

## Entidades e Atributos
O modelo de banco de dados é composto pelas seguintes entidades:

* **Pessoa:** id, nome, sobrenome, cpf, rg, email, data de nascimento, telefone, endereço, filial.
* **Funcionário:** id, função, placa.
* **Cliente:** id, tipo.
* **Endereço:** id, rua, bairro, cidade, estado, país.
* **Filial:** id, nome, cnpj, endereço.
* **Máquina:** id, nome, descrição, data de criação, ativada, algoritmo, filial.
* **Algoritmo:** id, descrição, url do código, data de criação.
* **Placa:** id, número, disponível, funcionário, jogo, filial.
* **Jogo:** id, nome, descrição, número máximo de jogadores, número mínimo de jogadores, aposta máxima, aposta mínima.
* **Pedido:** id, data de criação, status, serviço, produto, forma de pagamento, pessoa.
* **Forma de Pagamento:** id, nome, descrição, data de criação.
* **Pagamento:** id, valor, data, funcionário.
* **Produto:** id, nome, descrição, preço, data de criação, estoque.
* **Serviço:** id, nome, descrição, preço, data de criação.
* **Aposta:** id, valor, data de criação, vitória, jogo, máquina, pessoa.

## Relacionamentos
As entidades do modelo de banco de dados se relacionam da seguinte forma:

* Pessoa pode ter vários Endereços.
* Pessoa pode ser um Funcionário ou um Cliente.
* Funcionário pode estar associado a várias Placas.
* Cliente pode fazer várias Apostas.
* Máquina pode ter vários Algoritmos.
* Placa pode ter vários Jogos.
* Pedido pode ter vários Serviços e Produtos.
* Pedido pode ter uma Forma de Pagamento.
* Pagamento é feito por um Funcionário.
* Aposta pode ser feita em um Jogo ou em uma Máquina.

## Executando o Projeto
Para executar o projeto, siga os seguintes passos:

* Clone o repositório do GitHub.
* Crie um ambiente virtual Python.
* Instale as dependências do projeto com o comando `pip install -r requirements.txt.`
* Execute o arquivo `main.py` para criar o banco de dados e popular com dados de teste.
