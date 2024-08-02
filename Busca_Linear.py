# Método que busca os valores na lista.
def Pesquisar(vet, n):
    tamanho_vet = len(vet)
    posicao = -1

    for contador in range(0, tamanho_vet):
        if vet[contador] == n:
            posicao = contador
            break
    
    if posicao != -1:
        print(f"O número {n} existe no vetor. Ele está na {posicao+1}º posição.")   
    else:     
        print(f"O valor {n} não foi encontrado no vetor.")
        print("Tente novamente.")

    Main()


# Método de entrada do valor a ser buscado
def Completar_Valor():
    vet = [9, 7, 2, 16, 14, 32]
    n = int(input("Digite um valor para buscar no vetor: "))
    Pesquisar(vet, n)


# Método principal.
def Main():
    print("")
    Completar_Valor()


Main()