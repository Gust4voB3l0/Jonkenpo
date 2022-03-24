from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*13)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-='*13)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    elif jogador == 3:
        print('Jogada invalida!')
    else:
        print('Jogada invalida!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    elif jogador == 3:
        print('Jogada invalida!')
    else:
        print('Jogada Invalida!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 3:
        print('Jogada invalida!')
    else:
        print('Jogada Invalida!')
