'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 24,9: Peso Ideal
– 25 até 29,9: Sobrepeso
– 30 até 39,9: Obesidade
– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe o seu peso: (KG)'))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O IMC dessa pessoa é {:.2f}. Abaixo do peso.'.format(imc))
elif 18.5 >= imc <= 24.9:
    print('seu IMC é igual {}. Peso ideal.'.format(imc))
elif 25 >= imc <= 29.9:
    print('O IMC dessa pessoa é {:.2f}. Sobrepeso '.format(imc))
elif 30 >= imc <= 39.9:
    print('O IMC dessa pessoa é {:.2f}. Obesidade '.format(imc))
else:
    print('O IMC dessa pessoa é {:.2f}. Obesidade mórbida '.format(imc))



