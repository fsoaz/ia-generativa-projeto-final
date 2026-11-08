# Arquitetura e funcionamento

O navegador envia JSON para a API FastAPI. A API valida a pergunta, acrescenta uma orientação didática e envia o texto à OpenRouter, que encaminha a solicitação ao modelo Gemini, usando a chave guardada no servidor. A resposta volta como JSON e é apresentada como texto na página. O navegador nunca recebe a chave.

- `GET /saude`: retorna `{"status":"ok"}` quando a API responde; não testa a conectividade com o Gemini.
- `POST /perguntar`: recebe `{"pergunta":"O que é IA?"}` e devolve `{"resposta":"..."}`. Perguntas vazias ou maiores que 4000 caracteres geram 422. Falhas de configuração ou do provedor geram 503 com mensagem genérica.
- CORS permite apenas as origens configuradas em `FRONTEND_ORIGINS`, separadas por vírgulas. CORS não é autenticação: a API pública pode ser chamada por outros clientes.
- Não há armazenamento de perguntas na aplicação. O provedor pode processá-las conforme seus termos.

A função `gerar_resposta` isola a chamada HTTP externa. Os testes substituem esse ponto ou o cliente do SDK para evitar chamadas pagas e dependência da rede. O serviço não possui limitação de requisições: por isso, uma API pública pode consumir a cota da chave; acompanhe o uso e os custos na OpenRouter e considere adicionar proteção antes de uma divulgação ampla.
