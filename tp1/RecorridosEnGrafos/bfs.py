#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo import *

def BFS(grafo,i,f): 
	# recorremos todos los vértices del grafo inicializándolos a NO_VISITADO,
	# distancia INFINITA y padre de cada nodo NULL
	grafo.sacar_visitados()
	grafo.poner_distancias_inf()
	grafo.eliminar_padres()
	
	i.visitar()
	i.set_distancia(0)
	colaQ = []
	colaQ.append(i)

	termine = False
	if i.get_id() == f.get_id():
		termine = True

	while colaQ and not termine:
	# extraemos el nodo u de la cola Q y exploramos todos sus nodos adyacentes
		u = colaQ.pop(0)
		print u.get_id()
		adj_u = grafo.adj(u.get_id())
		for v in adj_u:
			if not v.fue_visitado():
				v.visitar()
				v.set_distancia(u.get_distancia() + 1)
				v.set_padre(u)

				colaQ.append(v)
				if v.get_id() == f.get_id():
					return v.get_distancia()

	if not colaQ:
		return POSITIVE_INFINITY
	else: return "Error, algo salio muy mal..."



graph = Digraph(19)
graph.add_edge( 0, 1, 1)
graph.add_edge( 0, 2, 2)
graph.add_edge( 0, 3, 3)
graph.add_edge( 1, 4, 4)
graph.add_edge( 1, 5, 5)
graph.add_edge( 2, 6, 6)
graph.add_edge( 2, 7, 7)
graph.add_edge( 2, 8, 8)
graph.add_edge( 3, 9, 9)
graph.add_edge( 4, 14, 10)
graph.add_edge( 5, 15, 11)
graph.add_edge( 6, 11, 12)
graph.add_edge( 7, 12, 13)
graph.add_edge( 8, 13, 14)
graph.add_edge( 9, 10, 15)
graph.add_edge( 10, 16, 16)

ads = BFS(graph,graph.get_V(0),graph.get_V(18))
print ads