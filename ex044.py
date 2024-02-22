'''
Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Informe o preço do produto: R$ '))
forma = int(input('''Informe a condição de pagamento:
[1] Dinheiro/cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão
'''))

if forma == 1:
    precofinal = preco - (preco * 10/100)
    print('O preço final do produto é R$ {}'.format(precofinal))

elif forma == 2:
    precofinal = preco - (preco * 5 / 100)
    print('O preço final do  produto é R$ {}'.format(precofinal))

elif forma == 3:
      print('O preço final do  produto é R$ {}'.format(preco))
elif forma == 4:
    parcela = int(input('Em quantas vezes deseja parcelar: '))
    if parcela >= 4:
        precofinal = preco + (preco * 20 / 100)
        print('O preço do final do produto será R$ {}'.format(precofinal))
    else:
        print('Opção inválida.')
