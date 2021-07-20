from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento):
        documento = str(documento) 
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!!")

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos do CNPJ invalido")

    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self):
        return self.formata_cnpj()