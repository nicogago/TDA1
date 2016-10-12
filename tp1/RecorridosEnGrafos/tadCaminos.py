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
		terna = [0, 0, vo] # [f(x), g(x), Id del vertice]
		heappush(abiertos,(terna))
		final = False
		padre = None
		verticeActual = None

		abiertos.append(terna)
		while abiertos and not final:
			print "balblabal"
			padre = verticeActual
			terna = heapq.heappop(abiertos)
			verticeActual = terna[2]
			g.get_V(verticeActual).set_padre(padre)
			if verticeActual != vd:
				vecinos = g.adj(verticeActual)
				ternaAGuardar = [0,0,0]
				for v in vecinos:
					id = v.get_id()
					ternaAGuardar[2] = id 
					ternaAGuardar[1] = terna[1] + g.get_A(verticeActual, id).get_weight() #el g(x) anterior + el nuevo peso
					ternaAGuardar[0] = ternaAGuardar[1] + heuristica(id, vd) # el nuevo g(x) + heuristica desde aca al fin
					heappush(abiertos,(ternaAGuardar))
									
			else:
				final = True
				g.get_V(verticeActual).set_padre(padre)

		###ARMO EL RECORRIDO
		while verticeActual != None:
			print "holaaaa"
			[verticeActual] + self.resultado
			verticeActual = g.get_V(verticeActual).get_padre()
			
		
	
	# realizado según http://stackoverflow.com/questions/5849667/a-search-algorithm
	
		
def heuristica(v,vd):
	return 1
