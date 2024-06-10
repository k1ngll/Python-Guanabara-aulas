# Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

#Solicita o nome para o usuario
name = str(input('Enter your name:')).strip()

#Se achar o nome 'silva' no nome da pessoa colocado todo em minusculo ent vai printar que achou se não,não achou


if name.lower().find('silva') >= 0:
    print('This person have Silva in their name')
else:
    print('This person does not have Silva in their name')

#outro metodo

nome = str(input('Digite seu nome completo: ')).strip()

print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")