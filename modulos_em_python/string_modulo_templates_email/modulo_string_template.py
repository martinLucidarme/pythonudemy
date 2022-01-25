# para parametrar a pagina html, digit html na pagina e ctrl+'espaço'

from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Li', data=data_atual)


msg = MIMEMultipart()
msg['from'] = 'Martin'
msg['to'] = meu_email  # qual email vai RECEBER a msg
msg['subject'] = 'Atenção: email teste'

corpo = MIMEText(corpo_msg, 'html', _charset='utf-8')  # Se for so uma frase: MIMEText('so uma frase')
msg.attach(corpo)

with open('image_email.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # manda um oi
    smtp.starttls()  # obrigatorio por seguranca
    smtp.login(meu_email, minha_senha)  # aqui é os credenciais de quem ENVIA
    smtp.send_message(msg)
    print('email enviado')
