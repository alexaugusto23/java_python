class Cpf:
    def __init__(self, documento):
        documento = str(documento) 
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!!")

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
    
    def formata_cpf(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"

    def __str__(self):
        return self.formata_cpf()