#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

#Pede o nome da cidade
city = str(input('Enter the city name:'))

#Splita o nome da cidade em uma lista
s_city = city.split()

#Pega o indice 0 da cidade que é o primeiro nome, Coloca em tudo em maisculo e dar find na palavra 'SANTO' que esta em maisculo.
#Iguala a 0 porque se o find acha a palavra ele da o indice dela.

if s_city[0].upper().find('SANTO') == 0:
    print(f"The city first name have 'SANTO'")
else:
    print(f"The city does not have 'SANTO' in the first name")

# OUTRO METODO

cidade = str(input('Em que cidade vc mora? ')).strip()
print(cidade[:5].lower() == 'santo')
