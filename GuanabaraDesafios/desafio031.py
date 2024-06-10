#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longas.


viagem = float(input('Qual a distância da viagem em Km: '))

if viagem <= 200:
    passagem = viagem * 0.50

else:
    passagem = viagem * 0.45

print(f'O preço da passagem custa R${passagem:.2f}')
