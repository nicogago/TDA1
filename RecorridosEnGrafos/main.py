#!/usr/bin/python
# -*- coding: utf-8 -*-

from tadCaminos import *
from constantes import *
from constantes import *

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
