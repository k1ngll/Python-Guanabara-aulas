#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: APOS A SOPA 

frase = str(input('Digite uma frase: ')).strip().lower()
frase_splitada = frase.split()
frase_sem_espaco = ''.join(frase_splitada) #substitui os espaços por nada
inverso = frase_sem_espaco[::-1]
#inverso_for = ''
#for letra in range(len(frase_sem_espaco) - 1,-1,-1):
#    inverso += frase_sem_espaco[letra]

if inverso == frase_sem_espaco:
    print(f'a frase {frase} é um palidromo')
else:
    print(f'A frase {frase} não é um palidromo')

print(f'Você digitou {frase}\n {frase_sem_espaco} -> {inverso} ')
