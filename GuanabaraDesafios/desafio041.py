'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

import datetime
year = datetime.date.today().year
#year = datetime.datetime.now().year

birth_year = int(input('What was the year you were born? '))
age = year - birth_year

if age <= 9:
    print(f'O atlela tem {age} anos.\nCategoria: mirim')
elif age <= 14:
    print(f'O atlela tem {age} anos.\nCategoria: infantil')
elif age <= 19:
    print(f'O atlela tem {age} anos.\nCategoria: Júnior')
elif age <= 25:
    print(f'O atlela tem {age} anos.\nCategoria: Sênior')
else:
    print(f'O atlela tem {age} anos.\nCategoria: Master')
