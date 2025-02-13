# Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) 
# de igual tamaño.
def producto_punto(l1, l2):
    # Calcular el producto punto
    pescalar = 0
    for i in range(len(l1)):
        pescalar += l1[i] * l2[i] #el producto punto es la suma de los productos de sus correspondientes coordenadas
    return pescalar

if __name__=="__main__":
    listA = []
    listB = []
    n = int(input("Ingrese la cantidad de componentes del vector: ")) #se asegura que los dos vectores tengan el mismo tamaño

    for i in range(n):
        elemA = int(input(f"Ingrese el componente del vector 1-{i + 1}: "))
        listA.append(elemA)
        elemB = int(input(f"Ingrese el componente del vector 2-{i + 1}: "))
        listB.append(elemB)
    escalar = producto_punto(listA, listB)
    print(f"El producto punto de los arreglos es: {escalar}")
