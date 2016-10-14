#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                          ###
###  ESTADISTICO DE ORDEN K  ###
###                          ###


# En ambas formas, cand es el indice en conj del numero candidato
# Asumiendo minimo k cuando hay repetidos
def fuerza_bruta_min_k(conj, cand, k):
    real_k = 1
    for i in conj:
        if (i < conj[cand]):
            real_k += 1
            if (real_k > k):
                return False
    if (real_k < k):
        return False
    return True

# Sin esa restriccion
def fuerza_bruta(conj, cand, k):
    min_real_k = 1
    diff_max_k = 0

    for idx, i in enumerate(conj):
        if (i < conj[cand]):
            min_real_k += 1
            if (min_real_k > k):
                return False
        elif (i == conj[cand] and idx != cand):
            diff_max_k += 1
    if (min_real_k + diff_max_k < k):
        return False
    return True

# Devuelve el estadístico orden-k como el resto de las funciones
def k_fuerza_bruta(conj, k):
    for idx_cand, cand in enumerate(conj):
        if fuerza_bruta(conj, idx_cand, k):
            return cand


# Usa el sort de Python
def ordenar_y_seleccionar(conj, k):
    conj.sort()
    return conj[k-1]


## K SELECCIONES
# k > 0
def k_selecciones(conj, k):
    for i in range(0, k):
        min = i
        for j in range(i+1,len(conj)):
            if conj[j] < conj[min]:
                min = j
        if i != min:
            conj[i] , conj[min] = conj[min] , conj[i]
    return conj[k-1]


# Para min-heapificar
def moveDownMin(conj, actual, last):
    hijo = 2 * actual + 1
    while (hijo <= last):
        if (hijo < last and conj[hijo] > conj[hijo + 1]):
            hijo += 1
        if (conj[actual] > conj[hijo]):
            conj[actual], conj[hijo] = conj[hijo], conj[actual]
            actual = hijo
            hijo = 2 * actual + 1
        else:
            return

def k_heapsort(conj, k):
    last = len(conj)
    for i in xrange(1, k+1):
        last -= 1
        # min-heapifico
        for j in xrange(last // 2, -1, -1):
            moveDownMin(conj, j, last)
        if i != k:
            conj[0], conj[last] = conj[last], conj[0]
    return conj[0]


# Para max-heapificar
def moveDownMax(conj, actual, last):
    hijo = 2 * actual + 1
    while (hijo <= last):
        if (hijo < last and conj[hijo] < conj[hijo + 1]):
            hijo += 1
        if (conj[actual] < conj[hijo]):
            conj[actual], conj[hijo] = conj[hijo], conj[actual]
            actual = hijo
            hijo = 2 * actual + 1
        else:
            return

# Para heap de máximo
def siftUpMax(conj, idx_actual):
    if idx_actual == 0:
        return
    idx_padre = idx_actual // 2
    if conj[idx_actual] > conj[idx_padre]:
        conj[idx_padre], conj[idx_actual] = conj[idx_actual], conj[idx_padre]
        siftUpMax(conj, idx_padre)

def heapselect(conj, k):
    maxHeap = []
    for idx, i in enumerate(conj):
        if (len(maxHeap) < k):
            maxHeap.append(i)
            siftUpMax(maxHeap, len(maxHeap)-1)
        elif (i < maxHeap[0]):
            maxHeap[0] = i
            moveDownMax(maxHeap, 0, len(maxHeap)-1)
    return maxHeap[0]


## QUICKSELECT
# k > 0
# Funcion para encontrar pivote para luego particionar el arreglo
def particionar(conj, ini, fin):
    i = ini - 1
    for j in range(ini, fin):
        if (conj[j] < conj[fin]):
            i += 1
            if (i != j):
                conj[i], conj[j] = conj[j], conj[i]
    # i+1 se va a convertir en el pivote (swap)
    conj[i+1], conj[fin] = conj[fin], conj[i+1]
    return i + 1

def quickselect(conj, ini, fin, k):
    k_real = k - 1
    if (ini == fin):
        return conj[k_real]
    # descartamos el subconj que no contiene al elemento k
    pivote = particionar(conj, ini, fin)
    if (k_real == pivote):
        return conj[k_real]
    if (k_real > pivote):
        ini = pivote + 1
    else:
        fin = pivote - 1
    return quickselect(conj, ini, fin, k)

# Devuelve el estadístico orden-k como el resto de las funciones
def k_quickselect(conj, k):
    return quickselect(conj, 0, len(conj)-1, k)
