#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual era a velocidade do carro quando passou no radar em km/h: '))

if speed > 80:
    print('Você foi multado')
    multa = (speed - 80) * 7
    print(f'voce tera que pagar R${multa:.2f}')
else:
    print('Bom dia , dirija com segurança')