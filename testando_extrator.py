from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = 'https://www.cambio.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150'

argumentosUrl = ExtratorArgumentosUrl(url)  # instancia
argumentosUrl2 = ExtratorArgumentosUrl(url)  # instancia

moedaOrigem, moedaDestino = argumentosUrl.extrai_argumentos()
valor = argumentosUrl.extraiValor()

print(moedaOrigem, moedaDestino, valor)
print(len(argumentosUrl))
print(argumentosUrl)

print(id(argumentosUrl))
print(id(argumentosUrl2))
print(argumentosUrl == argumentosUrl2)