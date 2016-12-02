#!/usr/bin/python
# -*- coding: utf-8 -*-

from tadgrafo import *
import heapq

# Actualiza la cola. En caso de que exista ese ítem con prioridad mayor se
# elimina y se agrega el ítem con su nueva prioridad
#def updateQueue(queue, item, priority):


def mst_prim(digraph, root):
    countV = digraph.V()
    mst = Digraph(countV)
    map_parents = {}
    map_weight = {}
    map_ids = {}
    heap = []
    visited = []

    for v_id in digraph.getVertices():
        map_parents[v_id] = None
        map_weight[v_id] = POSITIVE_INFINITY
        heap.append((POSITIVE_INFINITY, digraph.get_V(v_id)))

    heap[root] = (0, digraph.get_V(root))

    heapq.heapify(heap)

    while len(heap) > 0:
        u = heapq.heappop(heap) # return (priority, Vert)
        v = u[1]
    #    visited.append(v)
        neighbors = v.get_neighbors()
        for adj in neighbors:
            src = v.get_id()
            dst = adj.get_id()
            edge = digraph.get_A(src, dst)
            # Verifica si el vértice adyacente se encuentra en el heap
            if (not adj in visited) and (edge.get_weight() < map_weight[dst]):
                map_parents[dst] = v
                map_ids[dst] = v.get_id()
                map_weight[dst] = edge.get_weight()
                visited.append(v)

    print "pesos: ", map_weight
    print "ids: ", map_ids
#    print map_parents
