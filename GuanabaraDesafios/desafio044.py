'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('-=-'*10)
print('Bem vindo a Pichau')
print('-=-'*10)


preço = float(input('Preço das compras: R$'))

pagamento = int(input('\n[1] Pix\n[2] cartão à vista\n[3] Parcelado\nescolha a forma de pagamento:'))

if pagamento == 1:
    print('no pix')
    descont_10 = preço - (preço * 10/100)
    print(f'O valor do produto era R${preço} e com 10% de desconto agora é R${descont_10:.2f}')
elif pagamento == 2:
    print('Cartão à vista')
    desconto_5 = preço - (preço * 5/100)
    print(f'O valor do produto era R${preço} e com 5% de desconto agora é R${desconto_5:.2f}')
elif pagamento == 3:
    parcelas = int(input('Você quer dividir em quantas parcelas?'))
    if parcelas == 2:
        print(f'O valor do produto permanece R${preço} e você pagara 2x de R${preço/parcelas:.2f}')
    if parcelas >= 3:
        juros = preço + (preço * 20/100)
        print(f'O valor do produto era R${preço} com 20% de juros passa a ser R${juros:.2f} e você tera que pagar {parcelas}x de R${juros/parcelas:.2f}')
    
else:
    print('opção invalida')


