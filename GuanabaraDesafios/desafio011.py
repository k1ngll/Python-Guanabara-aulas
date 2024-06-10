'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro
de tinta, pinta uma área de 2 metros quadrados.
'''

wall_height = float(input('digite a altura da parede em metros :'))
wall_width = float(input('digite a largura da parede em metros :'))

area = wall_height * wall_width

# 1 L Pinta 2 m²

area_por_litro = 2 # m² por litro

pintura_necessaria = area / area_por_litro

print('A parede tem dimensão de {}x{} e sua área é {}m².'.format(wall_height, wall_width,area))
print('É necessario {} litros de tinta para pintar a parede completa.'.format(pintura_necessaria,wall_height,wall_width))
