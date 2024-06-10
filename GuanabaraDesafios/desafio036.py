'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print('-=-'* 10)
print('Bank Loans Simulator')
print('-=-'* 10)

house_value = float(input('Enter the house value: R$'))
salary = float(input('Enter your salary: R$'))
payment_years = int(input('How many years do you want to pay the installments ? '))

salary_cap = salary * 30/100
installment = payment_years * 12
prestacao_value = house_value / installment

print("\n\n")

if prestacao_value > salary_cap:
    print(f"To buy a house of R${house_value:.2f} in {payment_years} years the installment will be R${prestacao_value:.2f}\nYou cant buy the house")

else:
    print(f"\nYou can buy the house\nyou just need to pay {installment}x de R${prestacao_value:.2f} to buy the house")
