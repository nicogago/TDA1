#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import heapq
from tadgrafo import *
from _heapq import heappush
from constantes import *

class Caminos():
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self, g,vo,vd): 
		self.resultado = []
		self.g = g
		pass

	def distancia(self, v):
		total = 0
		for i in range(0,len(self.resultado)-1):
			if self.resultado[i] == v:
				return total
			total = total+self.g.get_A(self.resultado[i],self.resultado[i+1]).get_weight()
		return POSITIVE_INFINITY

	def visitado(self, v):
		for i in range(0,len(self.resultado)):
			if self.resultado[i] == v:
				return True
		return False
		
	def camino(self):
		return self.resultado



class Dijkstra(Caminos):

	def __init__(self, g,vo,vd): 
		super(Dijkstra, self).__init__(g,vo,vd)
		heap = []
		heappush(heap,(0,vo))

		while heap and not g.get_V(vd).fue_visitado():
			verticeVisitado = heapq.heappop(heap)
			g.get_V(verticeVisitado[1]).visitar()
			verticesAdyacentes = g.adj(verticeVisitado[1])
			
			for vertice in verticesAdyacentes:
				pesoDelVisitadoAlVertice = g.get_A(verticeVisitado[1], vertice.get_id()).get_weight()
				if ( not vertice.fue_visitado() ) and ( vertice.get_distancia() > pesoDelVisitadoAlVertice):
					vertice.set_distancia(pesoDelVisitadoAlVertice)
					vertice.set_padre(verticeVisitado[1])
					heappush(heap,(pesoDelVisitadoAlVertice,vertice.get_id()))
		self.armarResultado(vd)
	
	def armarResultado(self,vd):
		self.resultado = [vd]
		padre = self.g.get_V(vd).get_padre()
		while padre != None:
			self.resultado = [padre] + self.resultado
			padre = self.g.get_V(padre).get_padre()
			
		
		
	
class AEstrella(Caminos):
	
	def __init__(self,g,vo,vd):
		super(AEstrella, self).__init__(g,vo,vd)
		abiertos = []
		unCamino = [vo]
		par = [0,unCamino] #dejo f(x) como 0
		heappush(abiertos,par)
		final = False
		padre = None
		verticeActual = None

		while abiertos and not final:
			par = heapq.heappop(abiertos)
			idVerticeActual = par[1][-1]
			if idVerticeActual != vd:
				vecinos = g.adj(idVerticeActual)
				for v in vecinos:
					id = v.get_id()
					if (id != idVerticeActual):
						parAGuardar = [None,None]
						unCamino = par[1] + [id]
						parAGuardar = [__f__(unCamino,vd,g),unCamino]
						g.get_V(id).set_padre(idVerticeActual) #???
						heappush(abiertos,parAGuardar)	
														
			else:
				final = True				

		###ARMO EL RECORRIDO
		if final:
			self.resultado = par[1]
	
def __f__(camino, vd, g):
	return __g__(camino, g) + __heuristica__(g,camino[-1])

def __g__(camino, g):
	total = 0
	for elem in range(0,len(camino)-1):
		total = total + g.get_A(camino[elem], camino[elem+1]).get_weight() #sumo los pesos de las aristas
	return total
		
def __heuristica__(grafo,elem):
	adj_elem = grafo.adj(elem)
	cant = 1
	for elem in adj_elem:
		if(not elem.fue_visitado()):
			cant = cant + 1        
	return cant

def __mockHeuristica__(g,v):
	#heuristica para probar el ejemplo de http://stackoverflow.com/questions/5849667/a-search-algorithm 
	if v == 1: return 5
	if v == 2: return 6
	if v == 3: return 8
	if v == 4: return 5
	if v == 5: return 4
	if v == 6: return 15
	return 0

def __mock2Heuristica__(g,v):
	#heuristica para probar el ejemplo de http://stackoverflow.com/questions/20162735/a-algorithm-on-a-directed-graph?noredirect=1&lq=1
	if v == 1: return 7
	if v == 2: return 0
	if v == 3: return 11
	if v == 4: return 5
	if v == 5: return 1
	if v == 0: return 8
	return 0

def __estaEnLista__(lista,v):
	for i in range(0,len(lista)):
		if lista[i][1] == v:
			return True
	return False

	