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
 	cola_prior = Cola_prioridad()
 	cola_prior.add_elem(i)

 	termine = False
 	if i.get_id() == f.get_id():
 		termine = True

 	while !colaQ or !termine:
    # extraemos el nodo u de la cola Q y exploramos todos sus nodos adyacentes
    	u = cola_prior.get_elem()
    	adj_u = g.adj(g,i)
    	for  v in adj_u:
       		if ! v.fue_visitado():
       			v.visitar()
            	v.set_distancia(u.get_distancia() + 1)
            	v.set_padre(u)
            	cola_prior.add_elem(v)
            	if v.get_id() == f.get_id():
            		return v.get_distancia()

    if !cola_prior.is_empty():
    	return POSITIVE_INFINITY
    else return "Error, algo salio muy mal..."

    class Cola_prioridad:
    def __init__(self):
        self.lista = [] 
    
    def heuristica(grafo,elem):
        prioridad = 1
        return prioridad

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
        max_prior = -1
        elem = None
        for elem_prior in lista:
            if !self.lista:
                return None
            else:
                if elem_prior[1] > max_prior:
                    max_prior = elem_prior[1]
                    elem = elem_prior[0]
        return elem



