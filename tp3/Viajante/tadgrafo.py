#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    def set_distancia_inf(self):
        self.distancia = POSITIVE_INFINITY

    def set_padre_vacio(self):
        self.padre = None

    def get_distancia(self):
        return self.distancia

    def get_padre(self):
        return self.padre


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
        return aristas_incidentes_de_v



    def adj(g, v):  # @NoSelf
        """Itera sobre los vértices adyacentes a ‘v’.
        """
        return g.vertices[v].get_neighbors().keys()


    def add_edge(g, u, v, weight=0):    # @NoSelf
        """Añade una arista al grafo.
        """
        g.vertices[u].add_neighbor(g.vertices[v],weight)
        new_edge = Arista(u,v,weight)
        g.aristas.append(new_edge)


    def __iter__(g):    # @NoSelf
        """Itera de 0 a V."""
        return g.vertices

    def getVertices(g): #@NoSelf
        return g.vertices

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
        for i in range(0,len(g.vertices)):
            g.vertices[i].setear_no_visitado()

    def poner_distancias_inf(g): # @NoSelf
        for i in range(0,len(g.vertices)):
            g.vertices[i].set_distancia_inf()

    def eliminar_padres(g): # @NoSelf
        for i in range(0,len(g.vertices)):
            g.vertices[i].set_padre_vacio()

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
