class EstratorURL:

    def __init__(self, url) :
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else: return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia") 

    def get_url_base(self):
        ind_interrogacao = self.url.find('?')
        url_base = self.url[0:ind_interrogacao]
        return url_base

    def get_url_parametros(self):
        ind_interrogacao = self.url.find('?')
        url_parametros = self.url[ind_interrogacao + 1: ]
        return url_parametros
    
    def get_valor_parametro(self, parametro_de_busca):
        indice_de_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_de_valor = indice_de_parametro + len(parametro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_de_valor)
        valor = self.get_url_parametros()[indice_de_valor:indice_e_comercial]

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_de_valor:]
        else:
            valor = self.get_url_parametros()[indice_de_valor:indice_e_comercial]
        return valor



url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
extrator_url = EstratorURL(None)
moeda = extrator_url.get_valor_parametro("moedaOrigem")

print(f"URL: {extrator_url.url}\nMOEDA: {moeda}")