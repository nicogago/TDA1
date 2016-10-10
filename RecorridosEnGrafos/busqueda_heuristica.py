#!/usr/bin/python
# -*- coding: utf-8 -*-
from tadgrafo import *

def BFS(grafo,i,f): 
	# recorremos todos los vértices del grafo inicializándolos a NO_VISITADO,
	# distancia INFINITA y padre de cada nodo NULL
	sacar_visitados(grafo)
	poner_distancias_inf(grafo)
	eliminar_padres(grafo)

 	i.visitar()
 	i.set_distancia(0)
 	cola[]
 	cola.append(i)

 	termine = False
 	if i.get_id() == f.get_id():
 		termine = True

 	while !cola or !termine:
    # extraemos el nodo u de la cola Q y exploramos todos sus nodos adyacentes
    	u = cola[0]
    	adj_u = grafo.adj(g,i)
    	cola_hijos_prior = Cola_prioridad()
        for v in adj_u:
       		if !v.fue_visitado():
       			v.visitar()
            	v.set_distancia(u.get_distancia() + 1)
            	v.set_padre(u)
            	cola_hijos_prior.add_elem(v)
            	if v.get_id() == f.get_id():
            		return v.get_distancia()

        while !cola_hijos_prior.is_empty():
            cola.append(cola_hijos_prior.get_elem())
 
    if !cola:
    	return POSITIVE_INFINITY
    else return "Error, algo salio muy mal..."

    class Cola_prioridad:
    def __init__(self):
        self.lista = [] 
    
    def heuristica(grafo,elem):
        adj_elem = grafo.adj(grafo,elem)
        cant = 1
        for elem in adj_elem:
            if(!elem.fue_visitado()):
                cant = cant + 1        
        return cant

    def is_empty(self):
        if self.lista:
            return True 
        else: 
            return False

    def add_elem (self,grafo,elem):
        elem_prior = []
        prioridad = heuristica(grafo,elem)
        elem_prior.append(elem)
        elem_prior.append(prioridad)
        self.lista.append(elem_prior)

    def get_elem (self):
        max_prior = POSITIVE_INFINITY
        elem = None
        for elem_prior in lista:
            if !self.lista:
                return None
            else:
                if elem_prior[1] < max_prior:
                    max_prior = elem_prior[1]
                    elem = elem_prior[0]
        return elem
