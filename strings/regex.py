import re

#  expressões regulares

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalala 9543-1254 fjosdflsdhdudsh sdnfksdjsfkdsj é o meu celular"

padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"

retorno = re.search(padrao, email4)
print(retorno)
print(retorno.group())

cpf = "o meu cpf é: 36059729955 nwqklndlawknlk"
cpf2 = "o meu cpf é: 36059729955 nwqklndlawknlk 33859729900 kjjsdjhvdsjhdfs 338597397-01"
cpf_padrao = "[0-9]{9}[-]*[0-9]{2}" # {0,1} pode ser substituído por: asterisco *   

retorno2 = re.search(cpf_padrao, cpf)
print(retorno2)
print(retorno2.group())

retorno3 = re.findall(cpf_padrao, cpf2)
print(retorno3)
