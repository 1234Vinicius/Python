nota01 = int(input('Digite a sua nota do primeiro bimestre: '))
nota02 = int(input('Digite a sua nota do segundo bimestre: '))
nota03 = int(input('Digite a sua nota do terceiro bimestre: '))
nota04 = int(input('Digite a sua nota do quarto bimestre: '))
media = (nota01 + nota02 + nota03 + nota04)/4
print('A sua nota final foi de {}'.format(media))
if media >=6:
    print('\033[34mPARABÉNS! VOCÊ PASSOU DE ANO!')
else:
    print('\033[31mVOCÊ REPETIU! ESTUDE MAIS DA PRÓXIMA VEZ...')