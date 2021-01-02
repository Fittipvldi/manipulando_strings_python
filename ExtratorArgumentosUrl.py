class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):   # chama a validação da URL
            self.url = url
        else:
            raise LookupError('URL inválida!')
    

    @staticmethod           # método estático, no qual não necessita do self
    def urlEhValida(url):
        if url:             # se a tiver algo na URL = True senao False
            return True
        else:
            return False

    
    def extrai_argumentos(self):
        buscaMoedaOrigem = 'moedaorigem'
        buscaMoedaDestino = 'moedadestino'

        '''indiceInicialMoedaOrigem = self.url.find('=') + 1
        indiceFinalMoedaOrigem = self.url.find('&')'''
        indiceInicialMoedaOrigem = self.url(buscaMoedaOrigem) + len(buscaMoedaOrigem) + 1
        indiceFinalMoedaOrigem = self.url.find('&')
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        '''indiceInicialMoedaDestino = self.url.find('=', 15) + 1 # ponto de partida, posição 15'''
        indiceInicialMoedaDestino = self.url.find(buscaMoedaDestino) + len(buscaMoedaDestino) + 1
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino

