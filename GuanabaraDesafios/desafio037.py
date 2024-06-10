#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Enter a number: '))

print(f'''
[1] - binary
[2] - octal
[3] - hexadecimal
''')
menu = int(input('Choose one of the conversion bases: '))

if menu == 1:
    binary_number = bin(number)[2:]
    print(f'the integer number {number} is {binary_number} in binary')
elif menu == 2:
    octal_number = oct(number).replace("0o", "")
    print(f'the integer number {number} is {octal_number} in octal')
elif menu == 3:
    hexa_number = hex(number).replace("0x","").upper()
    print(f'the integer number {number} is {hexa_number} in hexadecimal')
else:
    print('Invalid choice')