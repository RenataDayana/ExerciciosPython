'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''
r1 = int(input('Informe o primeiro segmento: '))
r2 = int(input('Informe o segundo segmento: '))
r3 = int(input('Informe o terceiro segmento: '))

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo.')
else:
 print('Os segmentos acima não podem formar triângulo.')