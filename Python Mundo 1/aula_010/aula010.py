n1 = float(input('digite a nota da av1: '))
n2 = float(input('digite a nota da av2: '))

media = (n1+n2)/2

if media >= 6:
    print(f'{media:.1f} você foi aprovado')
else:
    print(f'{media:.1f} você foi reprovado')