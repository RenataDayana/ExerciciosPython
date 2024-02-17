'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
larg = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
a = larg * alt
tinta = a/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(larg,alt, a))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))