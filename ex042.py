'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''

r1 = int(input('Informe o primeiro segmento: '))
r2 = int(input('Informe o segundo segmento: '))
r3 = int(input('Informe o terceiro segmento: '))

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é equilátero')

    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isóceles')
else:
 print('Os segmentos acima não podem formar triângulo.')