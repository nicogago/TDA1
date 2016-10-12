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


# Función debe aceptar (conj, k_buscada), devuelve en ms
def medir_elapsed_time(func, conj, k, runs=100):
    wrapped = wrapper(func, conj, k)
    # Corre 100 veces y promedia
    elapsed = timeit.timeit(wrapped, number=runs)
    res = 10**3 * elapsed / runs
    return res


def imprimir_tiempos_y_promedio(func, lists, ks):
    print func.__name__
    sum = 0
    for i, a_list in enumerate(lists):
        t = medir_elapsed_time(func, a_list, ks[i])
        print 'Conj %d: %.3f ms' % (i, t)
        sum += t
    promedio = sum / (i + 1)
    print 'Tiempo promedio: %.3f ms' % (promedio)
    print
    return promedio

def imprimir_tiempo_promedio(func, lists, ks):
    sum = 0
    # Corre para cada list en lists y promedia
    for i, a_list in enumerate(lists):
        sum += medir_elapsed_time(func, a_list, ks[i], 5)
    promedio = sum / (i + 1)
    print 'N=%d\t%.3f ms\t(total: %.6f s)' % (len(lists[0]), promedio, sum/1000)
    return promedio


print
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
print
print

f = open('resultados', 'w')
f.write('N\tTiempo promedio [ms]\n\n')

print "Se corren con conjuntos cuyo tamaño crece exponencialmente"
print
for func in funciones:
    print func.__name__
    f.write('%r\n' % (func.__name__))
    for exp in xrange(0, 5):
        n = 10**exp
        lists = random_lists(n, 5)
        ks = np.random.randint(1, n+1, size=5)
        res = imprimir_tiempo_promedio(func, lists, ks)
        f.write('%d\t%.4f\n' % (n, res))
    print
    f.write('\n')

f.close()
