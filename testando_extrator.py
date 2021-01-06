from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = 'https://www.cambio.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150'

argumentosUrl = ExtratorArgumentosUrl(url)  # instancia

moedaOrigem, moedaDestino = argumentosUrl.extrai_argumentos()
valor = argumentosUrl.extraiValor()

print(moedaOrigem, moedaDestino, valor)
print(len(argumentosUrl))
