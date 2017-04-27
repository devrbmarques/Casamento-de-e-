pilha = []
abertura_valida   = ['(', '[', '{']
fechamento_valido = [')', ']', '}']
dados_validos     = ['(', ')', '[', ']', '{', '}']

def main(entrada):
    x = entrada
    #recebe nova_entrada
    nova_palavra = (trata_entrada(x))
    k = verifica(nova_palavra)
    if k == False:
        print(k)

    percorrer_pilha()









#remove todos os espaços da entrada
def trata_entrada(entrada):
    nova_entrada = ""
    for it in entrada:
        if it != ' ':
            nova_entrada += it
    #passa por parâmetro a nova palavra sem os espaços.
    return nova_entrada

#recebe palavra sem espaços
def verifica(nova_entrada):
    #verifica se o elemento x[0] da entrada informada é um ')', ']' ou '}'.
    #caso seja, False.
    if nova_entrada[0] in fechamento_valido:
        print(nova_entrada[0])
        return False
    else:
        #verifica se há qualquer caractere diferente do aceitado no problema
        for it in nova_entrada:
            # verifica a ausênica do elemento na lista 'dados_validos'
            # se ausente, retorna False
            if not it in dados_validos:
                return False
            #palavra valida com os elementos válidos
            else:
                k   = 0
                aux = 0
                for k in abertura_valida:
                    if it == k:
                        pilha.append(fechamento_valido[aux])
                    else:
                        aux += 1



#def percorrer_entrada(nova_entrada):

def percorrer_pilha():
    while (len(pilha) != 0):
        print(pilha.pop())


main(input(""))
# S->SS/(S)/[S]/{S}/()/[]/{}