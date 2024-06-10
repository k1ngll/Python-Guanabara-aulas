#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Qual a tabuada que você deseja?: '))

for cont in range(1,11):
    print(f'{num} x {cont:2} = {cont*num}')
    
    