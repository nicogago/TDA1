#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 0 < inicio <= len(M)
def viajante(inicio, M):
    S = list(range(len(M)))
    v = inicio - 1
    S.remove(v)
    costos = {}

    def D(x, conjunto):
        if (str(x)+str(conjunto)) in  costos:
            return costos[str(x)+str(conjunto)]

        if (len(conjunto) == 0):
            print 'g(', x, ',[]) = ', M[x][v]
            return M[x][v]

        values = []
        for elem in conjunto:
            subconjunto = list(conjunto)
            subconjunto.remove(elem)
            values.append(M[x][elem] + D(elem, subconjunto))
        print 'g(', x, ',',conjunto,') = ', min(values)
        costos[str(x)+str(conjunto)] = min(values)
        return min(values)

    return D(v, S)
