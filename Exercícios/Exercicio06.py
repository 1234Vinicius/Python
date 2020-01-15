print('Vamos calcular a área de uma parede para então pintá-la (em metros quadrados) e saber quanta tinta será necessária.')
alt = float(input('Qual a altura da parede?'))
larg = float(input('Qual a largura da parede?'))
area = alt*larg
print('A área da parede é de {:.3f} metros quadrados'.format(area))
tinta = area/2
print('Você então precisará de {:.1f} litros de tinta'.format(tinta))