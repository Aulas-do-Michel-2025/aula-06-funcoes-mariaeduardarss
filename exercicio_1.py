"""
Exercício 1 - Escrevendo uma função.

Escreva uma função com o nome `verificar_nota` que recebe um nota e diz se o aluno foi aprovado, ficou de recuperação ou foi reprovado.

Se a nota foi > 5 -> retorne "Aprovado".
Se a nota foi entre 3 e 5 -> retorne "Recuperação".
Se a nota for < 3 -> retorne "Reprovado".

Obs: Escreva necessariamente uma função que retorne (não só imprima) esses valores. De exatamente o nome de `verificar_nota` porque
o teste vai procurar uma função com esse nome.
"""

def verificar_nota(nota):
    if nota > 5:
        return "Aprovado"
    elif 3 <= nota <= 5:
        return "Recuperação"
    else:
        return "Reprovado"
