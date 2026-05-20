def propagar(L):
    resultado = L[:]

    fuego = False
    for i in range(len(resultado)):
        if resultado[i] == 1:
            fuego = True
        elif resultado[i] == -1:
            fuego = False
        elif resultado[i] == 0 and fuego:
            resultado[i] = 1

    fuego = False
    for i in range(len(resultado) - 1, -1, -1):
        if resultado[i] == 1:
            fuego = True
        elif resultado[i] == -1:
            fuego = False
        elif resultado[i] == 0 and fuego:
            resultado[i] = 1

    return resultado

print(propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]))

print(propagar([0, 0, 0, 1, 0, 0]))
