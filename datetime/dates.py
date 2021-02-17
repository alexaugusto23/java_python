from datetime import date
from typing import MutableSequence

def data():
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

if __name__ == "__main__":
    data()