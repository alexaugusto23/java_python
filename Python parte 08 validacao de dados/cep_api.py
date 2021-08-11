import requests

requisicao = requests.get('https://viacep.com.br/ws/06020194/json/')

metodos = dir(requisicao)

for met in metodos:
    print(met)
print()
print(requisicao.json())

print()
print(requisicao.text)

print()
print(type(requisicao.json()))
print(type(requisicao.text))





