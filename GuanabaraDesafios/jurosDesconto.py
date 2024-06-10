#simule juros e desconto
print(' desconto de 10% off no mause gamer a vista ou parcele com juros')
valor_mouse = 100

resp = int(input('digite 1 para comprar a vista ou digite 2 para parcelar:'))

if resp ==1:
    valor_mouse_10 = valor_mouse - (valor_mouse * 10/100)
    print('o valor do mouse gamer agora é R${:.2f}'.format(valor_mouse_10))
else:
    print('10% de juros no mause')
    valor_mouse_10 = valor_mouse + (valor_mouse * 10/100)
    print('o valor do mouse gamer agora é R${:.2f}'.format(valor_mouse_10))
