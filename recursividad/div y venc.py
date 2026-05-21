def sumar_lista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + sumar_lista(lista[1:])


print(sumar_lista([1, 2, 3, 4]))