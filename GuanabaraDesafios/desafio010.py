'''
crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

US$ 1.00 = R$ 5,14

'''

real = float(input('how many Reais you have in your wallet? R$'))

dolar = real / 5.14

btc = real / 323.757

euro = real / 5.54

won = real * 265.89

print('R${:.2f} is equal \n US${:.2f} \n EU$ {:.2f} \n Won$ {:.2f} \n BTC {:} .'.format(real,dolar,euro,won,btc))