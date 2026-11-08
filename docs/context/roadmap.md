# Publicação no Render

1. Crie uma chave na OpenRouter e confira disponibilidade, preços e créditos do modelo escolhido. Não inclua a chave no Git.
2. Publique o repositório no GitHub como público. Confira o histórico e o conteúdo antes do push.
3. No Render, conecte o GitHub e crie um Web Service gratuito com raiz `backend`, build `pip install -r requirements.txt` e start `uvicorn main:app --host 0.0.0.0 --port $PORT`. Configure `OPENROUTER_API_KEY`, `OPENROUTER_MODEL` e `FRONTEND_ORIGINS` no painel; esta última deve conter a URL HTTPS exata do frontend, sem barra final.
4. Edite `frontend/config.js` com a URL HTTPS do backend, faça commit e push. Crie um Static Site no Render com diretório de publicação `frontend` e sem comando de build. Após obter sua URL, atualize `FRONTEND_ORIGINS` no backend.
5. Aguarde os deploys, teste `/saude` e envie uma pergunta pela URL pública. Atualize o README com as URLs e com o badge `https://github.com/USUARIO/REPOSITORIO/actions/workflows/ci.yml/badge.svg`, substituindo usuário e repositório. Confira se o workflow está verde.

Serviços gratuitos podem adormecer e demorar a responder. Cotas e elegibilidade variam; confira os painéis do Render e da OpenRouter antes do uso. A ativação de serviços e credenciais depende das contas do estudante.

## Alternativa com Blueprint

O arquivo `render.yaml` descreve os dois serviços e configura deploy após os testes passarem. Na criação, informe `OPENROUTER_API_KEY`, `FRONTEND_ORIGINS` e `API_URL` no painel do Render. Como as URLs públicas ainda não existem antes da criação, use temporariamente URLs HTTPS de exemplo para `FRONTEND_ORIGINS` e `API_URL`, depois substitua-as pelas URLs reais dos serviços e faça um novo deploy dos serviços afetados. A variável `API_URL` é pública e usada durante o build para gerar `frontend/config.js`; a chave Gemini pertence apenas ao backend.
