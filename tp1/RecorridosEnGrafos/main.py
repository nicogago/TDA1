#!/usr/bin/python
# -*- coding: utf-8 -*-

from tadCaminos import *
from constantes import *
from constantes import *

from tadgrafo import *
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

print "otro Dijkstra"
d = Dijkstra( d6, 0, 5)
print d.camino()
print d.visitado (1)
print d.distancia(4)

"""http://stackoverflow.com/questions/5849667/a-search-algorithm
S=0
A=1
B=2
Y=3
X=4
C=5
D=6
E=7"""

print "3er grafo"
d8 = Digraph(8)
print "agrego aristas" 
d8.add_edge( 0, 1, 1)
d8.add_edge( 0, 2, 2)
d8.add_edge( 1, 3, 7)
d8.add_edge( 1, 4, 4)
d8.add_edge( 2, 5, 7)
d8.add_edge( 2, 6, 1)
d8.add_edge( 3, 7, 3)
d8.add_edge( 4, 7, 2)
d8.add_edge( 5, 7, 5)
d8.add_edge( 6, 7, 12)

print "testeo A*"
d = AEstrella( d8, 0, 7)
print d.camino()

""" ej de :
http://stackoverflow.com/questions/20162735/a-algorithm-on-a-directed-graph?noredirect=1&lq=1
"""

print "4to grafo"
d7 = Digraph(7)
print "agrego aristas" 
d7.add_edge( 0, 1, 2)
d7.add_edge( 0, 2, 11)
d7.add_edge( 0, 3, 1)
d7.add_edge( 1, 4, 3)
d7.add_edge( 2, 1, 2)
d7.add_edge( 2, 6, 1)
d7.add_edge( 2, 5, 1)
d7.add_edge( 3, 5, 15)
d7.add_edge( 3, 2, 12)
d7.add_edge( 4, 2, 5)
d7.add_edge( 4, 6, 7)
d7.add_edge( 5, 6, 1)


print "testeo A*"
d2 = AEstrella( d7, 0, 6)
print d2.camino()

