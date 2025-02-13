# Reto 9

1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
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
```
2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.
```python
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

```
3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
```
4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).
