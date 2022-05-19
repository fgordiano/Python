def remove_repetidos (lista):
    lista.sort()
    lista2 = []
    for item in lista:
        if (item in lista2)==False:
            lista2.append(item)
    return lista2




lista = [0,2,2,5,2,1,1,7,8,6,6,8,7,0,100]
lista2=[]
lista2 = remove_repetidos(lista)
print(lista2)


