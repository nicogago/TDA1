#!/usr/bin/python
# -*- coding: utf-8 -*-

from tadgrafo import *
import heapq

# Algoritmo de Prim
# A partir de un grafo dirigido/no dirigido, completo y pesado genera un árbol de tendido
# mínimo (Minimum Spanning Tree), el cual es devuelto en un grafo dirigido,
# no completo y pesado.

def mst_prim(digraph, root):
    mst = Digraph(digraph.V())
    map_parents = {}
    map_weights = {}
    heap = []
    visited = []

    for v_id in digraph.getVertices():
        map_parents[v_id] = None
        map_weights[v_id] = POSITIVE_INFINITY
        heap.append((POSITIVE_INFINITY, digraph.get_V(v_id)))

    heap[root] = (0, digraph.get_V(root))

    heapq.heapify(heap)

    while len(heap) > 0:
        u = heapq.heappop(heap) # devuelve una tupla (priority, Vert)
        v = u[1]
        visited.append(v)
        neighbors = v.get_neighbors()
        for adj in neighbors:
            src = v.get_id()
            dst = adj.get_id()
            edge = digraph.get_A(src, dst)
            # Verifica si el vértice adyacente se encuentra en el heap
            if (not adj in visited) and (edge.get_weight() < map_weights[dst]):
                map_parents[dst] = v
                map_weights[dst] = edge.get_weight()

    for dst,src in map_parents.iteritems():
        if src != None:
            mst.add_edge(src.get_id(), dst, map_weights[dst])

    return mst
