import re 

class ExtratorURL:

    def __init__(self, url) :
        self.valida_url(url)
        self.url = self.sanitiza_url(url)
        

    def sanitiza_url(self, url):
        if type(url) == str: # __eq__
            return url.strip()
        else: return ""

    def valida_url(self, url):
        if not url:
            raise ValueError("A URL está vazia") 

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é válida.")


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
    
    def __len__ (self):
        return len(self.url)

    def __str__ (self):
        return self.url
    
    def __equals__ (self, other):
        return self.url == other.url


# url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
# extrator_url = ExtratorURL(url)
# moeda = extrator_url.get_valor_parametro("moedaOrigem")

# print(f"URL: {extrator_url}\nMOEDA: {moeda}")
# print(f"O tamanho da URL é: {len(extrator_url)} ")

# extrator_url2 = ExtratorURL(url)
# print(id(extrator_url ))
# print(id(extrator_url2 ))
# print(extrator_url.__equals__(extrator_url2))

# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
# extrator_url = ExtratorURL(url)


