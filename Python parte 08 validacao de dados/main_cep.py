from acesso_cep import BuscaEndereco

cep = "06020194"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
viacep = objeto_cep.acessa_via_cep(formato="text")
print(viacep)

viacep = objeto_cep.acessa_via_cep_fotmat_data()
print(viacep)