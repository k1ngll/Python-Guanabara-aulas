'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

grade1 = float(input('enter the grade of your av1: '))
grade2 = float(input('enter the grade of your av2: '))
avarage = (grade1 + grade2)/2

print(f'With a grade_1 {grade1:.1f} and a grade_2 {grade2:.1f} your avarage is {avarage:.1f}')

if avarage >= 7:
    print('APPROVED')
elif avarage >= 5 and avarage < 7:
    print('School academy cath-up / summer schools classes / recuperação')
else:
    print('Failed')