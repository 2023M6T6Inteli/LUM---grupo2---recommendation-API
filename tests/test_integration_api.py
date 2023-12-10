import requests

# URL do servidor Flask
base_url = 'http://127.0.0.1:5000' 

# Endpoint para fazer previsões
predict_endpoint = '/predictSupplier'

# Dados de exemplo para enviar na requisição
data = {"CIE": "exemplo_cie"}

# Realizar uma requisição POST para o endpoint de previsão
response = requests.post(base_url + predict_endpoint, json=data)

# Verificar o código de status da resposta
status_code = response.status_code

# Exibir a resposta JSON do servidor
response_json = response.json()

# Exibir os resultados ou mensagens de erro
if status_code == 200:
    print("Resultado:")
    print(response_json)
else:
    print(f"Erro (código {status_code}):")
    print(response_json)
