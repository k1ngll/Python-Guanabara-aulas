# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
s_nome = nome.split()
tamanho = len(s_nome)
print(len(s_nome))
print(f"Muito prazer em te conhecer!\nseu primeiro nome é {s_nome[0]}\nseu ultimo nome é {s_nome[tamanho-1]}")