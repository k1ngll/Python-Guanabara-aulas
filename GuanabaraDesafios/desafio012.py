# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

#15% = 15/100 , 20% = 20/100

price = float(input('the price of the product? US$'))
discount = float(input('how much of discount do you have?'))

value_product = price - (price * (discount/100))
money_saved = price * (discount/100)

print('The Price of the product with {}% OFF is US${:.2f}'.format(discount, value_product))

print("you've saved US${:.2f}".format(money_saved))
