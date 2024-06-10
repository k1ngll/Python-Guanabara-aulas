#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

year = int(input('Digite 0 para analisar o ano atual ou digite um ano qualquer: '))

if year == 0:
    year = datetime.date.today().year

'''if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'O ano {year} é ano bissexto')
        else:
            print(f'O ano {year} não é ano bissexto')
    else:
        print(f'O ano {year} é ano bissexto')

else:
    print(f'O ano {year} não é ano bissexto')
'''
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é ano bissexto')
else:
    print(f'O ano {year} não é ano bissexto')