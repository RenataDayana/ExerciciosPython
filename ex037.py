'''
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''

n = int(input('Informe um número inteiro: '))
esc = int(input('''Escolha a base de conversão: 
[1] binário
[2] octal
[3] hexadecimal
'''))
if esc == 1:
    print('O número {} convertido para binário é {}'.format(n,bin(n)))
elif esc == 2:
    print('O número {} convertido para octal é {}'.format(n,oct(n)))
elif esc == 3:
    print('O número {} convertido para hexadecimal é {}'.format(n,hex(n)))
else:
    print('Opção inválida! Tente novamente.')

