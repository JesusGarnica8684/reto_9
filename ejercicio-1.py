# Desarrollar un algoritmo que calcule el promedio de un arreglo de reales

def calcular_promedio(lista):
    suma = sum(lista) #suma de los elementos
    nelem = len(lista) #se guarda la cantidad de elementos de la lista
    prom = suma / nelem #promedio
    return prom

if __name__=="__main__":
    reales = []
    n = int(input("Ingrese la cantidad de elementos de la lista: "))
    for i in range(n):
        elem = int(input(f"Ingrese el elemento {i + 1}: "))
        reales.append(elem)
    promedio = calcular_promedio(reales)
    print(f"El promedio de los elementos de la lista es: {promedio}")