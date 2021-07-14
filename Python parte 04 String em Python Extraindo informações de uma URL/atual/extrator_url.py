class EstratorURL:

    def __init__(self, url) :
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.url == None:
            raise ValueError("A URL é None") 
        elif self.url == "":
            raise ValueError("A URL está vazia") 

    def get_url_base(self):
        pass

    def get_url_parametros(self):
        pass




extrator_url = EstratorURL(" asd  ")
print(extrator_url)