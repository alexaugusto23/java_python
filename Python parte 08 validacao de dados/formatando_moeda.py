import locale
# Locale = pt-BR, it-IT, en-US, en-GB
locale.setlocale(locale.LC_MONETARY, 'it-IT')

def converte_real_para_euro(valor_em_real):
    valor_em_euro = valor_em_real / 4.013044610183722
    #valor_em_euro = str(round(valor_em_euro, 2)).replace(".",",")
    #return f"{valor_em_euro} €"
    return valor_em_euro

valor_inicial_em_real = 15000.0
valor_convertido_em_euro = converte_real_para_euro(valor_inicial_em_real)

print(valor_convertido_em_euro)

valor_em_dolar_formatado = locale.currency(valor_convertido_em_euro, grouping=True)
print(valor_em_dolar_formatado)