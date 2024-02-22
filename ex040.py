'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
'''
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Sua nota final é {:.1f}. Parabéns você foi aprovado!'.format(media))
elif media < 5:
    print('Sua nota final é {:.1f}. Você foi reprovado!'.format(media))
else:
    print('Sua nota final é {}. Você está de recuperação!'.format(media))
