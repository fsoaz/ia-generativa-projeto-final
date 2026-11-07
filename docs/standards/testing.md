# Testes e CI

O pytest usa o cliente de testes do FastAPI e substitui a integração externa. Os casos cobrem saúde, validação, resposta, indisponibilidade e configuração. `pytest-cov` mede as linhas do módulo da API; o comando falha abaixo de 70%. A cobertura não garante correção completa e não mede a interface. O GitHub Actions executa o mesmo comando em cada push e pull request. Uma chamada real publicada deve ser verificada separadamente.
