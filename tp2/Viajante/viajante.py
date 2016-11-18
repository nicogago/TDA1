#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 0 < inicio <= len(M)
def viajante(inicio, M):
    S = list(range(len(M)))
    v = inicio - 1
    S.remove(v)
    costos = {}
    parents = {}
    rec = []

    def D(x, conjunto):
        if (str(x)+str(conjunto)) in  costos:
            return costos[str(x)+str(conjunto)]

        if (len(conjunto) == 1):
            if (str(conjunto[0])+str([x])) in costos:
                return costos[str(conjunto[0])+str([x])]

        if (len(conjunto) == 0):
#            print 'g(', x, ',[]) = ', M[x][v]
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
#        print 'g(', x, ',',conjunto,') = ', min(values)
        costo_min = min(values)
        costos[str(x)+str(conjunto)] = costo_min
        prox_vert_cercano = conjunto[values.index(costo_min)]
        parents[str(x)+str(conjunto)] = prox_vert_cercano
        return min(values)

    def recorrido(x, conjunto):
        if len(conjunto) == 0:
            return
        vertice = parents[str(x)+str(conjunto)]
#        print 'p(', x, ',', str(conjunto),') = ', vertice
        rec.insert(0, vertice+1)
        subconjunto = list(conjunto)
        subconjunto.remove(vertice)
        recorrido(vertice, subconjunto)

    costoTotal = D(v, S)
    recorrido(v, S)
    rec.insert(0, v+1)
    rec.append(v+1)
    print 'Recorrido: ', rec
    print 'Costo Total:', costoTotal
