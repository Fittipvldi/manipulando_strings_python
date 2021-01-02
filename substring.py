nome = 'henrique'
subString = nome[1:3] # pega da posição 1 à 3
print(subString)

frase = 'meu nome é henrique'
subString = frase[4:] # pega da posição 4 ao final
print(subString)

argumento = 'https://www.youtube.com/watch?v=qd26lV3TLLU'
index = argumento.find('=') # retorna a posição do caracter encontrado
subString = argumento[index + 1:] # index + 1 para que não seja retornado o '='
print(subString)

frase_splitada = 'eu fui splitado'
lista_frase = frase_splitada.split(' ') # o espaço é o delimitador no qual define o fatiamento
print(lista_frase)
