'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

year = datetime.date.today().year

birth_year = int(input("What's your year of birth?"))
age = year - birth_year
print(f'you have {age} years old')

# idade que ja passou
years_overdue = age - 18

# idade que falta
years_remaining = 18 - age

if age == 18:
    print('\nYou need to enlist in the army')

elif age < 18:
    print(f"You will still need to enlist in the military service. ")
    print(f"There are {years_remaining} years left until enlistment.")
    print(f"Your enlistment will be in year {year + years_remaining}")
elif age > 18:
    print("\nthe time for enlistment has already passed")
    print(f"{years_overdue} years past the enlist time")
    print(f"Your enlistment was in year {year - years_overdue}")