# Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

number = int(input('enter a number : '))

double = number * 2
triple = number * 3
square_root = number ** (1/2)

print(' the number is: {}. \n the double is: {}. \n the triple is: {}. \n and the square root is:{:.2f}.'
      .format(number, double, triple, square_root))

#sem variaveis

print('o dobro é {}. \n o triplo é {}. \n a raiz quadrada de {} é {}.'.format((number*2),(number*3),number ,pow(number,(1/2))   ))