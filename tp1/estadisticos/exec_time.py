#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import timeit
import numpy as np
from estadisticos import *

## Funciones a medir
funciones = [k_fuerza_bruta, ordenar_y_seleccionar, k_selecciones, \
            k_heapsort, heapselect, k_quickselect]


def random_list(n):
    return random_lists(n, 1)

def random_lists(n, cant):
    return np.random.randint(0, 100, size=(cant, n))

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


# Función debe aceptar (conj, k_buscada)
def medir_elapsed_time(func, conj, k):
    wrapped = wrapper(func, conj, k)

    # Corre 100 veces y promedia
    elapsed = timeit.timeit(wrapped, number=100)
    res = 10**6 * elapsed / 100

    return res

def imprimir_tiempos_y_promedio(func, lists, ks):
    print func.__name__
    sum = 0
    for i, a_list in enumerate(lists):
        t = medir_elapsed_time(func, a_list, ks[i])
        print 'Conj %d: %.1f ms' % (i, t)
        sum += t
    promedio = sum / (i + 1)
    print 'Tiempo promedio: %.1f ms' % (promedio)
    print
    return promedio


print "Se miden los tiempos de ejecución para obtener"
print "el estadístico de orden k con distintos algoritmos"
print

lists = random_lists(16, 5)
ks = np.random.randint(1, 17, size=5)
print "Conjuntos rándom de 16 int y k rándom para buscarles:"
for i, a_list in enumerate(lists):
    print "Conjunto", (i+1), ":", a_list, "con k =", ks[i]
print

for func in funciones:
    imprimir_tiempos_y_promedio(func, lists, ks)
