#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo import *

def BFS(grafo,inf,fin): 
	# recorremos todos los vértices del grafo inicializándolos a NO_VISITADO,
	# distancia INFINITA y padre de cada nodo NULL
	i = grafo.get_V(inf)
	f = grafo.get_V(fin)

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

