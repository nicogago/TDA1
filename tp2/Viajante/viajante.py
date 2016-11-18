#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time

# 0 < inicio <= len(M)
def viajante(inicio, M):
    S = list(range(len(M)))
    v = inicio - 1
    S.remove(v)
    costos = {}
    parents = {}
    rec = []

    def D(x, conjunto):
        # Devuelve una solución parcial si es que existe
        if (str(x)+str(conjunto)) in  costos:
            return costos[str(x)+str(conjunto)]

        # Para matrices simétricas y asimétricas
        if (len(conjunto) == 0):
            try:
                return M[x][v]
            except IndexError:
                return M[v][x]

        values = []
        for elem in conjunto:
            subconjunto = list(conjunto)
            subconjunto.remove(elem)
            try:
                values.append(M[x][elem] + D(elem, subconjunto))
            except IndexError:
                values.append(M[elem][x] + D(elem, subconjunto))
        costo_min = min(values)
        costos[str(x)+str(conjunto)] = costo_min
        prox_vert_cercano = conjunto[values.index(costo_min)]
        # Guardamos el nodo padre para un subconjunto para luego hallar el recorrido
        parents[str(x)+str(conjunto)] = prox_vert_cercano
        return min(values)

    def recorrido(x, conjunto):
        if len(conjunto) == 0:
            return
        vertice = parents[str(x)+str(conjunto)]
        rec.insert(0, vertice+1)
        subconjunto = list(conjunto)
        subconjunto.remove(vertice)
        recorrido(vertice, subconjunto)

    t_start = time()
    costoTotal = D(v, S)
    time_diff = time() - t_start
    print 'Tiempo de ejecución: ', time_diff, ' segundos'

    recorrido(v, S)
    rec.insert(0, v+1)
    rec.append(v+1)
    print 'Recorrido: ', rec
    print 'Costo Total:', costoTotal
