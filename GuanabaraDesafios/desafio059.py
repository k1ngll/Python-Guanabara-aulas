'''
 Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

'''
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

menu = 0
soma = 0
multi = 0
maior = valor1

while menu != 5:
    print(f'''--------------
          [1] - Soma
          [2] - Multiplicar
          [3] - Maior valor
          [4] - novos Valores
          [5] - Sair do programa
          
          ------------------
          ''')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        soma = valor1 + valor2
        print(f'a soma do {valor1:.2f} + {valor2:.2f} = {soma:.2f}')
        
    elif menu == 2:
        multi = valor1 * valor2
        print(f'A multiplicação entre o {valor1:.2f} x {valor2:.2f} = {multi:.2f}')
        
    elif menu == 3:
        if valor1 != valor2:
            if valor1 < valor2:
                maior = valor2
                print(f'O maior valor é o segundo que é igual a {maior:.2f}')
            else:
                maior = valor1
                print(f'O maior valor é o primeiro que é igual a {maior:.2f}')
        else:
            print('Os 2 valores são iguais')
            
    elif menu == 4:
        valor1 = float(input('Digite um novo primeiro valor: '))
        valor2 = float(input('Digite um novo segundo valor: '))
        
        print(f'Valores atualizados respecitivamente para {valor1:.2f} e {valor2:.2f}')
    elif menu == 5:
        print('Programa finalizado')
    else:
        print('Valor invalido')