''' 
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
import time
num_cpu = random.randint(0,5)

print('-=-' * 30)
print('DE 0 A 5 ADIVINHE O NÚMERO QUE EU PENSAR')
print('-=-' * 30)
num_user = int(input('Qual você acha que é o número?: '))

print('PROCESSANDO....')
time.sleep(0.1)

if num_user == num_cpu:
    print(f'o computador escolheu {num_cpu},Você venceu o jogo')
else:
    print(f'o computador escolheu {num_cpu},Você perdeu o jogo')