# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
# km hm dam m dm cm mm
# 0.001 0.01 0.1 1 10 100 1000
#1 m = 100 cm
#1 cm = 10 mm
#1 m = 1000 mm

medida = float(input('Conversor de medidas. Digite um valor em metro: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000

dam = medida / 10
hm = medida / 100
km = medida / 1000


print(' Conversor de medidas :\n {} km \n {} hm \n {} dam \n {} m \n {} dm \n {} cm \n {} mm'.format(km,hm,dam,medida,dm,cm,mm))

