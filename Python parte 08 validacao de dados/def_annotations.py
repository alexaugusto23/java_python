# Anotações de funções:

def func(a: int, b: str) -> int : 
    return a + b

print(func(5,6))

def func(a, b: str) -> int : 
    return a + b

print(func(5,6))

def func(a: list, b: str, c: tuple) -> dict : 
    return a + b + c

print(func(5, 6, 5))