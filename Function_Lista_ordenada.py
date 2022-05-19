def remove_repetidos (lista):
    lista.sort()
    lista2 = []
    for item in lista:
        if (item in lista2)==False:
            lista2.append(item)
    return lista2


