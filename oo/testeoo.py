def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite,}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta = cria_conta(1,"Alex",0.00,400.00)

extrato(conta)
deposita(conta,15)
extrato(conta)
saca(conta,2)
extrato(conta)

for i in conta:
    print("Chave",i, "Valor", conta[i])
print(conta)