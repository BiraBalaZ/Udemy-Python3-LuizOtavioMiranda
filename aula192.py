# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import os
import requests
import re
from bs4 import BeautifulSoup
os.system('cls')

url = 'http://localhost:3333'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')
# print(top_jobs_heading.text)

if top_jobs_heading is not None:
    parent = top_jobs_heading.parent
    if parent is not None:
        for paragraph in parent.select('p'):
            print(re.sub(r'\s{1,}', ' ', paragraph.text.strip()),'\n')
