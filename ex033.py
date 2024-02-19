#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > b and c > b:
    maior = c

print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))

