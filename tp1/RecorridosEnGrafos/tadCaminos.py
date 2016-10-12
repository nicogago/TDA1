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
		pass

	def distancia(self, v):
		total = 0
		for i in range(0,len(self.resultado)):
			total = total+self.resultado[i][0]
			if self.resultado[i][1] == v:
				return total
		return POSITIVE_INFINITY

	def visitado(self, v):
		for i in range(0,len(self.resultado)):
			if self.resultado[i][1] == v:
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
			self.resultado.append(verticeVisitado)
			verticesAdyacentes = g.adj(verticeVisitado[1])
			
			for vertice in verticesAdyacentes:
				pesoDelVisitadoAlVertice = g.get_A(verticeVisitado[1], vertice.get_id()).get_weight()
				if ( not vertice.fue_visitado() ) and ( vertice.get_distancia() > pesoDelVisitadoAlVertice):
					vertice.set_distancia(pesoDelVisitadoAlVertice)
					vertice.set_padre(verticeVisitado)
					heappush(heap,(pesoDelVisitadoAlVertice,vertice.get_id()))
					
	
class AEstrella(Caminos):

	def __init__(self,g,vo,vd):
		super(AEstrella, self).__init__(g,vo,vd)
		abiertos = []
		#terna = [0, 0, vo] # [f(x), g(x), Id del vertice]
		unCamino = [vo]
		par = [0,unCamino] #dejo f(x) como 0
		heappush(abiertos,par)
		final = False
		padre = None
		verticeActual = None

		while abiertos and not final:
			par = heapq.heappop(abiertos)
			verticeActual = par[1][-1]
			g.get_V(verticeActual).set_padre(padre) #???
			if verticeActual != vd:
				vecinos = g.adj(verticeActual)
				for v in vecinos:
					parAGuardar = [None,None]
					id = v.get_id()
					unCamino = par[1] + [id]
					parAGuardar = [__f__(unCamino,vd,g),unCamino]
					heappush(abiertos,parAGuardar)
									
			else:
				final = True
				g.get_V(verticeActual).set_padre(padre)#???
				

		###ARMO EL RECORRIDO
		self.resultado = par[1]
		
	
	# realizado según http://stackoverflow.com/questions/5849667/a-search-algorithm
def __f__(camino, vd, g):
	return __g__(camino, g) + __heuristica__(camino[-1],vd)

def __g__(camino, g):
	total = 0
	for elem in range(0,len(camino)-1):
		print camino[elem]
		print camino[elem+1]
		total = total + g.get_A(camino[elem], camino[elem+1]).get_weight() #sumo los pesos de las aristas
	return total
		
def __heuristica__(v,vd):
	return 1
