# Entrelinhas — assistente de estudos

Aplicação de perguntas e respostas que usa a API Gemini para explicar assuntos em português. Projeto final da trilha de DevOps e IA da pós-graduação PUC-PR.

> O badge de CI e as URLs públicas serão adicionados após a criação do repositório remoto e a publicação dos serviços.

## Executar localmente

Requisitos: Python 3.12 ou superior e uma chave Gemini. Crie e ative um ambiente virtual, depois instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements-dev.txt
cp .env.example .env
```

Edite `.env` com sua chave e carregue as variáveis no shell antes de iniciar a API:

```bash
set -a; source .env; set +a
cd backend
uvicorn main:app --reload --port 8001
```

Em outro terminal, a partir da raiz, execute `python3 -m http.server 8000 --directory frontend` e abra `http://localhost:8000`. A documentação interativa da API está em `http://localhost:8001/docs`.

## Testes

```bash
cd backend
pytest --cov=main --cov-report=term-missing --cov-fail-under=70
```

Os testes simulam o provedor e não precisam de chave nem fazem chamadas reais. Veja [arquitetura](docs/context/architecture.md), [publicação](docs/context/roadmap.md) e [testes](docs/standards/testing.md).
