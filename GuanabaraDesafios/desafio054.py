#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

ano_atual = datetime.date.today().year

cont_menores = 0
cont_maiores = 0

for cont in range (1,8):
    ano = int(input(f'Em que ano a {cont}ª pessoa nasceu?'))
    idade = ano_atual - ano
    if idade < 21:
        cont_menores += 1
    else:
        cont_maiores += 1



print(f'\n{cont_menores} Pessoas ainda não antigiram a maioridade\n{cont_maiores} Pessoas ja antigiram a maioridade')

