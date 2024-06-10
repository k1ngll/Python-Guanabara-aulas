'''18 
faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
-> cos 
^ seno
| tangent
'''
import math

ang = int(input('Digite um angulo: '))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('o angulo é {}º que tem o valor de: \nseno {:.2f} \ncosseno {:.2f} \ntangente {:.2f}'.format(ang, seno, cosseno,tangente))