#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo import *


def __heuristica__(grafo,elem):
	adj_elem = grafo.adj(elem.get_id())
	cant = 1
	for elem in adj_elem:
		if(not elem.fue_visitado()):
			cant = cant + 1        
	return cant

def BFS_heuristica(grafo,inf,fin): 
	# recorremos todos los vértices del grafo inicializándolos a NO_VISITADO,
	# distancia INFINITA y padre de cada nodo NULL
	i = grafo.get_V(inf)
	f = grafo.get_V(fin)

	grafo.sacar_visitados()
	grafo.poner_distancias_inf()
	grafo.eliminar_padres()

	i.visitar()
	i.set_distancia(0)
	cola = []
	cola.append(i)

	termine = False
	if i.get_id() == f.get_id():
		termine = True

	while cola and not termine:
		# extraemos el nodo u de la cola Q y exploramos todos sus nodos adyacentes
		u = cola.pop(0)
		adj_u = grafo.adj(u.get_id())
		cola_hijos_prior = Cola_prioridad()
		for v in adj_u:
			if not v.fue_visitado():
				v.visitar()
				v.set_distancia(u.get_distancia() + 1)
				v.set_padre(u)
				cola_hijos_prior.add_elem(grafo,v)
				if v.get_id() == f.get_id():
					return v.get_distancia()

		while not cola_hijos_prior.is_empty():
			elem = cola_hijos_prior.get_elem()
			cola.append(elem)
 
	if not cola:
		return POSITIVE_INFINITY
	else: return "Error, algo salio muy mal..."

class Cola_prioridad:
	def __init__(self):
		self.lista = [] 

	def get_cola(self):
		return self.lista

	def is_empty(self):
		if not self.lista: return True 
		else: return False

	def add_elem (self,grafo,elem):
		elem_prior = []
		prioridad = __heuristica__(grafo,elem)
		elem_prior.append(elem)
		elem_prior.append(prioridad)
		self.lista.append(elem_prior)


	def get_elem (self):
		max_prior = POSITIVE_INFINITY
		elem = None
		cont = 0
		ind = 0
		
		if not self.lista:
			return None
		for elem_prior in self.lista:		
			if elem_prior[1] < max_prior:
				max_prior = elem_prior[1]
				elem = elem_prior[0]
				ind = cont 
			cont = cont + 1
		self.lista.pop(ind)
		return elem


"""
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

ads = BFS_heuristica(graph,graph.get_V(0),graph.get_V(18))
"""