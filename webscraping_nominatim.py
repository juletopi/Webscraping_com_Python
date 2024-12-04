import requests

# Webscraping referente ao site "https://nominatim.openstreetmap.org/ui/search.html"

# URLs para as APIs do Nominatim e Open Meteo
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search.php"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
# Cabeçalho para a requisição da API do Nominatim (requerido para CORS)
HEADERS = {
    "referer": "https://nominatim.openstreetmap.org/search.html"
}

# Função para obter as coordenadas (latitude e longitude) de uma cidade
def get_coordinates(city_name):
    # Parâmetros da requisição da API do Nominatim
    params = {
        "q": city_name.strip(),  # <-- Nome da cidade a ser pesquisada
        "polygon_geojson": 1,  # <-- Retornar dados em formato GeoJSON
        "format": "jsonv2"  # <-- Retornar dados em formato JSON
    }

    # Enviando uma requisição GET para a API do Nominatim
    response = requests.get(NOMINATIM_URL, params=params, headers=HEADERS)

    # Verifica se a requisição foi bem-sucedida (200 OK)
    if response.status_code != 200:
        print(f"Erro ao obter as coordenadas para {city_name}: {response.status_code}")

    # Obtendo o primeiro resultado da resposta (deve ser as coordenadas da cidade)
    location = response.json()[0]

    # Retorna a latitude e longitude como floats
    return float(location["lat"]), float(location["lon"])

# Função para obter o clima atual para uma latitude e longitude
def get_weather(lat, lon):
    # Parâmetros da requisição da API do Open Meteo
    params = {
        "latitude": lat,  # <-- Latitude do local
        "longitude": lon,  # <-- Longitude do local
        "current_weather": True  # <-- Retornar dados do clima atual
    }

    # Enviando uma requisição GET para a API do Open Meteo
    response = requests.get(OPEN_METEO_URL, params=params)

    if response.status_code != 200:
        print(f"Erro ao obter o clima para {lat}, {lon}: {response.status_code}")

    # Obtendo os dados do clima atual da resposta
    weather = response.json()["current_weather"]

    # Retorna a temperatura e o código do clima
    return weather["temperature"], weather["weathercode"]

# Obtendo o nome da cidade do usuário
city = input("\r\nDigite o nome da cidade: ")
# Obtendo as coordenadas da cidade
lat, lon = get_coordinates(city)

# Verifica se as coordenadas foram obtidas com sucesso
if lat and lon:
    # Obtendo o clima atual da cidade
    temperature, weather_code = get_weather(lat, lon)
    # Verifica se os dados do clima foram obtidos com sucesso
    if temperature and weather_code:
        # Printando os dados
        print(f"\r\nClima em {city}:\r\nTemperatura: {temperature}ºC\nCódigo do clima: {weather_code}")
    else:
        print(f"\r\nErro ao obter o clima para {city}.")
else:
    print(f"\r\nErro ao obter as coordenadas para {city}.")