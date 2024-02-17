# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o salário do funcionário: R$ '))
novosalario = salario + (salario*15/100)
print('O salário do funcionário é R${:.2f},com o aumento de 15%, passa a receber R${:.2f}.'.format(salario,novosalario))