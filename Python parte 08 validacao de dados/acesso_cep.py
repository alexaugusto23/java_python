import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else: 
            raise ValueError("CEP Inválido")

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:8]}"

    def __str__(self):
        return self.format_cep()

    def acessa_via_cep(self, formato):
        cep = self.cep
        formato_file = "json"
        url = f"https://viacep.com.br/ws/{cep}/{formato_file}"
        requisicao = requests.get(url)
        if formato.lower() == 'json':
            return requisicao.json()
        elif formato.lower() == 'text':
            return requisicao.text
        else:
            return 'Formato não existe'

    def acessa_via_cep_fotmat_data(self):
        cep = self.cep
        formato_file = "json"
        url = f"https://viacep.com.br/ws/{cep}/{formato_file}"
        requisicao = requests.get(url)
        dados = requisicao.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
