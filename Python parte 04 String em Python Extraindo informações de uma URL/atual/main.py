
from extrator_de_url import ExtratorURL 
from conversor_de_moeda import conv_dolar_real, conv_real_dolar

url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
extrator_url = ExtratorURL(url)

tx_real = 0.1968503937007874
tx_dolar = 5.08  
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem.lower() == 'real' and moeda_destino.lower() == 'dolar':
    valor =  conv_real_dolar(quantidade, tx_dolar)
    print(f"{round(valor, 2)}")
elif moeda_origem.lower() == 'dolar' and moeda_destino.lower() == 'real':
    valor =  conv_dolar_real(quantidade, tx_real)
    print(f"{round(valor, 2)}")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")

