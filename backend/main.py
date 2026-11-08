"""API do assistente de estudos."""
import logging
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
import httpx

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Assistente de Estudos")
origins = [origin.strip() for origin in os.getenv("FRONTEND_ORIGINS", "http://localhost:8000").split(",") if origin.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

class Pergunta(BaseModel):
    pergunta: str = Field(min_length=1, max_length=4000)

    @field_validator("pergunta")
    @classmethod
    def validar_pergunta(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Digite uma pergunta.")
        return value

class Resposta(BaseModel):
    resposta: str

def gerar_resposta(pergunta: str) -> str:
    chave = os.getenv("OPENROUTER_API_KEY")
    if not chave:
        raise RuntimeError("OPENROUTER_API_KEY não configurada")
    response = httpx.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {chave}"},
        json={
            "model": os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash"),
            "messages": [
                {"role": "system", "content": "Você é um assistente de estudos. Responda em português de forma clara e didática, usando exemplos quando úteis."},
                {"role": "user", "content": pergunta},
            ],
        },
        timeout=60.0,
    )
    response.raise_for_status()
    resposta = response.json()["choices"][0]["message"]["content"]
    if not isinstance(resposta, str) or not resposta.strip():
        raise RuntimeError("O provedor não retornou texto")
    return resposta

@app.get("/saude")
def saude():
    return {"status": "ok"}

@app.post("/perguntar", response_model=Resposta)
def perguntar(dados: Pergunta):
    try:
        return Resposta(resposta=gerar_resposta(dados.pergunta))
    except Exception:
        logging.exception("Falha ao gerar resposta")
        raise HTTPException(status_code=503, detail="Não foi possível gerar uma resposta. Tente novamente mais tarde.") from None
