import math
ang = int(input('Informe um ângulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('SENO: {:.2F}, COSSENO: {:.2F} E TANGENTE: {:.2F}'.format(s,c,t))