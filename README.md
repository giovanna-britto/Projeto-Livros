# **Gerenciador de Livros 📚**

Um projeto desenvolvido para gerenciar livros, utilizando uma API construída com **FastAPI** e uma interface gráfica em **Streamlit**.

## **Índice**
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Execução](#instalação-e-execução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso da API](#uso-da-api)
  - [Endpoints Disponíveis](#endpoints-disponíveis)
- [Uso do Front-end](#uso-do-front-end)


---

## **Funcionalidades**

- **Cadastro de Livros**: Adicionar novos livros ao sistema.
- **Consulta de Livros**: Listar livros cadastrados no banco de dados.
- **Atualização de Livros**: Editar informações de livros existentes.
- **Exclusão de Livros**: Remover livros do sistema.
- **Interface Gráfica**: Gerencie os livros por meio de um front-end simples usando Streamlit.

---

## **Tecnologias Utilizadas**

- **Backend**:
  - FastAPI
  - SQLAlchemy
  - SQLite (pode ser substituído por outros bancos, como PostgreSQL ou MySQL)
  - Alembic (gerenciamento de migrações)

- **Frontend**:
  - Streamlit

- **Outras Ferramentas**:
  - Python 3.10+
  - Poetry (gerenciamento de dependências)
  - Thunder Client ou Postman (para testar a API)

---

## **Pré-requisitos**

Certifique-se de ter instalado em sua máquina:
- Python 3.10 ou superior
- Git
- Poetry (instalado com `pip install poetry`)

---

## **Instalação e Execução**

### **1. Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/gerenciador-livros.git
cd gerenciador-livros
```

### **2. Instale as Dependências**
```bash
poetry install
```

### **3. Configure o Ambiente**
- Crie um arquivo `.env` na raiz do projeto com a seguinte configuração:
  ```env
  DATABASE_URL=sqlite:///./example.db
  ```

### **4. Execute as Migrações**
- Gere e aplique as migrações para criar as tabelas no banco de dados:
  ```bash
  poetry run alembic upgrade head
  ```

### **5. Inicie a API**
```bash
poetry run uvicorn gerenciador_livros.app:app --reload
```
- A API estará disponível em: `http://127.0.0.1:8000`

### **6. Inicie o Front-end**
Em outro terminal, execute:
```bash
poetry run streamlit run gerenciador_livros/front/app.py
```
- O front-end estará disponível em: `http://localhost:8501`

---

## **Estrutura do Projeto**

```
gerenciador_livros/
├── alembic.ini                 # Configuração do Alembic
├── example.db                  # Banco de dados SQLite (local)
├── gerenciador_livros/
│   ├── app.py                  # Arquivo principal da API FastAPI
│   ├── database.py             # Configuração do banco de dados
│   ├── models.py               # Modelos do banco de dados
│   ├── schemas.py              # Schemas Pydantic para validação
│   ├── settings.py             # Configurações do projeto
│   ├── migrations/             # Diretório de migrações (Alembic)
│   └── front/
│       └── app.py              # Interface gráfica com Streamlit
├── pyproject.toml              # Configuração do Poetry
├── README.md                   # Documentação do projeto
└── .env                        # Variáveis de ambiente
```

---

## **Uso da API**

### **Documentação Interativa**
Acesse `http://127.0.0.1:8000/docs` para visualizar e testar a API por meio do Swagger.

### **Endpoints Disponíveis**

| Método | Endpoint       | Descrição                      |
|--------|----------------|---------------------------------|
| GET    | `/books`       | Lista todos os livros          |
| POST   | `/books`       | Adiciona um novo livro         |
| PUT    | `/books/{id}`  | Atualiza um livro pelo ID      |
| DELETE | `/books/{id}`  | Remove um livro pelo ID        |

#### **Exemplo de Requisição (POST `/books`)**

**Request Body:**
```json
{
    "title": "O Senhor dos Anéis",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "isbn": "9780007117116",
    "category": "Fantasia",
    "price": 59.99,
    "assessment": 5
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "title": "O Senhor dos Anéis",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "isbn": "9780007117116",
    "category": "Fantasia",
    "price": 59.99,
    "assessment": 5
}
```

---

## **Uso do Front-end**

1. Acesse o Streamlit na URL: `http://localhost:8501`.
2. Use a interface para:
   - Adicionar livros: Preencha o formulário e clique em "Adicionar Livro".
   - Listar livros: Os livros cadastrados serão exibidos abaixo.
   - Atualizar livros: Selecione o ID de um livro para edição.
   - Excluir livros: Clique no botão "Excluir Livro" correspondente.
