'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o valor do seu salário? R$ '))
anos = int(input("Quantos anos?"))
p = casa/(anos*12)

if p <= sal*30/100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. Empréstimo aprovado!.'.format(casa, anos, p))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.Empréstimo negado!'.format(casa, anos, p))
