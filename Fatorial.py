# Método que calcula o fatorial.
def Calcula_Fatorial(fatorial):
    contador = 1
    resultado_fatorial = 1
    while contador <= fatorial:
        resultado_fatorial = resultado_fatorial * contador 
        contador += 1
    return resultado_fatorial


# Método que calcula o FAT.
def Calcula_FAT():
    dividendo = 224
    fatorial = 2
    contador = 1
    fat = 0

    print("FAT =", end=" ")    

    while contador < 10:
        if fatorial == 10:
            print(f"({dividendo} / {fatorial}!)")
            break

        resultado = Calcula_Fatorial(fatorial)
        fat = fat + (dividendo / resultado)

        print(f"({dividendo} / {fatorial}!)", end=" + ")

        fatorial += 1
        dividendo += 4
        contador += 1

    print("")
    print(f"A soma FAT é {round(fat, 2)}. E o termo faltante é {dividendo}.")
    print("")


# Método principal.
def Main():
    print("")
    Calcula_FAT()


Main()