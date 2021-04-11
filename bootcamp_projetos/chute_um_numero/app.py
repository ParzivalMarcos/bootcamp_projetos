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


def main():
    apresentacao()
    numero_secreto = gera_numero_aleartorio()

    while True:
        numero_chutado = int(input('Chute um número de 1 a 100: '))

        if numero_secreto == numero_chutado:
            print('Voce Acertou !!')

            sair = input('Deseja continuar?\nPara sair digite s \
                 \nPara continuar, aperte a tecla ENTER\n -> ')
            if sair.lower() == 's':
                break
            else:
                numero_secreto = gera_numero_aleartorio()
                
                
        elif numero_secreto < numero_chutado:
            print('Chute um numero menor\n')
        else:
            print('Chute um numero maior\n')
    

if __name__ == '__main__':
    main()
