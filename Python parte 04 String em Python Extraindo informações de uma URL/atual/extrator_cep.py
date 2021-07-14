import re # Regular Expression ou Espressões Regulares -- RegEx

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

#5 dígitos + hífen (opicional) + 3 dígitos

# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# Quando usar [] o padrão deve entre o intervalo dos caracteres passados.
# Quando usar () o padrão deve ser igual a string passada ex ("http")
# {5} quantidade de repetição.
# {0,1} pode ir de nehum há apenas uma repetição do caracter.
# [0-9] simplificação do padrão.
# ? diz se é opcional o padrão de busca daquel caracter exemplo: [-]? 
# Documentação https://docs.python.org/pt-br/3/howto/regex.html#regex-howto
 
padrao = re.compile("[0-9]{5}}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)

cpf = "Rafaela Brasil, CPF: 718.457.190-85"
padrao = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}")
busca = padrao.search(cpf) #Match
if busca:
    cpf_found = busca.group()
    print(cpf_found)


