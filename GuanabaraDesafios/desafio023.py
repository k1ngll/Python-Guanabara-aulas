'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: 1834
unidade:4
dezena:3
centena:8
milhar:1
'''
def validar():
    if num < 0 or num > 9999:
        print('Número invalido')
    elif num >= 0 and num < 10:
        num_str = str(num)
        print(f"""
        Unidade:{num_str[0]}
        dezena:{0}
        centena:{0}
        milhar:{0}
        """)

    elif num >= 10 and num < 99:
        num_str = str(num)
        print(f"""
        Unidade:{num_str[1]}
        dezena:{num_str[0]}
        centena:{0}
        milhar:{0}
        """)
    elif num >= 100 and num < 999:
        num_str = str(num)
        print(f"""
        Unidade:{num_str[2]}
        dezena:{num_str[1]}
        centena:{num_str[0]}
        milhar:{0}
            """)
    elif num >= 1000 and num < 9999:
        num_str = str(num)
        print(f"""
        Unidade:{num_str[3]}
        dezena:{num_str[2]}
        centena:{num_str[1]}
        milhar:{num_str[0]}
        """)

num = int(input('digite um numéro entre 0 a 9999:'))

validar()

#Outro metodo
#Metodo matematico

n2 = int(input('Digite um número: '))

u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10

print(f"""
Analisando o número {n2}
unidade: {u}
dezena: {d}
centena: {c}
milhar: {m}""")