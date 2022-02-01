"""
web scraping: entrar no site de dados e buscar o que precisar para usar
útil quando nao tem API

Exemplo no https://pt.stackoverflow.com/questions/tagged/python

para instalar os lib: pip install requests/ pip install beautifulsoup4
"""
import requests  # faz requisiçãp: baixar html e tudo
from bs4 import BeautifulSoup  # permite manipular o HTML

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)  # str do html
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')  # transforma a str em algo legivel

for pergunta in html.select('.question-summary'):  # coloca o seletor CSS
    titulo = pergunta.select_one('.question-hyperlink')  # so tem um titulo (class no html) entao select_one
    data = pergunta.select_one('.relativetime')  # com indicador HTML
    votos = pergunta.select_one('.vote-count-post')  # com indicador CSS
    print(data.text, titulo.text,votos.text, sep='\t')  # mostra só o texto da pergunta

