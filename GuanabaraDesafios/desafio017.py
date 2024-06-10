# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# | cateto oposto , _ adjacesnte, \ hipotenusa, ang de 90 L
#quadrado da hipotenusa é a soma dos quadrados dos catetos c²= a² + b²

import math

cateto_op = float(input('digite o valor do cateto oposto cm: '))

cateto_adj = float(input('digite o valor do cateto adjacente cm: '))

hi = math.hypot(cateto_op, cateto_adj)

soma_quad_cat = pow(cateto_op,2) + pow(cateto_adj,2)

hipotenusa = math.sqrt(soma_quad_cat)

print('o comprimento da hipotenusa é {:.2f}cm '.format(hi))