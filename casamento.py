pilha = []
abertura_valida   = ['(', '[', '{']
fechamento_valido = [')', ']', '}']

def main(entrada):
    print(entrada)
    percorrer_pilha()
    #verifica(entrada)

def trata_entrada(entrada):
    nova_entrada = ""
    for it in entrada:
        if it != ' ':
            nova_entrada = it
            pilha.append(it)
    return nova_entrada

def percorrer_pilha():
    while (len(pilha) != 0):
        print(pilha.pop())

#def verifica(entrada):
#    for it in entrada_abertura:


main(trata_entrada(input()))
# S->SS/(S)/[S]/{S}/()/[]/{}