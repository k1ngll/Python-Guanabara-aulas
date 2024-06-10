#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

ano_atual = datetime.date.today().year

cont_menores = 0
cont_maiores = 0

for cont in range (0,7):
    ano = int(input('Em que ano você nasceu?'))
    idade = ano_atual - ano
    if idade < 21:
        cont_menores += 1
    else:
        cont_maiores += 1



print(f'{cont_menores} Pessoas ainda não antigiram a maioridade\n{cont_maiores} Pessoas ja antigiram a maioridade')

