'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
IMC = PESO/(ALTURA)²
'''

height = float(input('What is your height? (m) '))
weight = float(input('What is your weight? (kg) '))

bml = weight / height **2

if bml < 18.5:
    print(f"""
    Height: {height:.2f}m
    Weight: {weight:.2f}kg
    BML/IMC: {bml:.1f} kg/m²
    You are Underweight
    Abaixo do Peso
    """)
elif 18.5 <= bml < 25:
    print(f"""
        Height: {height:.2f}m
        Weight: {weight:.2f}kg
        BML/IMC: {bml:.1f} kg/m²
        You have a Healthy Weight
        Peso Ideal
        """)
elif 25 <= bml < 30:
    print(f"""
        Height: {height:.2f}m
        Weight: {weight:.2f}kg
        BML/IMC: {bml:.1f} kg/m²
        Overweight
        Sobrepeso
            """)

elif 30 <= bml < 40:
    print(f"""
        Height: {height:.2f}m
        Weight: {weight:.2f}kg
        BML/IMC: {bml:.1f} kg/m²
        Severe Obese
        Obesidade
                """)

elif bml >= 40:
    print(f"""
        Height: {height:.2f}m
        Weight: {weight:.2f}kg
        BML/IMC: {bml:.1f} kg/m²
        Very severely obese
        Obesidade Mórbida
        """)
