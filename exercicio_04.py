#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = input('Digite a Nota do 1o. Bimestre: ')
nota2 = input('Digite a Nota do 2o. Bimestre: ')
nota3 = input('Digite a Nota do 3o. Bimestre: ')
nota4 = input('Digite a Nota do 4o. Bimestre: ')
media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4
print('Sua Média final é '+ str(media) )