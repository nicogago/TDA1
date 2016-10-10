#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from tadCaminos import *
from constantes import *

class Vert:
    def __init__(self,node):
        self.id = node
        self.vecinos = {}
        self.visitado = False
        self.distancia = POSITIVE_INFINITY
        self.padre = None 
                
    def add_neighbor (self ,dst,w = 0):
        self.vecinos[dst] = w

    def get_neighbors (self):
        return self.vecinos
    
    def get_id(self):
        return self.id

    def get_weight (self, dst):
        return self.vecinos[dst].get_weight()

    def visitar(self):
        self.visitado = True

    def fue_visitado(self):
        return self.visitado

    def setear_no_visitado(self):
        self.visitado = False
        
    def set_padre(self, padre):
        self.padre = padre
        
    def set_distancia(self, distancia):
        self.distancia = distancia
        
    def set_distancia_inf():
        self.distancia = POSITIVE_INFINITY

    def set_padre_vacio():
        self.padre = None

    def get_distancia(self):
        return self.distancia


class Digraph:
    """Grafo no dirigido con un número fijo de vértices.
    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas.
    """
    
    def __init__(g, V):  # @NoSelf
        """Construye un grafo sin aristas de V vértices.
        """
        g.aristas = []
        g.vertices = {}
        for i in range(0,V):
            new_vert = Vert(i)
            g.vertices[i] = new_vert

    def V(g):   # @NoSelf
        """Número de vértices en el grafo.
        """
        return len(g.vertices)

    def E(g):   # @NoSelf
        """Número de aristas en el grafo.
        """
        return len(g.aristas)

    def adj_e(g, v):    # @NoSelf
        """Itera sobre los aristas incidentes _desde_ v.
        """
        aristas_incidentes_de_v = []
        for i in range(0,len(g.aristas)):
            if g.aristas[i].get_from() == v : 
                aristas_incidentes_de_v.append(g.aristas[i])
        return iter(aristas_incidentes_de_v)



    def adj(g, v):  # @NoSelf
        """Itera sobre los vértices adyacentes a ‘v’.
        """
        return iter(g.vertices[v].get_neighbors())


    def add_edge(g, u, v, weight=0):    # @NoSelf
        """Añade una arista al grafo.
        """
        g.vertices[u].add_neighbor(g.vertices[v],weight)
        new_edge = Arista(u,v,weight)
        g.aristas.append(new_edge)


    def __iter__(g):    # @NoSelf
        """Itera de 0 a V."""
        return iter(range(g.vertices))
    
    def get_V(g,v): # @NoSelf
        return g.vertices[v]
    
    def get_A(self, src, dst):
        for i in range(0,len(self.aristas)):
            arista = self.aristas[i]
            if (arista.get_from() == src ) and (arista.get_to() == dst) : 
                return arista
        return None

    def iter_edges(g):  # @NoSelf
        """Itera sobre todas las aristas del grafo.
    
        Las aristas devueltas tienen los siguientes atributos de solo lectura:
    
            • e.src
            • e.dst
            • e.weight
        """
        return iter(g.aristas)

    def sacar_visitados(g): # @NoSelf
        for i in range(0,g.V):
            g.vertices[i].setear_no_visitado()
    def poner_distancias_inf(g): # @NoSelf
        for i in range(0,g.V):
            g.vertices[i].poner_distancias_inf()
    def eliminar_padres(g): # @NoSelf
        for i in range(0,g.V):
            g.vertices[i].set_padre_vacio()

"""    def get_weight(g,i,f):  # @NoSelf
        for i in range(0,g.cant_aristas):
            if g.aristas[i].get_from() == v : 
                aristas_incidentes_de_v[cant_aristas_incidentes_desde_v] = g.vertices[g.aristas[i].get_to()]
                cant_aristas_incidentes_desde_v = cant_aristas_incidentes_desde_v + 1
   """ 

class Arista:
    """Arista de un grafo.
      """
    def __init__(self, src, dst, weight=0):
        # inicializar y do things 
        self.src = src
        self.dst = dst
        self.weight = weight
      
    def get_weight (self):
        return self.weight
    
    def get_from (self):
        return self.src
    
    def get_to (self):
        return self.dst
    




#FUNCIONES DE FER

"""
def heuristica (g,i,f,peso = 0):
  u = random.random()        # Random float x, 0.0 <= x < 1.0     
  vecinos = i.get_neighbors() 
  if f in i.get_neighbors().keys():
    return (get_weight(g,i,f) + peso)
  else:
    if u < 0.75 :
      menor = get_nodo_menor_peso(g,i,vecinos)
      peso = peso + get_weight(menor)
      return heuristica(g,menor,f,peso)
    else:
      nodo = get_random_nodo(vecinos)
      peso = peso + get_weight(nodo)
      return heuristica(g,nodo,f,peso)

def get_nodo_menor_peso(g,i,vect):
  peso = None 
  for x in vect:
    if peso == None : 
      peso = dar_peso(g,i,x)
    else:
      aux_peso = dar_peso(g,i,x)
      if (peso > aux_peso):
        peso = aux_peso
  return peso

def dar_peso(g,i,f):
  for i in range(0,cant_aristas):
    if g.aristas[i].get_from() == i and g.aristas[i].get_to() == f: 
      return g.aristas[i].get_weight()

def get_random_nodo(vecinos):
  cant_vecinos = len(vecinos)
  num_random = randint(0,cant_vecinos)
  return vecinos[num_random]
"""
