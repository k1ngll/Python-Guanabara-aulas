# Crie um programa que faça o computador jogar Jokenpô com você.
#Pedra : 👊
#Papel : ✋
#Tesoura ✂ ✌
import emoji, random, time

pedra = '👊'
papel = '✋'
tesoura = '✌'
jokenpo = [pedra,papel,tesoura]

print('-=-' * 10)
print('Bem vindo ao jogo do JOKENPÔ ')
print('-=-' * 10)

cpu_choose = random.choice(jokenpo)


option = int(input('[0] - Pedra\n[1] - Papel\n[2] - Tesoura\nescolha a sua opção:'))
player_choose = jokenpo[option]

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)

if player_choose == cpu_choose: # EMPATE
    print(f'Player {player_choose} x {cpu_choose} CPU\nDRAW')

elif player_choose == jokenpo[0] and cpu_choose == jokenpo[1]:  # pedra x papel
    print(f'Player {player_choose} x {cpu_choose} CPU\nCPU WINS')

elif player_choose == jokenpo[0] and cpu_choose == jokenpo[2]: #pedra x tesoura
    print(f'Player {player_choose} x {cpu_choose} CPU\nPLAYER WINS')

elif player_choose == jokenpo[1] and cpu_choose == jokenpo[0]: # papel x pedra
    print(f'Player {player_choose} x {cpu_choose} CPU\nPLAYER WINS')

elif player_choose == jokenpo[1] and cpu_choose == jokenpo[2]: # papel x tesoura
    print(f'Player {player_choose} x {cpu_choose} CPU\nCPU WINS')

elif player_choose == jokenpo[2] and cpu_choose == jokenpo[0]: # tesoura x pedra
    print(f'Player {player_choose} x {cpu_choose} CPU\nCPU WINS')
elif player_choose == jokenpo[2] and cpu_choose == jokenpo[1]: # tesoura x papel
    print(f'Player {player_choose} x {cpu_choose} CPU\nPLAYER WINS')


else:
    print('Invalid Answer')


