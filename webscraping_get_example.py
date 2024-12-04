import requests
import json

# Webscraping referente ao site "https://httpbin.org/"

# Envia uma requisição GET para o servidor do HTTP Bin
# O servidor de teste do HTTP Bin é um serviço que retorna informações sobre a requisição que foi enviada
response = requests.get("https://httpbin.org/get")

# Printando o status code da resposta
# O status code é um número que indica o resultado da requisição
# Por exemplo, 200 OK indica que a requisição foi bem-sucedida
print(f"Status Code: {response.status_code}")

# Printando os dados da resposta em formato JSON
# O método json() da resposta retorna os dados da resposta em formato JSON
# O método dumps() da biblioteca json é usado para formatar os dados JSON de forma legível
print(f"Dados da resposta: {json.dumps(response.json(), indent=2)}")