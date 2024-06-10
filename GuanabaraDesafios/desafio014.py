# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_celsius = float(input('digite a temperatura em ºC: '))

temperatura_fahrenheit = (temperatura_celsius * 1.8 + 32)

print('a temperatura em de {} ºC é {} ºF'.format(temperatura_celsius,temperatura_fahrenheit))