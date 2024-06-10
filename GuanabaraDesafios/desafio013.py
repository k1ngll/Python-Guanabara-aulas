#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,com 15% de aumento.
#15/100 = 15% = 1.15
# meu salario é 100 ent 15% do meu salario é 15 reais, somo os 15 cm meu salario e este é o aumento
name_func = str(input('what is your name: '))
sal_func = float(input('enter your salary: '))
sal_increase = int(input('how much % will increase in the salary: '))

new_sal = sal_func + (sal_func * sal_increase/100)

print('{} earned US${:.2f} per month, with an increase of {}% in her/him salary,now earns US${:.2f} per month'.format(name_func,sal_func,sal_increase,new_sal))

