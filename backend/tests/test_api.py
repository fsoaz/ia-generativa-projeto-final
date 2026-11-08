from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

def test_saude():
    assert client.get('/saude').json() == {'status': 'ok'}

def test_pergunta(monkeypatch):
    monkeypatch.setattr(main, 'gerar_resposta', lambda pergunta: f'Explicação: {pergunta}')
    response = client.post('/perguntar', json={'pergunta': '  O que é IA?  '})
    assert response.status_code == 200
    assert response.json() == {'resposta': 'Explicação: O que é IA?'}

def test_validacao():
    for pergunta in ['', '   ', 'a' * 4001]:
        assert client.post('/perguntar', json={'pergunta': pergunta}).status_code == 422
    assert client.post('/perguntar', json={}).status_code == 422

def test_falha_provedor(monkeypatch):
    def falhar(_):
        raise RuntimeError('segredo interno')
    monkeypatch.setattr(main, 'gerar_resposta', falhar)
    response = client.post('/perguntar', json={'pergunta': 'Teste'})
    assert response.status_code == 503
    assert 'segredo interno' not in response.text

def test_sem_chave(monkeypatch):
    monkeypatch.delenv('OPENROUTER_API_KEY', raising=False)
    assert client.post('/perguntar', json={'pergunta': 'Teste'}).status_code == 503

def test_servico_openrouter(monkeypatch):
    def post(url, headers, json, timeout):
        assert url == 'https://openrouter.ai/api/v1/chat/completions'
        assert headers['Authorization'] == 'Bearer teste'
        assert json['model'] == 'google/gemini-2.5-flash'
        assert json['messages'][1]['content'] == 'Fotossíntese'
        return main.httpx.Response(200, json={'choices': [{'message': {'content': 'Resposta simulada'}}]}, request=main.httpx.Request('POST', url))
    monkeypatch.setenv('OPENROUTER_API_KEY', 'teste')
    monkeypatch.delenv('OPENROUTER_MODEL', raising=False)
    monkeypatch.setattr(main.httpx, 'post', post)
    assert main.gerar_resposta('Fotossíntese') == 'Resposta simulada'

def test_resposta_vazia(monkeypatch):
    def post(url, **kwargs):
        return main.httpx.Response(200, json={'choices': [{'message': {'content': ''}}]}, request=main.httpx.Request('POST', url))
    monkeypatch.setenv('OPENROUTER_API_KEY', 'teste')
    monkeypatch.setattr(main.httpx, 'post', post)
    assert client.post('/perguntar', json={'pergunta': 'Teste'}).status_code == 503
