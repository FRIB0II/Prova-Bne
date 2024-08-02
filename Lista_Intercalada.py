# Método que calcula a média dos valores do vetor C.
def Media_Vetor_Intercalado(vetor_c):
    soma = 0
    tamanho_vetor_c = len(vetor_c)

    for numero in vetor_c:
        soma += numero
    
    media = soma / tamanho_vetor_c

    print(f"A média do vetor c é: {media}.")
    print("")


# Método que intercala os valores de A e B em C.
def Vetor_Intercalado(vetor_a, vetor_b):
    vetor_c = []

    for contador in range(0, 5):
        vetor_c.append(vetor_a[contador])
        vetor_c.append(vetor_b[contador])

    print("Vetor C")
    print(vetor_c)

    print("")

    Media_Vetor_Intercalado(vetor_c)


# Método de preenchimento dos vetores A e B.
def Preencher_Vetores():
    vetor_a = []
    vetor_b = []

    print("Vetor A")
    for contador in range(1, 6):
        numero_a = int(input(f"Digite o valor {contador}: "))
        vetor_a.append(numero_a)

    print("")
    print("Vetor B")
    for contador in range(1, 6):
        numero_b = int(input(f"Digite o valor {contador}: "))
        vetor_b.append(numero_b)

    print("")
    print(vetor_a)
    print(vetor_b)
    print("")

    Vetor_Intercalado(vetor_a, vetor_b)


# Método principal.
def Main ():
    print("")
    Preencher_Vetores()


Main()