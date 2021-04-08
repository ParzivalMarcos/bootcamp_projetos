import random
import os
from time import sleep


def inicio():
    # Comando para limpar a tela
    # Função lambda com a finalidade de limpar o terminal e será chamada pelo comando 'clear()'
    clear = lambda: os.system('cls')  

    # Informações das listas
    valores_das_listas = gera_listas()


    # Tela Inicial
    clear()
    opcoes_usuario = ''
    while opcoes_usuario != 'parar':
        print('*' * 65)
        print('Olá, este é um gerador de dados aleartórios')
        print('Por favor, digite as opções abaixo, para que seja gerado (separar por virgulas)')
        print('Caso queira sair do programa a qualquer momento, digite "parar"')
        print('*' * 65)

        opcoes_usuario = list(input('[1]: Nomes\n[2]: E-mails\n[3]: Telefones\n[4]: Cidades\n[5]: Estados\n->'))
        if opcoes_usuario == 'parar':
            break

        opcoes_valores = [opcao for opcao in opcoes_usuario if opcao != ',']      
        opcoes_usuario = str(input('Deseja que os dados sejam gravados em um arquivo? '))
        if opcoes_usuario == 'parar':
            break

        clear()

        for opcao in opcoes_valores:
            print(random.choice(valores_das_listas[opcao]))

        aguarde(5)


# Listas das opções
def gera_listas():
    
    opcoes = {
        '1':['Marcos', 'Maria', 'Kalienne', 'Ideltudes', 'Tom'],
        '2': ['marcolim977@gmail.com', 'marcoslimamarinhodev@gmail.com', 'teste@teste.com', 'um23@numeros.com', 'abc@letras.com'],
        '3': ['11 99999-9999', '00 12345-6789', '22 34567-8910', '33 67890-1234', '44 56789-0123'],
        '4': ['São Paulo', 'Fortaleza', 'Salvador', 'Marcosgrado', 'Manaus'],
        '5': ['SP', 'CE', 'BH', 'AM', 'MG']
    }

    return opcoes


def aguarde(segundos):
    for s in range(segundos):
        print(f'Retornando ao inicio em {s} segundos...')
        sleep(1)


if __name__ == "__main__":
    inicio()