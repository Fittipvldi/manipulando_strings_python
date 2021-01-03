nome = 'henrique'
subString = nome[1:3] # pega da posição 1 à 3
print(subString)

frase1 = 'meu nome é henrique'
subString = frase1[4:] # pega da posição 4 ao final
print(subString)

argumento = 'https://www.youtube.com/watch?v=qd26lV3TLLU'
index = argumento.find('=') # retorna a posição do caracter encontrado
subString = argumento[index + 1:] # index + 1 para que não seja retornado o '='
print(subString)

frase2 = 'eu fui splitado'
lista_frase = frase2.split(' ') # o espaço é o delimitador no qual define o fatiamento
print(lista_frase)

frase3 = 'meu nome é Denis'
frase_replace = frase3.replace('Denis', 'Henrique', ) # substituição através da identificação da string
                                                      # terceiro argumento é a quantidade de substituições
print(frase_replace)

url_verdadeira = 'https://meusite.com.br'   
url1 = 'https://meusite.com.br/estouaqui'
url2 = 'https://meusyte.com.br/naoestouaqui'
print(url1.startswith(url_verdadeira), url2.startswith(url_verdadeira)) # verifica se o começo é == url_verdadeira
