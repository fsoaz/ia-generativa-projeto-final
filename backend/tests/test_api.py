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
    monkeypatch.delenv('GEMINI_API_KEY', raising=False)
    assert client.post('/perguntar', json={'pergunta': 'Teste'}).status_code == 503

def test_servico_gemini(monkeypatch):
    class Models:
        def generate_content(self, **kwargs):
            assert 'Fotossíntese' in kwargs['contents']
            return type('Result', (), {'text': 'Resposta simulada'})()
    class Client:
        def __init__(self, api_key):
            assert api_key == 'teste'
            self.models = Models()
    monkeypatch.setenv('GEMINI_API_KEY', 'teste')
    monkeypatch.setattr(main.genai, 'Client', Client)
    assert main.gerar_resposta('Fotossíntese') == 'Resposta simulada'
