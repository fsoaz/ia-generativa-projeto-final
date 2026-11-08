# Decisões técnicas e aprendizados

Este documento apresenta as escolhas do projeto Entrelinhas e os conceitos que podem ser explicados na apresentação. Os aprendizados devem ser revisados pelo estudante antes da entrega, para refletir sua própria experiência.

## Tema e organização

Escolhi um assistente de estudos porque perguntas e explicações formam um fluxo simples de demonstrar e permitem perceber o papel da IA generativa. Organizei o repositório em `frontend` e `backend` para distinguir a interface, executada no navegador, da API, executada no servidor. Essa separação facilita a manutenção e evita que a chave da OpenRouter seja enviada ao navegador.

## Tecnologias

Escolhi Python e FastAPI para implementar uma API pequena com validação de dados e documentação interativa. A rota `GET /saude` verifica se a aplicação está respondendo, enquanto `POST /perguntar` valida a pergunta, chama o serviço de IA e retorna uma resposta. O endpoint de saúde não garante que o Gemini esteja disponível. O frontend usa HTML, CSS e JavaScript: para uma tela com um formulário, uma biblioteca de interface não era necessária. O JavaScript envia a pergunta à API, apresenta o estado de carregamento e mostra a resposta ou um erro.

Escolhi o Gemini como modelo e a OpenRouter como intermediária para acessar diferentes provedores por uma única API. O modelo selecionado pode gerar custos; preços e disponibilidade devem ser verificados na plataforma. O nome do modelo é configurável, pois modelos podem mudar ou deixar de aceitar novas contas. A chave é armazenada em variável de ambiente no servidor; `.env.example` mostra as configurações necessárias sem conter uma chave real. A resposta é exibida como texto, e não como HTML executável.

## Testes, integração e publicação

Usei pytest e pytest-cov para verificar a API, incluindo perguntas inválidas e falhas do provedor. As chamadas à OpenRouter são simuladas, permitindo rodar testes sem rede, custo ou chave. A cobertura informa quais trechos foram executados, mas não garante que todos os erros foram encontrados. O GitHub Actions executa os testes e exige pelo menos 70% de cobertura; o badge no README mostra o resultado do workflow.

Escolhi o Render para publicar a API e o site estático. O arquivo `render.yaml` descreve a infraestrutura, e as variáveis de ambiente conectam os serviços. O plano gratuito pode adormecer após inatividade e está sujeito a limites. CORS permite configurar qual origem do navegador pode acessar a API, mas não substitui autenticação ou limitação de acesso.

## Aprendizados a apresentar

O projeto permitiu praticar a comunicação entre navegador, API e provedor de IA, além de diferenciar testes simulados de uma chamada real. A publicação mostrou a importância de configurar corretamente URLs, variáveis de ambiente e CORS e de acompanhar logs quando um deploy falha. Também demonstrou que provedores externos podem alterar modelos ou apresentar indisponibilidade temporária. Esses pontos reforçam a necessidade de mensagens de erro claras, testes e cuidado com segredos. O uso de IA como assistente de desenvolvimento exige revisão e compreensão das soluções pelo estudante.
