from datetime import date
from typing import MutableSequence

def mod_date():
    data_atual = date.today()
    dia = data_atual.day 
    mes = data_atual.month
    ano = data_atual.year
    format = None
    print(dia < 10)
    if dia  < 10: d = 0
    else: d = ''
    if mes  < 10: m = 0
    else: m = ''
    print(data_atual)
    print('{}{}/{}{}/{}'.format(d,dia,m,mes,ano))
    #or strftime para formatar sem a necessidade de ifs.
    print('strftime:')
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    print(data_em_texto)

if __name__ == "__main__":
    mod_date()