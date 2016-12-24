#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from tadgrafo3 import *

def esCicloSimple(lVertices):
	# lVertices: lista de elementos
	# se debe chequear si hay elementos repetidos en la lista
	elem = lVertices.pop()
	if lVertices:
		if elem in lVertices:
			return False
		else:
			if not esCicloSimple(lVertices):
				return False
	return True	 

def verificador_zwc(grafo, vertices):     
	# grafo: digrafo. 
	# vertices: lista de elementos ordenados en donde el ultimo
	#           elemento se conecta con el primero para terminar 
	#           el ciclo.
	# ej de vertices [1,2,3,4] y representa: 1->2->3->4->1.
	aux = copy.deepcopy(vertices)
	if esCicloSimple(aux):
		elem0 = vertices[0]
		elemAnt = elem0
		sumatoria = 0
		for elem in vertices:
			if elem != elem0:
				arista = grafo.get_A(elemAnt,elem)
				if arista == None:
					return false
				sumatoria = sumatoria + arista.get_weight()
				elemAnt = elem
		arista = grafo.get_A(elem,elem0)
		sumatoria = sumatoria + arista.get_weight()
		print (sumatoria)
		if sumatoria == 0:
			return True
		return False
	else:
		print ("No es un ciclo simple...")
		return False

g = Digraph(6)
g.add_edge(0,1,3)
g.add_edge(1,2,4)
g.add_edge(2,0,2)
g.add_edge(0,5,4)
g.add_edge(5,4,3)
g.add_edge(4,3,1)
g.add_edge(3,0,-8)

#for adge in g.iter_edges():
#    print adge

verticesT = [0,5,4,3]
verticesF = [0,1,2]
verticesFC= [0,5,4,3,0,5,4,3]

res = verificador_zwc(g, verticesT)
print (res)
res = verificador_zwc(g, verticesF)
print (res)
res = verificador_zwc(g, verticesFC)
print (res)

"""
cTrue = [0,5,4,3]
cFalse = [0,1,2,3,2,5]
res = esCicloSimple(cTrue)
print (res)
res = esCicloSimple(cFalse)
print (res)
"""