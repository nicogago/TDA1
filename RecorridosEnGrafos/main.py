#!/usr/bin/python
# -*- coding: utf-8 -*-

from tadCaminos import *
from constantes import *
from constantes import *

from tadGrafo import *
from busqueda_heuristica import *
from bfs import *

d4 = Digraph(4)

print "aristas = " + str(d4.E())
print "vertices = " + str(d4.V())

# testeo las funciones de Digraph
print "agrego aristas"
d4.add_edge( 1, 2, 20)
d4.add_edge( 0, 1, 3)
d4.add_edge( 0, 3, 15)
d4.add_edge( 1, 3, 9)
d4.add_edge( 1, 1)
d4.add_edge( 2, 3, 7)

print "aristas = " + str(d4.E())
print "vertices = " + str(d4.V())

print "testeo iter_edges()" 

i = d4.iter_edges()
for a in i:
    print a.get_weight()
    
print "testeo adj_e"
i = d4.adj_e( 1) 
for a in i:
    print a.get_weight()
    
print "testeo adj"
i = d4.adj( 1) 
for a in i:
    print a.get_id()

print "testeo Dijkstra"
d = Dijkstra( d4, 0, 3)
print d.camino()
print d.distancia(1)
print d.distancia(2)
print d.distancia(3)

print "otro grafo"
d6 = Digraph(6)
print "agrego aristas"
d6.add_edge( 0, 1, 4)
d6.add_edge( 0, 2, 2)
d6.add_edge( 1, 3, 5)
d6.add_edge( 2, 3, 8)
d6.add_edge( 2, 4, 10)
d6.add_edge( 3, 4, 2)
d6.add_edge( 4, 3, 2)
d6.add_edge( 3, 5, 6)
d6.add_edge( 4, 5, 2)
print "testeo Dijkstra"
d = Dijkstra( d6, 0, 5)
print d.camino()


