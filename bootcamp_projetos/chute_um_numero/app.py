import random

def apresentacao():
    apresentacao = """
    Jogo de adivinhação

    Aperte enter para começar\n\n
    """

    input(apresentacao)


def gera_numero_aleartorio():
    print('Gerando um número entre 1 e 100...')

    return random.randint(1, 100)

def captura_dado_usuario():
    try:
        return int(input('Chute um número de 1 a 100: '))
    except ValueError:
        print('Por favor, digite um número inteiro')



def main():
    apresentacao()
    gera_numero_aleartorio()


if __name__ == '__main__':
    # numero = gera_numero_aleartorio()
    captura_dado_usuario()

