pilha = []
abertura_valida   = ['(', '[', '{']
fechamento_valido = [')', ']', '}']

def main(entrada):
    x = trata_entrada(entrada)
    print(x)
    percorrer_pilha()

#remove todos os espaços da entrada
def trata_entrada(entrada):
    nova_entrada = ""
    for it in entrada:
        if it != ' ':
            nova_entrada += it
    #passa por parâmetro a nova palavra sem os ' '.
    return verifica(nova_entrada)

#recebe palavra sem ' '
def verifica(nova_entrada):
    for it in nova_entrada:
        #verifica se o elemento 0 da entrada informada é um ')', ']' ou '}'.
        #caso seja, False.
        if it[0] in fechamento_valido:
            return False




def percorrer_pilha():
    while (len(pilha) != 0):
        print(pilha.pop())


main(input(""))
# S->SS/(S)/[S]/{S}/()/[]/{}