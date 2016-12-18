#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo3 import *

def verificador_zwc(grafo, vertices):     
    # grafo: digrafo. 
    # vertices: lista de elementos ordenados en donde el ultimo
    #           elemento se conecta con el primero para terminar 
    #           el ciclo.
    # ej de vertices [1,2,3,4] y representa: 1->2->3->4->1.
    elem0 = vertices[0]
    elemAnt = elem0
    sumatoria = 0
    for elem in vertices:
        if elem != elem0:
            arista = grafo.get_A(elemAnt,elem)
            sumatoria = arista.get_weight()
            elemAnt = elem
    arista = grafo.get_A(elem,elem0)
    sumatoria = sumatoria + arista.get_weight()
    if sumatoria == 0:
        return True
    return False

