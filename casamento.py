pilha = []
abertura_valida   = ['(', '[', '{']
fechamento_valido = [')', ']', '}']
dados_validos     = ['(', ')', '[', ']', '{', '}']

def main(entrada):
    try:
        x = entrada
        #recebe nova_entrada
        nova_palavra = (trata_entrada(x))
        print(verifica(nova_palavra))
    except Exception:
        print(True)



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
                #'it' faz parte da lista 'abertura_valida'?
                if it in abertura_valida:
                    for k in abertura_valida:
                        #obtém qual dos 3 símbolos 'it' corresponde
                        if it == k:
                            #insere na pilha o símbolo oposto a 'it'
                            pilha.append(fechamento_valido[aux])
                        else:
                            aux += 1
                else:
                    # 'it' faz parte da lista 'fechamento_valido'?
                    if it in fechamento_valido:
                        #compara se 'it' tem o seu correspondente no topo da pilha
                        if it == pilha.pop():
                            return True
                        else:
                            return False

#def percorrer_entrada(nova_entrada):


main(input(""))
# S->SS/(S)/[S]/{S}/()/[]/{}