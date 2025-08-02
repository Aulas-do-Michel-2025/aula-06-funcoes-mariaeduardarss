"""
Exercício 2 - Criando um dicionário

Escreva uma função com o nome `criar_organismo` que recebe 3 argumentos: id, nome, tamanho_do_genoma e retorna um
dicionário contendo esses três campos (com as chaves "id", "nome" e "tamanho_do_genoma").

Exemplo de uso:
>>> print(criar_organismo(10, 'HIV', 1000))
>>> {"id": 10, "nome": "HIV", 1000}
"""

def criar_organismo(id, nome, tamanho_do_genoma):
    return {
        "id": id,
        "nome": nome,
        "tamanho_do_genoma": tamanho_do_genoma
    }

def interativo():
    print("Vamos criar um organismo!")
    try:
        id = int(input("Digite o ID do organismo (número inteiro): "))
        nome = input("Digite o nome do organismo: ")
        tamanho_do_genoma = int(input("Digite o tamanho do genoma (número inteiro): "))
    except ValueError:
        print("Erro: ID e tamanho do genoma devem ser números inteiros.")
        return

    organismo = criar_organismo(id, nome, tamanho_do_genoma)
    print("\nOrganismo criado:")
    print(organismo)

if __name__ == "__main__":
    interativo()
