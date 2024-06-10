nome = str(input('digite seu nome: '))

print(f'tenha um bom dia {nome}')

if nome == 'Sena':
    print('que nome bonito!')
elif nome == 'Pedro' or nome == "Maria" or nome == "Gabriel":
    print('seu nome é bem popular')
elif nome in 'Ana Cláudia Julia Jéssica Juliana yasmin':
    print('Belo nome feminino')
else:
    print('Seu nome é normal!')