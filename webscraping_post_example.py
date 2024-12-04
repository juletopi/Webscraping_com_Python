import requests
import json

# Webscraping referente ao site "https://httpbin.org/"

# Criar um dicionário com os dados a serem enviados na requisição POST
data = {
    "name": "Julio",
    "age": 21,
    "city": "Ji-Parana",
    "state": "RO"
}

# Enviando uma requisição POST para o servidor do HTTP Bin
# O método post() da biblioteca requests é usado para enviar uma requisição POST
# O parâmetro data é usado para passar os dados a serem enviados na requisição
response = requests.post("https://httpbin.org/post", data=data)

# Printando o status code da resposta e os dados da resposta em formato JSON
print(f"\r\nStatus Code: {response.status_code} - {json.dumps(response.json(), indent=2)}")