#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import heapq
from tadgrafo3 import *
from _heapq import heappush
from constantes import *

class Caminos():
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self, g,vo,vd, heuristica = None): 
		self.resultado = []
		self.g = g
		pass

	def distancia(self, v):
		if v not in self.resultado: return POSITIVE_INFINITY
		total = 0
		for i in range(0,len(self.resultado)):
			if self.resultado[i] == v:
				return total
			total = total+self.g.get_A(self.resultado[i],self.resultado[i+1]).get_weight()
			
	def visitado(self, v):
		for i in range(0,len(self.resultado)):
			if self.resultado[i] == v:
				return True
		return False
		
	def camino(self):
		return self.resultado



class Dijkstra(Caminos):

	def __init__(self, g,vo,vd,heuristica = None): 
		super(Dijkstra, self).__init__(g,vo,vd,heuristica = None)
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
	
	def __init__(self,g,vo,vd,heuristica = None):
		super(AEstrella, self).__init__(g,vo,vd,heuristica = None)
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
						parAGuardar = [__f__(unCamino,vd,g,heuristica),unCamino]
						g.get_V(id).set_padre(idVerticeActual)
						heappush(abiertos,parAGuardar)	
														
			else:
				final = True				

		###ARMO EL RECORRIDO
		if final:
			self.resultado = par[1]
	


def __f__(camino, vd, g,heuristica):
	return __g__(camino, g) + heuristica(g,camino[-1])

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



	