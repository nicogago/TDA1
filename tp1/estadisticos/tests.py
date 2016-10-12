#!/usr/bin/python
# -*- coding: utf-8 -*-
from estadisticos import *

### TESTS ###

## fuerza_bruta
my_list = [4, 1, 5, 9, 12, 3, 0, 2, 7, 6]
true_k  = [5, 2, 6, 9, 10, 4, 1, 3, 8, 7]
for idx, k in enumerate(true_k):
	assert fuerza_bruta_min_k(my_list, idx, k)

my_list = [1, 1, 5, 12, 12, 5, 7, 2, 7, 6]
true_k  = [1, 2, 4,  9, 10, 5, 7, 3, 8, 6]
for idx, k in enumerate(true_k):
    assert fuerza_bruta(my_list, idx, k)

my_list  = [1, 1, 5, 12, 12, 5, 7, 2, 7, 6]
sorted_l = [1, 1, 2, 5, 5, 6, 7, 7, 12, 12]
for idx, i in enumerate(sorted_l):
    assert k_fuerza_bruta(my_list, idx+1) == i

## ordenar_y_seleccionar
my_list = [1, 1, 5, 12, 12, 5, 7, 2, 7, 6]
sorted_l = my_list
sorted_l.sort()
result = []
for k in xrange(1, 11):
    result.append(ordenar_y_seleccionar(my_list, k))
assert result == sorted_l

## k_selecciones
my_list  = [4, 1, 5, 9, 12, 3, 0, 2, 7, 6]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12]
for idx in xrange(0, 8):
    assert k_selecciones(my_list, idx+1) == idx

## k_heapsort
my_list  = [4, 1, 5, 9, 12, 3, 0, 2, 7, 6]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12]
for idx, i in enumerate(sorted_l):
    assert k_heapsort(my_list, idx+1) == i

## heapselect
my_list  = [4, 1, 5, 9, 12, 3, 0, 2, 7, 6]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12]
for idx, i in enumerate(sorted_l):
    assert heapselect(my_list, idx+1) == i

## quickselect
my_list  = [4, 1, 5, 9, 12, 3, 0, 2, 7, 6]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12]
for idx, i in enumerate(sorted_l):
    assert k_quickselect(my_list,  idx+1) == i
