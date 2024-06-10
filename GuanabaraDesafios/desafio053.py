#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: APOS A SOPA 

frase = str(input('Digite uma frase: ')).strip()

new_frase = frase.replace(' ','')

frase_inversa = new_frase[::-1]

print(new_frase)
print(frase_inversa)

if frase_inversa[::-1] == new_frase: # se a frase invertida , desinvertida for igual a frase normal ent é um polindromo
    print(f"A frase '{frase}' é um palíndromo da frase {frase_inversa}'")
else:
    print(f"A frase '{frase}' não é um palidromo da frase '{frase_inversa}'")
