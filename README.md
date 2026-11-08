# Entrelinhas — assistente de estudos

Aplicação de perguntas e respostas que usa o Gemini por meio da OpenRouter para explicar assuntos em português. Projeto final da trilha de DevOps e IA da pós-graduação PUC-PR.

[![Testes](https://github.com/fsoaz/ia-generativa-projeto-final/actions/workflows/ci.yml/badge.svg)](https://github.com/fsoaz/ia-generativa-projeto-final/actions/workflows/ci.yml)

**Aplicação publicada:** [Abrir o Entrelinhas](https://entrelinhas-web-awjs.onrender.com)

**API:** [Verificar saúde](https://entrelinhas-api-awjs.onrender.com/saude)

Consulte [DECISOES.md](DECISOES.md) para conhecer as escolhas técnicas e os aprendizados do projeto.

## Executar localmente

Requisitos: Python 3.12 ou superior e uma chave OpenRouter. Crie e ative um ambiente virtual, depois instale as dependências:

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
