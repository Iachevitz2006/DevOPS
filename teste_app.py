import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1: Verifica se a Home (/) responde 200 OK
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica se a mensagem de sucesso está na Home
def test_home_content(client):
    response = client.get('/')
    assert b"DOCKER FUNCIONANDO!" in response.data

# Teste 3: Verifica se a rota /status retorna o JSON correto
def test_status_route(client):
    response = client.get('/status')
    assert response.json['status'] == "online"

# Teste 4: Verifica se a rota /info contém a chave 'projeto'
def test_info_route(client):
    response = client.get('/info')
    assert "projeto" in response.json

# Teste 5: Verifica se o sistema retorna 404 para rotas inexistentes
def test_404_error(client):
    response = client.get('/qualquer-rota-errada')
    assert response.status_code == 404