'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

phrase = str(input('Type a phrase:')).strip()

print(
f"""
appear 'A' {phrase.upper().count('A')} times in the sentence 
O 'A' aparece primeira na posição de indice -> {phrase.upper().find('A')}
O 'A' aparece pela ultimas vez na posição de indice -> {phrase.upper().rfind('A')}
""")

