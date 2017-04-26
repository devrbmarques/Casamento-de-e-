pilha = []
abertura_valida   = ['(', '[', '{']
fechamento_valido = [')', ']', '}']

def main(entrada):
    percorrer_pilha()

#remove todos os espaços da entrada
def trata_entrada(entrada):
    nova_entrada = ""
    for it in entrada:
        if it != ' ':
            nova_entrada = it
    verifica(nova_entrada)

#recebe palavra sem espaços
def verifica(nova_entrada):
    for it in nova_entrada:
        while abertura_valida <= abertura_valida[3]:
            if it == abertura_valida:
                print(it)
            else:
                print("Erro")

def percorrer_pilha():
    while (len(pilha) != 0):
        print(pilha.pop())


main(trata_entrada(input("")))
# S->SS/(S)/[S]/{S}/()/[]/{}