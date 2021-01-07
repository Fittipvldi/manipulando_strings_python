class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):   # chama a validação da URL
            self.url = url.lower()
        else:
            raise LookupError('URL inválida!')

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extrai_argumentos()
        representacaoString = 'Valor:' + self.extraiValor() + ' moeda origem: ' + moedaOrigem + 'moeda destino: ' + moedaDestino
        return representacaoString

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    @staticmethod           # método estático, no qual não necessita do self
    def urlEhValida(url):
        if url and url.startswith('https://www.cambio.com'):  # se a tiver algo na URL = True senao False && deve começar com 'https://cambio..'
            return True
        else:
            return False

    def extrai_argumentos(self):
        buscaMoedaOrigem = 'moedaorigem='.lower()
        buscaMoedaDestino = 'moedadestino='.lower()

        '''indiceInicialMoedaOrigem = self.url.find('=') + 1
        indiceFinalMoedaOrigem = self.url.find('&')'''
        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find('&')
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == 'moedadestino':
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find('&')
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        '''indiceInicialMoedaDestino = self.url.find('=', 15) + 1 # ponto de partida, posição 15'''
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find('&valor')
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace('moedadestino', 'real', 1)

    def extraiValor(self):
        buscaValor = 'valor='
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
