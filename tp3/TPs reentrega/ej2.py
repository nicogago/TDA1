#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo3 import *

def reduce_ss_to_zwc(values):
    # 0,2,4,6... van a ser los u
    # 1,3,5,7... van a ser los v
    # un vert representado por i e i+1
    # peso ai desde ui hasta vi
    # peso cero desde todos los vj hacia ui
    # peso cero desde todos los vi hacia uj
    cantVert = len(values) * 2
    g = Digraph(cantVert)
    i = 0
    for peso in values:
        # peso ai desde ui hasta vi
        g.add_edge(i,i+1,peso) 
        j = 0
        while j < cantVert:
            if j != i:
                # peso cero desde todos los vj hacia ui y vi a uj 
                g.add_edge(j+1,i,0)
                # peso cero desde todos los vi hacia uj notar           
                #g.add_edge(i+1,j,0)
            j = j + 2
        i = i + 2        
    return g

values = set([1,2,-3])
g = reduce_ss_to_zwc(values)
for adge in g.iter_edges():
    print adge