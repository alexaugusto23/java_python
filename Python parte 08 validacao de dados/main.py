from cpf_cnpj_refatorado import Documento

cpf = "36054729852"
cnpj = "35379838000112"

validador = Documento.cria_documento(cpf)
print(validador)