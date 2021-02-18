class ExtratoArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url 
        else: raise LookupError("URL Invalída!!!")

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False
    
    def extrai_argumentos(self):
        indice__inicial_moeda_origem = self.url.find("=") + 1  
        indice_final_moeda_origem = self.url.find("&")
        
        indice__inicial_moeda_destino = self.url.find("=", 55) + 1 
        indice_final_moeda_destino = self.url.find("&",55)

        moeda_origem = self.url[indice__inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice__inicial_moeda_destino:indice_final_moeda_destino]
        return moeda_origem, moeda_destino
           