'''
Style:
0 -> none
1 -> bold
4 -> underline
7 - > Negative
Text: 30 White, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 cyan and 37 gray.
Background: 40 Black, 41 Red, 42 Green, 43 Yellow, 44 Blue, 45 Purple, 46 Cyan and 47 White.
\033[0;33;44m
'''

print('\033[7;30m Hello,World\033[m')

a = 3
b = 5
print(f'os valores são \033[33m{a}\033[m e \033[31m{b}\033[m')

nome = 'Sena Junior'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'}

print(f" Olá prazer em te conhecer {cores['pretoebranco']}{nome}{cores['limpa']}")

