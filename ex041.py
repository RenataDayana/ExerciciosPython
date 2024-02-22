import datetime
from datetime import date
'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
ano = int(input('Informe o ano do nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} anos. Sua categoria é MIRIM'.format(idade))
elif idade <=14:
    print('Você tem {} anos. Sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Sua categoria é JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos. Sua categoria é SÉNIOR'.format(idade))
else:
    print('Você tem {} anos. Sua categoria é MASTER'.format(idade))

