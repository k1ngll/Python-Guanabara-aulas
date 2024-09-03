#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random,time
print('\n')
print('-=-' * 10)
print('Advinhe o Número')
print('-=-' * 10)
print('\n')

computador_escolha = random.randint(1,10)
jogador_escolha = 0

cont_jogadas = 1

while jogador_escolha != computador_escolha:
    jogador_escolha = int(input('Adivinhe o número: '))
    print('PROCESSANDO......')
    time.sleep(0.5)
    if jogador_escolha != computador_escolha:
        print('Você errou, Tente novamente')
        cont_jogadas += 1
    else:    
        print('\nVocê Acertou!!!')
        
print(f'Você precisou de {cont_jogadas} escolhas para acertar o número {computador_escolha} ')