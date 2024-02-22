from random import randint
# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('-=-' * 10)
print('Vamos jogar Jokenpô!')
print('-=-' * 10)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print ('''Opções:: 
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual a sua jogada? '))
print('Jogador jogou {}'.format(itens[jogador]))
print("Computador jogou {}".format(itens[computador]))

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Opção inválida, tente novamente!')

if computador == 1:
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Opção inválida, tente novamente!')
if computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Opção inválida, tente novamente!')



