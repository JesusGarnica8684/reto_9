def mover_ceros(lista):
    # Índice para guardar los elementos no ceros
    inotnull = 0
    # se repasa la lista y cuando se encuentra un elemento no cero se guarda en inotnull
    for i in range(len(lista)):
        if lista[i] != 0:
            lista[inotnull] = lista[i] # se mueven los elementos no cero a las primeras posiciones
            inotnull += 1
    # se rellena el resto del arreglo con ceros
    for i in range(inotnull, len(lista)):
        lista[i] = 0
    return lista

if __name__=="__main__":
    listaPrueba = [1, 0, 2, 0, 3, 4, 0, 5]
    print(f"Lista original: {listaPrueba}")
    listaOrdenada = mover_ceros(listaPrueba)
    print(f"Lista con ceros al final: {listaOrdenada}")