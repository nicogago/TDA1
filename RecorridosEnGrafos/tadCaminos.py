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

	@abstractmethod
	def distancia(self, v):
		pass

	@abstractmethod
	def edge_to(self, v):
		pass

	def visitado(self, v):
		return  self.distancia(v) < self.POSITIVE_INFINITY
		
	def camino(self):
		return self.resultado



class Dijkstra(Caminos):

	def __init__(self, g,vo,vd): 
		print "init dijkstra way"
		super(Dijkstra, self).__init__(g,vo,vd)
		heap = []
		heappush(heap,(0,vo))

		while heap and not g.get_V(vd).fue_visitado():
			verticeVisitado = heapq.heappop(heap)
			g.get_V(verticeVisitado[1]).visitar()
			self.resultado.append(verticeVisitado[1])
			verticesAdyacentes = g.adj(verticeVisitado[1])
			
			for vertice in verticesAdyacentes:
				pesoDelVisitadoAlVertice = g.get_A(verticeVisitado[1], vertice.get_id()).get_weight()
				print "pesoDelVisitadoAlVertice = " + str(pesoDelVisitadoAlVertice)
				if ( not vertice.fue_visitado() ) and ( vertice.get_distancia() > pesoDelVisitadoAlVertice):
					vertice.set_distancia(pesoDelVisitadoAlVertice)
					vertice.set_padre(verticeVisitado)
					heappush(heap,(pesoDelVisitadoAlVertice,vertice.get_id()))
					
	def distancia(self, v):
		return NotImplemented

	def edge_to(self, v):
		return NotImplemented

	
class Aasterisk(Caminos):

	def __init__(self,g,vo,vd):
		return NotImplemented

	def distancia(self, v):
		return NotImplemented

	def edge_to(self, v):
		return NotImplemented
		