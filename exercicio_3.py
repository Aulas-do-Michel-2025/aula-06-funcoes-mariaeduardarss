"""
Exercício 3 - Calculando a média de uma lista

Escreva uma funcao chamada `calcular_media` (sem acento) que recebe uma lista com numeros
e retorne a média dos valores dela.

Exemplo de uso:
>>> print(calcular_media([0, 100, 200]))
>>> 100
"""

def calcular_media(lista):
    if len(lista) == 0:
        return 0 
    return sum(lista) / len(lista)

numeros = input("Digite os números separados por vírgula: ")
lista_numeros = [float(num.strip()) for num in numeros.split(",")]
media = calcular_media(lista_numeros)

print(f"A média dos valores é: {media}")
