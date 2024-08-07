# Enviando E-Mails SMTP com Python
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15355208#overview
import os
from string import Template
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv # type: ignore

load_dotenv()

# Caminho arquivo HTML
CAMINHO_ARQUIVO = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente # Enviando para o mesmo E-Mail (para si mesmo)

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este e o assunto do E-Mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8') # 'html' or 'plain' for text
mime_multipart.attach(corpo_email)

# Abrindo o SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() # Extended Hello para inicar a conexão com o SMTP
    server.starttls() # Para iniciar uma conexão segura com o servidor
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart) # Enviando a mensagem
    print('E-Mail enviado com sucesso!')
