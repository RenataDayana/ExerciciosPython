#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Informe o preço do produto: R$ '))
novopreco = preco - ((preco * 5)/100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto custará R$ {:.2f}'.format(preco,novopreco))