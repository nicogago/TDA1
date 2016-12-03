#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from tadCaminos import *
from constantes import *
from collections import defaultdict

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
    
    def __repr__(self):
        return "%s->%s:%s" % (self.src, self.dst, self.weight)

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

        g.adj = defaultdict(list)
        g.flow = {}

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

        arista = Arista(u,v,weight)
        reversa_arista = Arista(v,u,0)
        arista.reversa_arista = reversa_arista
        reversa_arista.reversa_arista = arista
        g.adj[u].append(arista)
        g.adj[v].append(reversa_arista)
        g.flow[arista] = 0
        g.flow[reversa_arista] = 0
 

    def __iter__(g):    # @NoSelf
        """Itera de 0 a V."""
        return g.vertices
    
    def get_V(g,v): # @NoSelf
        return g.vertices[v]
    
    def get_A(self, src, dst):
        for i in range(0,len(self.aristas)):
            arista = self.aristas[i]
            if (arista.get_from() == src ) and (arista.get_to() == dst) : 
                return arista
        return None

    def get_A_Adj(g, v):
        return g.adj[v]

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

    def find_path(g, src, dst, path, scalingFactor): # @NoSelf
        if src == dst:
            return path
        for arista in g.get_A_Adj(src):
            residual = arista.weight - g.flow[arista]
            if residual > 0 and arista not in path:
                result = g.find_path( arista.dst, dst, path + [arista], scalingFactor) 
                if result != None:
                    return result

    def fordFulkerson(g, src, dst): # @NoSelf
        scalingFactor = g.getScalingFactor()
        while scalingFactor >= 1:
            path = g.find_path(src, dst, [],scalingFactor)
            while path != None:
                residuals = [arista.weight - g.flow[arista] for arista in path]
                flow = min(residuals)
                for arista in path:
                    g.flow[arista] += flow
                    g.flow[arista.reversa_arista] -= flow
                path = g.find_path(src, dst, [], scalingFactor)
            scalingFactor = scalingFactor/2
        print g.flow
        return sum(g.flow[arista] for arista in g.get_A_Adj(src))
        
        """        path = g.find_path(src, dst, [],scalingFactor)
        while path != None:
            residuals = [arista.weight - g.flow[arista] for arista in path]
            flow = min(residuals)
            for arista in path:
                g.flow[arista] += flow
                g.flow[arista.reversa_arista] -= flow
            path = g.find_path(src, dst, [], scalingFactor)
        print g.flow
        return sum(g.flow[arista] for arista in g.get_A_Adj(src))"""
    
    def minimalCut(self, src):
        visited = set()
        nodosARecorrer = [src]
        resultado = []
        while nodosARecorrer:
            nodo = nodosARecorrer.pop()
            if nodo not in visited: 
                visited.add(nodo)
                for arista in self.get_A_Adj(nodo):  
                    destino = arista.dst
                    if destino not in visited and arista.weight - self.flow[arista] <>0 :
                        resultado.append(destino)
                        nodosARecorrer.append(destino)
            
        return resultado

    def getScalingFactor(self):
        print "ohhh plis killl meee !"
        maxArray = 0
        for i in self.iter_edges():
            if i.get_weight() > maxArray:
                maxArray = i.get_weight()
        resultado = 2
        while resultado < maxArray:
            resultado = resultado * 2
        print resultado/2
        return resultado/2

