'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50  por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

d = float(input('Informe a distância da sua viagem em Km: '))
print('Você está preste a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    p = d * 0.50
    print('O preço da passagem é R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('E o preço da sua passagem será R${:.2f}'.format(p))
