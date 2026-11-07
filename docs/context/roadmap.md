# Publicação no Render

1. Crie uma chave no Google AI Studio e confirme que o modelo configurado tem cota gratuita na conta. Não inclua a chave no Git.
2. Publique o repositório no GitHub como público. Confira o histórico e o conteúdo antes do push.
3. No Render, conecte o GitHub e crie um Web Service gratuito com raiz `backend`, build `pip install -r requirements.txt` e start `uvicorn main:app --host 0.0.0.0 --port $PORT`. Configure `GEMINI_API_KEY`, `GEMINI_MODEL` e `FRONTEND_ORIGINS` no painel; esta última deve conter a URL HTTPS exata do frontend, sem barra final.
4. Edite `frontend/config.js` com a URL HTTPS do backend, faça commit e push. Crie um Static Site no Render com diretório de publicação `frontend` e sem comando de build. Após obter sua URL, atualize `FRONTEND_ORIGINS` no backend.
5. Aguarde os deploys, teste `/saude` e envie uma pergunta pela URL pública. Atualize o README com as URLs e com o badge `https://github.com/USUARIO/REPOSITORIO/actions/workflows/ci.yml/badge.svg`, substituindo usuário e repositório. Confira se o workflow está verde.

Serviços gratuitos podem adormecer e demorar a responder. Cotas e elegibilidade variam; confira os painéis do Render e do Google antes do uso. A ativação de serviços e credenciais depende das contas do estudante.
