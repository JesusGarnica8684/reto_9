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
```
4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).

# Algoritmos de Sorting

¿Qué son los algoritmos de ordenamiento?

Los algoritmos de ordenamiento son métodos utilizados para organizar los elementos de una lista o arreglo en un orden específico, generalmente ascendente o descendente. Son fundamentales en informática, ya que permiten estructurar datos de manera eficiente para su procesamiento y análisis.

Tipos de algoritmos de ordenamiento

Los algoritmos de ordenamiento se pueden clasificar en diferentes categorías según su funcionamiento y eficiencia.

Algoritmos de ordenamiento básicos

Estos algoritmos son simples de entender e implementar, pero no son eficientes para grandes volúmenes de datos.

- **Bubble Sort**: Compara e intercambia elementos adyacentes repetidamente hasta ordenar la lista.
- **Selection Sort**: Encuentra el elemento más pequeño y lo coloca en su posición correcta en cada iteración.
- **Insertion Sort**: Inserta cada elemento en su posición correcta dentro de una lista parcialmente ordenada.

Algoritmos eficientes

Estos algoritmos tienen mejor rendimiento y son adecuados para manejar grandes conjuntos de datos.

- **Merge Sort**: Aplica la estrategia de "divide y vencerás", dividiendo la lista en mitades, ordenándolas por separado y luego fusionándolas.
- **Quick Sort**: Selecciona un elemento como pivote y divide la lista en dos subconjuntos, ordenando cada uno de manera recursiva.
- **Heap Sort**: Utiliza una estructura de datos llamada "montículo" o "heap" para organizar y extraer los elementos en orden.

Algoritmos de ordenamiento lineal

Algunos algoritmos pueden alcanzar un tiempo de ejecución de \(O(n)\) en casos específicos, aunque suelen requerir condiciones especiales.

- **Counting Sort**: Ordena contando la frecuencia de los valores dentro de un rango limitado.
- **Radix Sort**: Ordena los números procesando sus dígitos de menor a mayor.
- **Bucket Sort**: Distribuye los elementos en diferentes grupos o "cubetas" y luego ordena cada una individualmente.

Importancia del ordenamiento

El ordenamiento es una operación esencial en programación y ciencia de datos. Su correcta aplicación permite:

- Mejorar la eficiencia de búsquedas, como en la **búsqueda binaria**.
- Optimizar el almacenamiento y acceso a datos en bases de datos.
- Facilitar la organización de información en estructuras como listas, colas y árboles.
- Servir de base para algoritmos avanzados en inteligencia artificial, optimización y computación científica.

La elección del algoritmo de ordenamiento adecuado depende del tamaño de los datos, la disponibilidad de memoria y la necesidad de estabilidad en la ordenación.

### Bubble Sort

¿Qué es Bubble Sort?  

Bubble Sort es un algoritmo de ordenamiento que compara e intercambia elementos adyacentes hasta que la lista esté completamente ordenada. Su nombre proviene del hecho de que los valores más grandes "suben" gradualmente a su posición correcta, como burbujas en el agua.  

Si bien es fácil de implementar y comprender, es ineficiente para grandes volúmenes de datos. Por esta razón, se usa principalmente con fines educativos para ilustrar los conceptos de ordenamiento.  

¿Cómo funciona Bubble Sort?  

* Pasos del Algoritmo:  
**Recorrer el arreglo**, comparando los elementos adyacentes.  
**Intercambiar los elementos** si están en el orden incorrecto (el mayor antes del menor).  
**Repetir el proceso** hasta que no haya más intercambios en una pasada.  
**Después de cada pasada**, el elemento más grande de los no ordenados se posiciona correctamente.  
**Repetir el proceso `n-1` veces**, donde `n` es el número de elementos en la lista.  

Este método garantiza que, tras `k` pasadas, los `k` elementos más grandes estarán en sus posiciones finales.  

