import locale
from decimal import Decimal

def converte_real_para_euro(valor_em_real):
    ## implementação da conversão
    valor = str(valor_em_real)
    valor_em_real = Decimal(valor)
    valor_em_euro = valor_em_real * Decimal('6.5149')	
    return valor_em_euro

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')#pt-BR
valor_inicial_em_real = 1.0
valor_convertido_em_euro_inicial = converte_real_para_euro(valor_inicial_em_real)
valor_arredondado_em_euro = round(valor_convertido_em_euro_inicial, 2)
valor_em_euro_texto = str(valor_arredondado_em_euro).replace('.', ',')
valor_em_dolar_formatado = locale.currency(valor_convertido_em_euro_inicial, grouping=True)

print(f'{valor_convertido_em_euro_inicial}\n{valor_arredondado_em_euro}\n{valor_em_euro_texto}\n{valor_em_dolar_formatado}')


