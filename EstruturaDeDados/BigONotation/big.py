'''
Big O Notation descreve o comportamento de tempo ou espaço de um algoritmo em função do tamanho da entrada (geralmente representado por n).
Serve para medir a complexidade de algoritmos quanto ao pior caso (worst-case), tempo de execução e uso de memória.

- fala sobre escabilidade, e não necessariamente performace


            Categorias mais comuns de Big O:

| Notação   | Nome técnico   |       Descrição resumida

O(1)	       Constante	      Independente do tamanho do input tem o mesmo tempo de execução
O(log n)	   Logarítmica	      Cresce lentamente à medida que n aumenta
O(n)	         Linear	          Cresce proporcionalmente a n
O(n log n)	   Linearítmica	      Usado em algoritmos de ordenação eficientes
O(n²)	        Quadrática	      Cresce rapidamente — dupla iteração
O(2ⁿ)	        Exponencial	      Cresce extremamente rápido
O(n!)	         Fatorial	      Usado em permutações — extremamente ineficiente

Exemplos práticos em Python:

1. O(1) – Complexidade constante

def get_first_element(arr):
    return arr[0]  # Sempre 1 operação

    
2. O(n) – Complexidade linear

def print_all_elements(arr):
    for element in arr:
        print(element)  # Executa n vezes


3. O(n²) – Complexidade quadrática

def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Executa n * n vezes



4. O(log n) – Complexidade logarítmica (Ex: busca binária)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


5. O(n log n) – Merge Sort (ordenação eficiente)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    

    # Combina os arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

'''