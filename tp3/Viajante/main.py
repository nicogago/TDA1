#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from parser import *
from mst_prim import *

# Verificación de argumentos (validación)

cant_args = len(sys.argv) - 1
if cant_args != 2:
    print 'Cantidad de argumentos inválidos. Ejecute el siguiente comando:'
    print '> python main.py <vértice> testfiles/<archivo_de_prueba>'
    quit()

testfile = str(sys.argv[2])

if not '.tsp' in testfile:
    print 'Archivo de prueba en formato inválido.'
    quit()

if str(sys.argv[1]).isdigit() == False:
    print 'Vértice inválido. Ingrese un número no negativo.'
    quit()

vertice_id = int(sys.argv[1])

M = parse(testfile)
digraph = Digraph(len(M))

print
print "Matriz de pesos\n"
for i in range(0, len(M)):
    print M[i]
    for j in range(0, len(M)):
        try:
            digraph.add_edge(i, j, M[i][j]) # para matrices asimétricas
        except IndexError:
            digraph.add_edge(i, j, M[j][i]) # en caso de error para matrices simétricas
print

mst = mst_prim(digraph, 0)

print "\nÁrbol de tendido mínimo\n"
for edge in mst.iter_edges():
    print "src: ", edge.get_from(), "\tdst: ", edge.get_to(), "\tweight: ", edge.get_weight()
'''
#viajante(vertice_id, M)
d4 = Digraph(4)

print "aristas = " + str(d4.E())
print "vertices = " + str(d4.V())

# testeo las funciones de Digraph
print "agrego aristas"
d4.add_edge( 0, 1, 1)
d4.add_edge( 0, 2, 3)
d4.add_edge( 0, 3, 1)
d4.add_edge( 1, 0, 2)
d4.add_edge( 1, 2, 1)
d4.add_edge( 1, 3, 1)
d4.add_edge( 2, 0, 2)
d4.add_edge( 2, 1, 3)
d4.add_edge( 2, 3, 1)
d4.add_edge( 3, 0, 1)
d4.add_edge( 3, 1, 2)
d4.add_edge( 3, 2, 3)

print "aristas = " + str(d4.E())
print "vertices = " + str(d4.V())

mst_prim(d4,1)
'''
