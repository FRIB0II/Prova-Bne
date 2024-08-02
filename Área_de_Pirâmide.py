from math import sqrt


# Método que calcula a área total da pirâmide.
def Piramide_Quadrada():
    aresta_base = 133.2
    altura_piramide = float(input("Informe a altura da pirâmide (em milímetros): "))

    area_base = ((aresta_base**2) * sqrt(3)) / 4
    area_face_piramide = (aresta_base * altura_piramide) / 2
    area_faces_totais = area_face_piramide * 4

    area_total = area_base + area_faces_totais

    print("")
    print(f"A área total dessa pirâmide é: {area_total:.2f} milímetros cúbicos.")


# Método principal.
def Main():
    print("")
    Piramide_Quadrada()


Main()