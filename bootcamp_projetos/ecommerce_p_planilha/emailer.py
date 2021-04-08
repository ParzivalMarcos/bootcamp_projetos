import yagmail
import json

def envia_email(destinatario):
    with open("info_email.json", "r") as arquivo:
        conteudo_arquivo = json.load(arquivo)
        email = conteudo_arquivo['email']
        senha = conteudo_arquivo['senha']

    usuario = yagmail.SMTP(user=email, password=senha)

    usuario.send(
        to=destinatario, 
        subject='Relatório de Preços', 
        contents='Em anexo, segue relatório atualizado', 
        attachments='produtos_e-commerce.xlsx')

    print('\nEMAIL ENVIADO !!!!\n')