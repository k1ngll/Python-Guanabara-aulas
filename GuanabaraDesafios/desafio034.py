#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 10/100
    salario_atual = aumento + salario
    print(f'Seu salario era {salario} e com aumento de 10% foi para {salario_atual}')
else:
    aumento = salario * 15/100
    salario_atual = aumento + salario
    print(f'Seu salario era {salario} e com aumento de 15% foi para {salario_atual}')