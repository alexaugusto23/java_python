from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento: str = "", tipo_documento: str = "", lista_doc: list = None ) -> str:
        
        if documento == "" and tipo_documento == "" and lista_doc != None:
            try:
                self.tipo_documento = lista_doc[1]
                documento = lista_doc[0]
            except IndexError:
                raise ValueError("Sem Argumentos")

        elif documento == "" and tipo_documento == "" and lista_doc == None or lista_doc == "":
            raise ValueError("Sem Argumentos")
        else:
            self.tipo_documento = tipo_documento
            documento = str(documento)
        
        if self.tipo_documento.lower() == "cpf":       
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido!!!")
        elif self.tipo_documento.lower() == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!!!")
        else:
            raise ValueError("Tipo não existe")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos do CPF invalido")

    
    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos do CNPJ invalido")


    def formata_cpf(self):
        #return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        mascara = CPF()
        return mascara.mask(self.cpf)
        
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self):
        if self.tipo_documento.lower() == "cpf": 
            return self.formata_cpf()
        elif self.tipo_documento.lower() == "cnpj":
            return self.formata_cnpj()
