salario = float(input('Parabéns, você ganhará um aumento de salário! Digite aqui seu salário atual:'))
aumento = float(input('Digite agora quanto % será aumentado do salário:'))
salaument = salario+(salario*(aumento/100))
print('Parabéns, seu salário foi aumentado para {:.2f}'.format(salaument))