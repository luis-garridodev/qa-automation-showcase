import requests

BASE_URL = "https://reqres.in/api"

def test_api_caminho_feliz():
    # Validando o Status 200 (OK)
    response = requests.get(f"{BASE_URL}/users/2")
    
    assert response.status_code == 200
    assert response.json()['data']['first_name'] == "Janet"
    print("Sucesso: API retornou os dados corretamente (Status 200).")

def test_api_rota_inexistente():
    # Validando resiliência e tratamento de erro (Status 404)
    # Procurando um usuário que não existe
    response = requests.get(f"{BASE_URL}/users/23")
    
    assert response.status_code == 404
    print("Sucesso: API tratou o erro corretamente e não caiu (Status 404).")

def test_api_payload_invalido():
    # Validando POST com erro na regra de negócio (Status 400)
    # Tentando registrar um usuário sem passar a senha
    payload_incompleto = {
        "email": "sydney@fife"
    }
    response = requests.post(f"{BASE_URL}/register", json=payload_incompleto)
    
    assert response.status_code == 400
    assert "Missing password" in response.json()['error']
    print("Sucesso: API barrou a inserção de dados incompletos (Status 400).")