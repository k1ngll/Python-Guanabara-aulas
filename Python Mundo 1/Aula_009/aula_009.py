#Manipulando Texto | Cadeia de strings

#Curso em Video Python
#0___________________20
# ao total tem 21 caracteres 0 a 20

frase = 'Curso em Video Python'

#ANÁLISE
print('ANÁLISE') # analise da cadeia de strings
print(f"o tamanho da minha string 'frase' é {len(frase)} caracteres") # tamanho da string
print(f"na frase temos {frase.count('o')} o minusculos") # conte quantos o minusculos tem na frase
print(f"na frase temos {frase.count('o',0,13)} o minusculo entre o indice 0 e 12") # conte quantos o minusculos tem na frase, do 0 ao 13-1
print(f"em que indice começa a palavra 'deo', no indice {frase.find('deo')}") # mostre em que indice começa uma palavra especifica
print(f" procure uma palavra que não esta na frase e retornara {frase.find('android')}") # ao procurar uma palavra que não esta na frase retorna um indice -1 dizendo
#que não encontrou na frase
teste = 'Curso' in frase # recebe true or false para saber se tem a palavra na sua frase
print(f"\nExiste a palavra 'Curso' na minha frase? {teste}\n")

#FATIAMENTO motodos de fatiamento
print('FATIAMENTO')
print(f"mostre o indice 9 = {frase[9]}")
print(f"de 9 a 13 - 1  = {frase[9:13]}")
print(f"de 9 a 21 - 1  = {frase[9:21]}")
print(f"de 9 a 21 - 1, pulando de 2 em 2 = {frase[9:21:2]}")
print(f"do inicio a 5 - 1 = {frase[:5]}")
print(f"do 15 até o final = {frase[15:]}")
print(f"do 9 até o final, de 3 em 3 = {frase[9::3]}\n")

#Transformação
print('TRANSFORMAÇÃO')
transformacao_frase = frase.replace('Python','Android') # substitui uma palavra pela outra na frase
print(f"a antiga frase era '{frase}' e agora é '{transformacao_frase}'\n")

print('UPPER | lower') # maisculo e minusculo
print(f"Tudo vai para maisculo --> {transformacao_frase.upper()}")
print(f"Tudo vai para minusculo -->{transformacao_frase.lower()}\n")

print('Captalizer | title') # primeira letra maisculo e tudo minusculo | todas as palavras começam com minusculo
print(transformacao_frase)
print(f"Captalizer = {transformacao_frase.capitalize()}")
print(f"Title = {transformacao_frase.title()}")

#Excluir caracteres inuteis = Strip
print('STRIP | LSTRIP | RSTRIP')
new_frase = '   Aprenda Python  '
print(f"A frase '{new_frase}' com o strip passa a ser '{new_frase.strip()}'")
print(f"A frase tirando os espaços da esquerda é '{new_frase.lstrip()}' e tirando os da direita é '{new_frase.rstrip()}'")

#DIVISÃO
print('DIVISÃO')
#METODO SPLIT divide
frase_splitada = frase.split()
print(f"a frase splitada é {frase_splitada}")

#Metodo Join para reunir a frase dividida
print(f"juntar a frase splitada fica '{'-'.join(frase_splitada)}'")

