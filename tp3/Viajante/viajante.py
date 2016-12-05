#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time
from mst_prim import *

# 0 < start <= len(M)
def viajante(start, M):
    digraph = Digraph(len(M))
    travel = []
    total_cost = 0

    print
    print "Matriz de pesos\n"
    for i in range(0, len(M)):
        print M[i]
        for j in range(0, len(M)):
            # agregamos las aristas correspondientes con sus pesos
            try:
                digraph.add_edge(i, j, M[i][j]) # para matrices asimétricas
            except IndexError:
                digraph.add_edge(i, j, M[j][i]) # en caso de error para matrices simétricas
    print

    t_start = time()
    # Digrafo no completo y pesado (start = root)
    mst = mst_prim(digraph, start-1)

#   Descomentar si se desea ver el árbol de tendido mínimo
#    print "\nÁrbol de tendido mínimo ( raíz:", str(start), ")\n"
#    for edge in mst.iter_edges():
#        print "src: ", edge.get_from()+1, "\tdst: ", edge.get_to()+1, "\tweight: ", edge.get_weight()

    # realizamos un recorrido en pre-orden del digrafo generado con mst_prim
    def preorder(start, mst_prim):
        neighbors = mst_prim.adj(start)
        if len(neighbors) == 0:
            return
        for v in neighbors:
            travel.append(v.get_id())
            preorder(v.get_id(), mst_prim)

    preorder(start-1, mst)
    travel.insert(0, start-1)
    travel.append(start-1)

    for i in range(0, len(travel)-1):
        src = travel[i]
        dst = travel[i+1]
        try:
            total_cost += M[src][dst]
        except IndexError:
            total_cost += M[dst][src]

    time_diff = time() - t_start

    travel = [x+1 for x in travel]
    print "\nRecorrido: ", travel
    print "\nCosto Total: ", total_cost
    print '\nTiempo de ejecución: ', time_diff, ' segundos'
