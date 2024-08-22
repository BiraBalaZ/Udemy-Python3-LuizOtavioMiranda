from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

url = 'https://www.google.com'
navegador.get(url)

print(navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('Hello, Wolrd!'))
