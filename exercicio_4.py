"""
Exercicio 4 - Usando funcoes

Você vai escrever uma funcao que recebe uma lista com números e deve retornar uma outra lista
só com os números primos.

Mas você não precisa escrever a lógica para saber se o número é primo: você pode só usar a funcão
`verificar_se_eh_primo` disponibilizada, que vai retornar True se o número for primo e False se não for.
"""


def verificar_se_eh_primo(numero):
    if numero > 1:
        for i in range(2, int(numero / 2) + 1):
            if (numero % i) == 0:
                return False
        return True
    return False

def filtrar_lista_por_numeros_primos(lista):
    lista_filtrada = []
    for numero in lista:
        if verificar_se_eh_primo(numero):
            lista_filtrada.append(numero)
    return lista_filtrada
