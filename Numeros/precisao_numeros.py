from decimal import Decimal

ganhos_julho = 99.91 * 5
gastos_julho = 110.1 * 3

armazena_no_banco = (ganhos_julho, gastos_julho)
val_a = 99.91
val_b = 110.1


ganhos_julho_dec = Decimal(str(val_a)) * 5
gastos_julho_dec = Decimal(str(val_b)) * 3

armazena_no_banco_dec = (ganhos_julho_dec, gastos_julho_dec)


print(armazena_no_banco)
print(armazena_no_banco_dec[0])
print(armazena_no_banco_dec[1])
print(type(armazena_no_banco_dec[0]))
print(type(armazena_no_banco_dec[1]))
