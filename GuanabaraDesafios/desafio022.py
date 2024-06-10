'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços). print(len(name.replace(' ',''))) ou seja de replace onde tem espaço para sem espaço.
- Quantas letras tem o primeiro nome. primeiro splita o nome para uma lista e depois verifica o tamanho com o len no indice escolhido
name_splitado = name.split()
len(name_splitado[0])
'''

name = str(input('Enter your name:'))

print(f"""
nome com todas as letras maiúsculas = {name.upper()}
nome com todas as letras minúsculas = {name.lower()}
O nome tem {len(name.replace(' ',''))} letras ao todo. 
O primeiro nome tem {len(name.split()[0])} letras
""")

#Outro metodo

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu pimeiro nome tem {nome.find(' ')} letras")



