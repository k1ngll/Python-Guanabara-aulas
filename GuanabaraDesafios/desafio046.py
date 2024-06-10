'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

🎇🎇🎆🎆🎉🎉🎊🎊
'''
import time,emoji

for count in range(10, -1 , -1):
    print(count)
    time.sleep(1)
print('\n')


time.sleep(0.5)
print('🎇🎇🎇🎇🎇🎇🎇🎇\n\033[32mFELIZ ANO NOVO!!!!\033[m\n🎆🎆🎆🎆🎆🎆🎆🎆')