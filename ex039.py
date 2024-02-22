'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 18:
    saldo = idade - 18
    print('Você devia ter se alistado há {} anos.'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento.'.format(saldo))
else:
    print('Você tem que se alistar imediatamente!')
2007
