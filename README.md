# 🚀 LabBooker

## 📌 Descrição do Problema
Ambientes acadêmicos sofrem com a falta de organização no uso de laboratórios. Professores e alunos muitas vezes enfrentam conflitos de horários, chegando a um laboratório e descobrindo que ele já está ocupado. O projeto inicial (Checkpoint 1) abordou isso de forma básica no terminal, sem salvamento real dos dados, o que limitava a usabilidade do sistema.

## 💡 Solução Proposta
O LabBooker é um sistema web responsivo e amigável que permite o cadastro de usuários, visualização de laboratórios disponíveis e o agendamento de reservas em horários específicos. Ele soluciona os conflitos checando automaticamente se o horário solicitado já está em uso, proporcionando um ambiente digital para garantir o recurso laboratorial para os alunos e professores.

## 🆕 Evoluções do Checkpoint 1 para o Checkpoint 2
- **Interface Gráfica Web**: Substituição da interface CLI (terminal) por uma interface web completa (HTML, CSS Glassmorphism).
- **Banco de Dados Real**: O armazenamento em memória (listas) foi substituído por um banco de dados relacional (SQLite), permitindo a persistência de dados.
- **Segurança e Autenticação**: Implementação de telas de cadastro e login com criptografia de senha (hash).
- **Arquitetura Modular**: O código foi separado em camadas (models, views, controllers/rotas, auth, database).

## 🛠️ Tecnologias Utilizadas
- **Python 3** (Linguagem Principal)
- **Flask** (Framework Web)
- **SQLite3** (Banco de Dados Relacional)
- **Werkzeug Security** (Criptografia de Senhas)
- **HTML5 e CSS3 Vanilla** (Design System com Glassmorphism)

## ⚙️ Como Executar

### Pré-requisitos
- Ter o [Python 3](https://www.python.org/downloads/) instalado na máquina.
- Ter o `pip` (gerenciador de pacotes do Python).

### Instalação
1. Clone o repositório ou faça o download dos arquivos.
2. Navegue até a pasta do projeto no terminal.
3. Instale as dependências executando:
```bash
pip install -r requirements.txt
```

### Execução
1. Inicialize o banco de dados (será criado um arquivo `lab_reserva.db`):
```bash
python src/data/database.py
```
2. Inicie o servidor Flask:
```bash
python -m src.main
```
3. Abra o seu navegador e acesse: `http://127.0.0.1:5000`

## 📁 Estrutura do Projeto
```
/
├── README.md               # Documentação principal
├── requirements.txt        # Dependências do projeto
├── docs/                   # Documentos extras e artefatos (Board Miro)
└── src/
    ├── main.py             # Arquivo principal (App Flask e Rotas)
    ├── auth/               # Módulos de cadastro e login
    │   ├── cadastro.py
    │   └── login.py
    ├── models/             # Classes de domínio e regra de negócio
    │   └── domain.py
    ├── views/              # Templates HTML do sistema
    │   ├── base.html
    │   ├── login.html
    │   ├── cadastro.html
    │   ├── dashboard.html
    │   └── reservas.html
    ├── static/             # Arquivos de estilo (CSS)
    │   └── style.css
    └── data/               # Configuração e arquivo do banco de dados
        ├── database.py
        └── lab_reserva.db
```

## ✅ Funcionalidades Implementadas

### Cadastro e Login
- O sistema possui tela de registro para novos usuários (nome, e-mail e senha).
- A senha não é salva em texto puro; ela sofre hash antes de ir pro banco de dados.
- O sistema possui tela de login, e o painel interno só é acessível após estar logado.

### Casos de Uso (com status)
1. **Efetuar Cadastro**: ✅ Implementado
2. **Fazer Login**: ✅ Implementado
3. **Cadastrar Laboratório**: ✅ Implementado
4. **Listar Laboratórios**: ✅ Implementado
5. **Fazer Reserva**: ✅ Implementado
6. **Visualizar Minhas Reservas**: ✅ Implementado
7. **Cancelar Reserva**: ✅ Implementado
8. **Fazer Logout**: ✅ Implementado

## ⭐ Diferencial do Projeto

### Descrição
O diferencial implementado consiste em três pilares principais combinados:
1. **Interface Web Moderna**: Uso de Flask renderizando templates HTML/CSS responsivos e com design "Glassmorphism".
2. **Segurança Avançada**: Uso do `werkzeug.security` para aplicar hash nas senhas dos usuários.
3. **Persistência de Dados**: Migração do projeto para utilizar banco de dados embutido **SQLite**.

### Justificativa
Um sistema puramente em terminal não simula a realidade do mercado atual para sistemas de reserva, que são majoritariamente plataformas web. Além disso, salvar dados em variáveis em memória faz com que o sistema perca seu propósito logo após fechar o console. A adoção de banco de dados e hash de senhas garante segurança real aos usuários e transforma o projeto acadêmico inicial em um Produto Mínimo Viável (MVP) sólido.

### Referências
- Documentação do Werkzeug Security: https://werkzeug.palletsprojects.com/en/3.0.x/utils/
- Documentação do SQLite3 Python: https://docs.python.org/3/library/sqlite3.html
- Documentação Flask: https://flask.palletsprojects.com/

## 🎬 Demonstração
> [!NOTE]
> Grave um vídeo de até 3 minutos ou crie GIFs demonstrando o Cadastro, Login e Criação de Reserva, e coloque o link aqui (substituindo esta nota).

## 👥 Integrantes do Grupo
- Eduardo Rodrigues (RM XXXX)
- (Adicione o nome dos outros membros)

## 🔗 Links (Miro, repositório, vídeo)
- **Repositório GitHub**: *(Insira a URL)*
- **Board do Miro**: *(Insira a URL)*
- **Vídeo de Demonstração**: *(Insira a URL)*
