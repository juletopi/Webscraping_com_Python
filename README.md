<!--
❗ ➤ References used in this Repository:
🔗 • https://github.com/piyushsuthar/github-readme-quotes
🔗 • https://github.com/kyechan99/capsule-render
🔗 • https://github.com/DenverCoder1/custom-icon-badges
🔗 • https://shields.io
🔗 • https://emoji.gg
🔗 • https://getemoji.com
-->

<!-- PRESENTATION -->

<div align="center">
  <img src="https://github.com/user-attachments/assets/e459ca7b-7f36-43aa-b2a4-d43a233ca14e" alt="PythonTraining-pic" width="530px" title="Repositório de 'Treinamento Python'">
</div>
<br>

<div align="center">
  <a href="#">
    <img width=70% align="center" src="https://capsule-render.vercel.app/api?type=rect&color=ffffff&height=4&section=header&%20render">
  </a>
</div>
<br>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Kanit&size=40&duration=1&pause=99999&color=ffffff&center=true&vCenter=true&repeat=false&width=1400&height=80&lines=Repositório+back-end+sobre+'webscraping'+usando+Python." alt="WebscrapingPythonSVG" title="Texto-subtítulo do repositório"/>
  </a>
</div>

<!-- SUMMARY -->

<h2 align="center">Sumário 🧾</h2>

<div align="center">
  <p align="center">
    <a href="#-apresentação">Apresentação</a> &#xa0; | &#xa0;
    <a href="#-configurando-o-ambiente-virtual">Configurando o Ambiente Virtual</a> &#xa0; | &#xa0;
    <a href="#-utilizando-a-biblioteca-requests">Utilizando a Biblioteca Requests</a>
  </p>
  <p align="center">
    <a href="#-implementando-o-webscraping">Implementando o Webscraping</a> &#xa0; | &#xa0;
    <a href="#️-tecnologias-utilizadas">Tecnologias Utilizadas</a> &#xa0; | &#xa0;
    <a href="#-contribuições">Contribuições</a> &#xa0; | &#xa0;
    <a href="#-autor">Autor</a>
  </p>
</div>
<br>

<!-- ABOUT THE PAGE -->

## 📖 Apresentação
Este projeto tem como objetivo demonstrar como o processo de **webscraping** utilizando a linguagem **Python**, abordando desde a configuração inicial até a extração de dados de páginas web utilizando bibliotecas populares como `requests` e `BeautifulSoup`. 

Fora idealizado durante uma das oficinas da **21ª Semana Nacional de Ciência e Tecnologia** realizada em dezembro de 2024 no **IFRO Campus Ji-Paraná**.

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

## 🔧 Configurando o Ambiente Virtual 
1. **Crie o ambiente virtual**:
   ```bash
   python -m venv venv
   ```  
2. **Ative o ambiente virtual**:  
   - **Windows**:  
     ```bash
     venv\Scripts\activate
     ```  
   - **Linux/Mac**:  
     ```bash
     source venv/bin/activate
     ```  
3. **Instale as dependências**:  
   ```bash
   pip install -r requirements.txt
   ```

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

## 📥 Utilizando a Biblioteca Requests 
A biblioteca `requests` permite enviar requisições HTTP de forma simples. É ideal para interagir com APIs ou capturar o HTML de páginas web.  

### Exemplo: Requisição GET

```python
import requests
import json

response = requests.get("https://httpbin.org/get")
print(f"Status Code: {response.status_code}")
print(f"Dados da resposta: {json.dumps(response.json(), indent=2)}")
```

### Exemplo: Requisição POST

```python
import requests
import json

data = {
    "name": "Julio",
    "age": 21,
    "city": "Ji-Parana",
    "state": "RO"
}

response = requests.post("https://httpbin.org/post", data=data)
print(f"\nStatus Code: {response.status_code} - {json.dumps(response.json(), indent=2)}")
```

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

## 🌐 Implementando o Webscraping

### Exemplo: Obter Clima e Coordenadas

```python
import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search.php"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
HEADERS = {"referer": "https://nominatim.openstreetmap.org/search.html"}

def get_coordinates(city_name):
    params = {"q": city_name.strip(), "polygon_geojson": 1, "format": "jsonv2"}
    response = requests.get(NOMINATIM_URL, params=params, headers=HEADERS)
    if response.status_code == 200:
        location = response.json()[0]
        return float(location["lat"]), float(location["lon"])
    else:
        print(f"Erro ao obter coordenadas: {response.status_code}")

def get_weather(lat, lon):
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(OPEN_METEO_URL, params=params)
    if response.status_code == 200:
        weather = response.json()["current_weather"]
        return weather["temperature"], weather["weathercode"]
    else:
        print(f"Erro ao obter clima: {response.status_code}")

city = input("\nDigite o nome da cidade: ")
lat, lon = get_coordinates(city)
if lat and lon:
    temp, weather_code = get_weather(lat, lon)
    print(f"\nClima em {city}:\nTemperatura: {temp}ºC\nCódigo do clima: {weather_code}")
```

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Requests**
- **BeautifulSoup (bs4)**

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

<!-- CONTRIBUTIONS -->

## 🤝 Contribuições

<p>Todas as contribuições ao projeto são bem vindas!<br>Se você deseja contribuir para este projeto, há várias maneiras de fazer isso. Você pode:</p>
<ul>
  <li>Reportar bugs ou problemas;</li>
  <li>Propor novos recursos ou melhorias;</li>
  <li>Corrigir problemas através de pull requests;</li>
  <li>Ajudar a melhorar a documentação;</li>
  <li>Compartilhar o projeto com outras pessoas.</li>
</ul>
<p>Para saber mais sobre como contribuir, consulte o guia de contribuição <a href="https://github.com/juletopi/Webscraping_com_Python/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a>.</p>

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>
<br>

<!-- AUTHOR -->

## 👤 Autor

<table>
  <tr>
    <td valign="top" width="33%">
      <div align="center">  
        <a href="https://github.com/juletopi">
          <img src="https://user-images.githubusercontent.com/76459155/220271784-9f930c36-c370-4518-9b56-604627c6e2b5.png" width="120px;" alt="JuletopiAvatar-pic" title="Autor: Juletopi" />
          <br>
          <sub><b>Júlio Cézar | Juletopi</b></sub>
        </a>
      </div>
    </td>
    <td valign="left" width="100%">
      <div align="left">
        <ul>
          <li>
            <sub><img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" height="15" alt="LinkedIn-icon"> LinkedIn - <a href="https://www.linkedin.com/in/julio-cezar-pereira-camargo/">Júlio Cézar P. Camargo</a></sub>
          </li>
          <li>
            <sub><img align="center" src="https://pngimg.com/uploads/email/email_PNG100738.png" height="15" alt="Facebook-icon"> Email - <a href="mailto:juliocezarpvh@hotmail.com">juliocezarpvh@hotmail.com</a></sub>
          </li>
          <li>
            <sub><img align="center" src="https://cdn3.emoji.gg/emojis/6158-whatsapp.png" height="15" alt="WhatsApp-icon"> Whatsapp - <a href="http://api.whatsapp.com/send?phone=5569993606894">+55 (69) 9 9360-6894</a></sub>
          </li>
          <li>
            <sub><img align="center" src="https://cdn3.emoji.gg/emojis/6333-instagram.png" height="15" alt="Instagram-icon"> Instagram - <a href="https://www.instagram.com/juletopi/">@juletopi</a></sub>
          </li>
        </ul>
      </div>
    </td>
  </tr>
</table>

<div align="left">
  <h6><a href="#sumário-"> Voltar para o início ↺</a></h6>
</div>

<br>

<!-- THANK YOU, GOODBYE -->

----

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Sue+Ellen+Francisco&size=40&duration=1&pause=99999&color=dddddd&center=true&vCenter=true&repeat=false&width=620&height=60&lines=Obrigado+por+visitar%2C+e+até+a+próxima!" alt="TypingGoodbye-SVG" title="Boas venturas e volte sempre que precisar! ;)"/>
  </a>
</div>

<div align="center">
  Feito com 🤍 por <a href="https://github.com/juletopi"> Juletopi</a>.
</div>
