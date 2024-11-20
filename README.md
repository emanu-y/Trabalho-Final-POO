# Trabalho-Final-POO
Sistema de Reserva de Hotel em Python utilizando os conceitos de Programação Orientada a Objetos.
1. Introdução ao Sistema

Objetivo: "Este sistema é um software de gerenciamento para hotéis, permitindo que administradores e clientes interajam com quartos, reservas e informações pessoais."
Usuários: Há dois tipos de usuários principais:
Administrador: Gerencia quartos, clientes e reservas.
Cliente: Faz reservas, visualiza e gerencia suas próprias informações.


2. Estrutura Geral do Sistema
Classes Principais:
Usuario: Classe base para todos os usuários, contendo atributos e métodos comuns (como nome, email, senha).
Cliente: Herda de Usuario e permite ações específicas, como fazer reservas e pesquisar quartos.
Administrador: Também herda de Usuario e possui permissões adicionais, como adicionar quartos e visualizar todas as reservas.
Quarto: Representa os quartos do hotel, armazenando informações como tipo, preço e disponibilidade.
Reserva: Garante o vínculo entre cliente e quarto, com informações sobre check-in e check-out.
Pagamento: Processa e cancela pagamentos, garantindo que reserva seja efetuada somente se houver pagamento.
Hotel: É a classe central que armazena listas de quartos, clientes e reservas.
Relatorio: Responsável por gerar relatórios consolidados.

3. Funcionamento de Cada Parte
a) Login e Diferenciação de Usuários
O método 'login' no arquivo 'main.py', inicializa o sistema, classificando os usuarios como clientes, adiministradores ou usuarios que irão se cadastrar como clientes, os direcionando para o método 'fazer_login' na classe usuários, que verifica se as credenciais são válidas e redireciona para o menu apropriado:
Se o tipo for administrador, exibe as opções de gerenciamento do hotel.
Se for cliente, exibe as opções de cliente.

b) Funcionalidades do Cliente
Fazer Reserva:
Pesquisa quartos disponíveis e cria uma instância da classe Reserva.
Adiciona a reserva ao histórico do cliente e à lista geral do hotel.
Visualizar Reservas:
Mostra todas as reservas do cliente.
Cancelar Reserva:
Permite cancelar uma reserva ativa, removendo-a do histórico e da lista do hotel.
Pesquisar Quarto por Tipo: 
Permite o usuário acessar os quartos baseado na sua classificação (soleiro, casal ou família).
Pesquisar Quartos: 
Mostra apenas os quartos disponíveis para o cliente.

c) Funcionalidades do Administrador
Gerenciar Quartos:
Adicionar, atualizar e remover quartos.
Gerenciar Clientes:
Cadastrar novos clientes, atualizar dados ou removê-los do sistema.
Gerenciar Reservas:
Mostra todas as reservas feitas no hotel, e permite o administrador cancelar reserva.
Gerar Relatório:
Usa a classe Relatorio para exibir um resumo de quartos, clientes e reservas.


d) Relacionamento entre Objetos
O sistema utiliza uma estrutura em que o Hotel atua como um ponto central, armazenando os dados globais (clientes, quartos, reservas). Tanto o administrador quanto o cliente interagem com o Hotel para acessar ou modificar informações.


4. Soluções Técnicas
Herança: As classes Cliente e Administrador herdam de Usuario para evitar duplicação de código.
Métodos Estáticos: Usados para funcionalidades que não dependem de uma instância, como o relatório.
Encapsulamento: Métodos get e set garantem que os dados sejam acessados de forma controlada.
Validação de Dados: Verificação de datas e tipos, como no método de fazer reservas.
