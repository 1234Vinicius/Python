idade = int(input('Digite a sua idade: '))
if idade <18:
    print('\033[31mVocê é menor de idade'.format(idade))
else:
    print('\033[36mVocê é maior de idade'.format(idade))