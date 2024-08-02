# Método que busca os valores na lista.
def Pesquisar(vetor_a, valor):
    posicao = 0
    for contador in range(len(vetor_a)):
        if vetor_a[contador] == valor:
            posicao = contador
            break
        else:
            pass
    
    if posicao != "":
        print(f"O número {valor} já existe no vetor. Ele está na {posicao+1}º posição.")
        print("Tente novamente.")
        print("")
        Completar_Valor()   
    elif posicao == "":     
        print(f"O valor {valor} não foi encontrado no vetor.")
        print("")
        Completar_Valor()



def Completar_Valor():
    vetor_a = [9, 7, 2, 16, 14, 32]

    valor = int(input("Digite um valor para buscar no vetor: "))

    Pesquisar(vetor_a, valor)


# Método principal.
def Main():
    print("")
    Completar_Valor()


Main()