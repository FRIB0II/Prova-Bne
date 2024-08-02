# Método que ordena a lista em ordem decrescente.
def Bubble_Sort_Reverse(lista_a):
    mudou = 1

    while mudou > 0:
        mudou = 0
        for contador in range(0, len(lista_a)-1):
            if lista_a[contador] < lista_a[contador+1]:
                lista_a[contador], lista_a[contador+1] = lista_a[contador+1], lista_a[contador]
                mudou +=1

    print("")
    print("Lista em ordem decrescente: ")
    print(lista_a)
    print("")


# Método que ordena a lista em ordem crescente.
def Bubble_Sort(lista_a):
    mudou = 1

    while mudou > 0:
        mudou = 0
        for contador in range(0, len(lista_a)-1):
            if lista_a[contador] > lista_a[contador+1]:
                lista_a[contador], lista_a[contador+1] = lista_a[contador+1], lista_a[contador]
                mudou +=1

    print("")
    print("Lista em ordem crescente: ")
    print(lista_a)

    Bubble_Sort_Reverse(lista_a)


# Método para colocar os dados na lista.
def Preencher_Lista():
    lista_a = []
    nome_usuario = str(input("Digite seu nome: "))
    tamanho_nome_usario = len(nome_usuario)
    print("")

    for iterador in range(tamanho_nome_usario):
        numero = int(input("Digite um número: "))
        lista_a.append(numero)

    Bubble_Sort(lista_a)

# Método principal.
def Main():
    print("")
    Preencher_Lista()

Main()