from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento) 
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!!")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos do CPF invalido")

    
    def formata_cpf(self):
        #return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def __str__(self):
        return self.formata_cpf()