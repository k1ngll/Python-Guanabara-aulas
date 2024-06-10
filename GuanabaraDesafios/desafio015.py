'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado '''

dias = int(input('Por quantos dias você alugou o carro? '))

kilometragem = float(input('quantos KM você percorreu? '))

preco_dias = dias * 60
preco_km = kilometragem * 0.15

preco_total = preco_dias + preco_km

print('O total a pagar por ter alugado por {} dias e andando {} km é R${:.2f}'.format(dias,kilometragem,preco_total))