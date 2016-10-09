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
 	colaQ = []
 	colaQ.append(i)

 	termine = False
 	if i.get_id() == f.get_id():
 		termine = True

 	while !colaQ or !termine:
    # extraemos el nodo u de la cola Q y exploramos todos sus nodos adyacentes
    	u = colaQ[0]
    	adj_u = g.adj(g,i)
    	for  v in adj_u:
       		if ! v.fue_visitado():
       			v.visitar()
            	v.set_distancia(u.get_distancia() + 1)
            	v.set_padre(u)
            	colaQ.append(v)
            	if v.get_id() == f.get_id():
            		return v.get_distancia()

    if !colaQ:
    	return POSITIVE_INFINITY
    else return "Error, algo salio muy mal..."