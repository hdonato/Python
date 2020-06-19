# Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

tempF = input('Digite a temperatura em graus Farenheit: ')
tempC = (5 * (int(tempF) - 32) / 9)
print('Temperatura em graus Celsius: ' + str(tempC))