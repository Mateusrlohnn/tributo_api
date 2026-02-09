# 📊 Tributo API

API backend desenvolvida em FastAPI para simulação e comparação de regimes tributários (Simples Nacional, Lucro Presumido e Lucro Real).

O sistema permite cadastrar empresas, realizar simulações com base no faturamento informado e identificar automaticamente o regime tributário mais vantajoso.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Psycopg
- Docker
- Uvicorn

---

## 📂 Estrutura do Projeto

```bash
tributo_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── services.py
│
├── requirements.txt
└── README.md
```

### 📌 Descrição dos Arquivos

- **main.py** → definição das rotas e inicialização da aplicação  
- **database.py** → configuração do banco de dados e sessão SQLAlchemy  
- **models.py** → definição dos modelos ORM  
- **schemas.py** → validação e serialização de dados com Pydantic  
- **services.py** → regras de negócio (cálculo tributário)

---

## 🧠 Funcionalidades

✔ Cadastro de empresas  
✔ Listagem de empresas  
✔ Simulação tributária  
✔ Cálculo automático do melhor regime  
✔ Consulta agregada de total de impostos por empresa  

---

## 📌 Endpoints Principais

POST /empresas  
Cria uma nova empresa

GET /empresas  
Lista todas as empresas cadastradas

POST /simular  
Realiza simulação tributária com base no faturamento

GET /empresas/{empresa_id}/total-impostos  
Retorna a soma total de impostos simulados por regime

---

## ⚙️ Como Rodar o Projeto

1) Clone o repositório

git clone https://github.com/Mateusrlohnn/tributo_api.git
cd tributo_api

2) Crie e ative o ambiente virtual

Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate

3) Instale as dependências

pip install -r requirements.txt

4) Configure o banco de dados no arquivo database.py

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/tributo"

Certifique-se de que o banco "tributo" existe no PostgreSQL.

5) Execute a aplicação

uvicorn app.main:app --reload

Acesse a documentação automática em:

http://127.0.0.1:8000/docs

---

## 🏗️ Arquitetura

A aplicação segue uma arquitetura em camadas:

- Camada HTTP (FastAPI - rotas)
- Camada de Serviços (regras de negócio)
- Camada de Persistência (SQLAlchemy + PostgreSQL)

Essa organização facilita manutenção, escalabilidade e testes.

---

## 📊 Observações Técnicas

- Uso de ORM para abstração de banco de dados
- Separação clara de responsabilidades
- Validação de dados com Pydantic
- Consultas agregadas utilizando funções SQL (SUM)
- Estrutura preparada para expansão futura da API

---

## 👨‍💻 Autor

Mateus Rachadel Lohn


