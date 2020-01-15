numero = int(input('Me diga qualquer numero: '))
resultado = numero %2
if resultado == 0:
    print('\033[33mEsse numero {} é PAR'.format(numero))
else:
    print('\033[34mEsse numero {} é ÍMPAR'.format(numero))