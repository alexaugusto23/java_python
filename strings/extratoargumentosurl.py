class ExtratoArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url.lower() 
        else: raise LookupError("URL Invalída!!!")

    @staticmethod
    def url_eh_valida(url):
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False
    
    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem=".lower() 
        busca_moeda_destino = "moedadestino=".lower() 

        indice_inicial_moeda_origem = self.encontra_ind_inicial(busca_moeda_origem)
        #print(f"ind inicio: {indice_inicial_moeda_origem}")
        indice_final_moeda_origem = self.encontra_ind_final("&")
        #print(f"ind final: {indice_final_moeda_origem}")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        #print(moeda_origem)
        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_ind_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.encontra_ind_final("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_ind_inicial(busca_moeda_destino) 
        indice_final_moeda_destino = self.encontra_ind_final("&",52)
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]
        
        return moeda_origem, moeda_destino
    
    def encontra_ind_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def encontra_ind_final(self, valor1 = None, valor2 = None):
        return self.url.find(valor1, valor2)
    
    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino","real", 1)
        #print(self.url)
    
    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_ind_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor