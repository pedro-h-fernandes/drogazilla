# drogazilla

# **Documentação do Sistema de E-commerce**

## **1. Introdução**
### 1.1 Objetivo
Descrever as funcionalidades, arquitetura e requisitos do sistema de e-commerce, além de fornecer diretrizes para a implementação, manutenção e uso da plataforma.

### 1.2 Escopo
Este documento abrange todos os aspectos do sistema de e-commerce, incluindo funcionalidades de usuário, integrações, segurança e infraestrutura.

### 1.3 Público-alvo
Esta documentação é destinada a desenvolvedores, administradores de sistemas, testadores e gerentes de projeto.

---

## **2. Visão Geral do Sistema**
### 2.1 Descrição do Sistema
O sistema de e-commerce da farmácia Drogazilla permite que os usuários cadastrados naveguem por produtos variados encontrados em todas as farmacias do Brasil, façam compras online, efetuem pagamentos e acompanhem seus pedidos. O sistema oferece suporte a múltiplos métodos de pagamento e integrações com transportadoras.

### 2.2 Principais Funcionalidades
- **Gestão de Produtos**: Criação, atualização e exclusão de produtos, além de gerenciamento de categorias e inventário para usuários de funcionarios e adm.
- **Carrinho de Compras**: Adição e remoção de itens, cálculo de frete e descontos para usuarios comuns (clientes).
- **Sistema de Pagamentos**: Integração com gateways de pagamento para cartões de crédito, débito e outras formas.
- **Gerenciamento de Pedidos**: Visualização, cancelamento e histórico de pedidos.
- **Autenticação e Autorização**: Registro e login de usuários, com níveis de permissão.
- **Painel de Administrador**: Gestão de usuários, pedidos, produtos e configurações do site.

---

## **3. Requisitos**
### 3.1 Requisitos Funcionais
1. O sistema deve permitir o cadastro de novos usuários.
2. O sistema deve permitir que os usuários visualizem e adicionem produtos ao carrinho e finalizem a compra.
3. O sistema deve suportar múltiplos métodos de pagamento.
4. O sistema deve fornecer uma interface administrativa para a gestão de pedidos, produtos e usuários.

### 3.2 Requisitos Não Funcionais
1. **Desempenho**: O sistema deve ser capaz de suportar até 1.000 usuários simultâneos.
2. **Segurança**: O sistema deve implementar autenticação via bcrypt e armazenar senhas de forma criptografada.
3. **Disponibilidade**: O sistema deve estar disponível 99,9% do tempo.
4. **Escalabilidade**: O sistema deve ser facilmente escalável para atender a picos de tráfego.

---

## **4. Arquitetura do Sistema**
### 4.1 Diagrama de Arquitetura
![image](https://github.com/user-attachments/assets/330caedc-2e0d-41aa-b623-8c0259f5d0ad)


### 4.2 Componentes Principais
- **Front-end**: Desenvolvido com Flask e Bootstrap.
- **Back-end**: Implementado em Python com o framework Flask.
- **Banco de Dados**: MySQL para dados relacionais

---

## **5. Diagrama de Casos de Uso**

![image](https://github.com/user-attachments/assets/0af18c6f-91a1-4afc-b80c-3c402eb64e28)

---

## **6. Banco de Dados**
### 6.1 Modelo de Dados

![image](https://github.com/user-attachments/assets/a7641616-0a98-4810-9866-4d169865195b)


### 6.2 Estrutura de Tabelas/Coleções
#### **Tabela: Usuários**
- **Campos**: CPF, Nome, E-mail, Senha, Data de Nascimento, telefone
#### **Tabela: Produtos**
- **Campos**: codigo, Nome, Descrição, valor, quantidade, Categoria_id, fornecedor_cnpj
#### **Tabela: Pedidos**
- **Campos**: ID, ID do cliente, Data do Pedido, Código do produto

---

## **7. Integrações**
### 7.1 Gateways de Pagamento
Descrição das integrações com gateways de pagamento como Stripe, PayPal, e outros métodos.

### 7.2 APIs Externas
Integrações com APIs de serviços de entrega, plataformas de marketing e sistemas de recomendação de produtos.

---

## **8. Segurança**
### 8.1 Políticas de Segurança
- **Autenticação**: Implementação de autenticação via OAuth 2.0 e JWT.
- **Autorização**: Controle de permissões com base no nível de acesso do usuário.
- **Criptografia**: Senhas armazenadas com hashing e criptografia SSL em todas as transações sensíveis.

### 8.2 Vulnerabilidades Conhecidas e Soluções
Lista de vulnerabilidades comuns (SQL Injection, XSS, CSRF) e as medidas de prevenção adotadas.

---

## **9. Testes**
### 9.1 Testes Unitários
Descrição dos principais testes unitários implementados para validação das funcionalidades.

### 9.2 Testes de Integração
Testes para verificar a integração entre diferentes módulos, como o processamento de pagamentos e a atualização do inventário.

### 9.3 Testes de Segurança
Testes focados em vulnerabilidades como tentativas de SQL injection e ataques XSS.

---

## **10. Guia de Instalação**
### 10.1 Pré-requisitos
- Node.js (versão X.X.X)
- MongoDB
- Redis

### 10.2 Passo a Passo
1. Clone o repositório.
2. Instale as dependências com `npm install`.
3. Configure as variáveis de ambiente.
4. Execute o servidor com `npm start`.
5. Acesse o sistema em `http://localhost:3000`.

---

## **11. Manual do Usuário**
### 11.1 Visão Geral
Fornecer uma explicação passo a passo de como os usuários podem navegar no site, adicionar produtos ao carrinho, finalizar compras e acompanhar pedidos.

### 11.2 Tela de Administração
Explicar as funcionalidades disponíveis para administradores: adição de novos produtos, gerenciamento de pedidos e modificação de usuários.

---

## **12. Manutenção e Suporte**
### 12.1 Atualizações
Instruções sobre como aplicar atualizações de segurança e melhorias de performance.

### 12.2 Solução de Problemas
Lista de problemas comuns e suas soluções (ex: problemas de login, erros de pagamento, falhas de integração com APIs).

---

## **13. Anexos**
- **Diagrama ER**
- **Exemplos de Chamadas de API**
- **Políticas de Backup e Recuperação**
