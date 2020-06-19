# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salarioHora = input('Quanto ganha por hora trabalhada? ')
horaTrab = input('Quantas horas trabalhadas? ')
salarioMes = int(salarioHora) * int(horaTrab)
print('Salário para o mês: ' + str(salarioMes))