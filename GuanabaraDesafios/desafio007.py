# Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média

nota1 = float(input('digite a nota da av1:'))
nota2 = float(input('digite a nota da av2:'))

media = (nota1 + nota2 ) / 2

print('sua media é {:.1f}'.format(media))