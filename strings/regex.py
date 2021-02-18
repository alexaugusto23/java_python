import re

#  expressões regulares

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalala 9543-1254 fjosdflsdhdudsh sdnfksdjsfkdsj é o meu celular"

padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"

retorno = re.search(padrao, email4)
print(retorno)
print(retorno.group())