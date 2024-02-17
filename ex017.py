'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input('Informe o comprimento do cateto oposto:'))
ca = float(input('Informe o comprimento do cateto adjancente: '))
hi = math.hypot(co,ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))

