import sys
import os

if sys.version_info.major == 2:
    print(sys.version_info.major)
    usuario = raw_input('Insira seu login: ')
elif sys.version_info.major == 3:
    print(sys.version_info.major)
    usuario = input('Insira seu login: ')

# Executa a string como código python.
# Executa a string como expressão.
print(eval("os.system('dir')"))