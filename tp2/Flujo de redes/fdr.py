#!/usr/bin/python
# -*- coding: utf-8 -*-

from proyecto import *
from especialista import *
from tadgrafo2 import *

def procesoArchivo():
	# SE LEE EL ARCHIVO DE CONFIGURACION INICIAL Y SE DEJA INICIALIZADAS LAS VARIABLES
	#
	# n: se deja la cantidad de areas o especialidades
	# m: son la cantidad de proyectos
	# costo_areas: es un diccionario que tiene como id numero de area y valor su especialista
	# ganancia_req: es un diccionario que tiene como id numero de proy y valor su proyecto
	archivo = open("archivo.txt")
	n = archivo.readline()
	n = n.rstrip('\n')
	n = int(n)
	print n
	m = archivo.readline()
	m = m.rstrip('\n')
	m = int(m)
	print m
	global costo_areas
	costo_areas = []
	global ganancia_req
	ganancia_req = []
	
	linea = archivo.readline()
	i = 0
	while i < n:
		numeros = linea.split(" ")
		nuevaLinea = []	 
		for elem in numeros:
			nuevaLinea.append(int(elem.rstrip('\n'))) 
		especialista = Especialista(nuevaLinea.pop())
		costo_areas.append(especialista)
		linea = archivo.readline()
		i = i + 1
	
	i = 0
	while i < m:
		numeros = linea.split(" ")
		nuevaLinea = []	 
		for elem in numeros:
			nuevaLinea.append(int(elem.rstrip('\n')))
		proyecto = Proyecto(nuevaLinea.pop(0),nuevaLinea)
		ganancia_req.append(proyecto)
		linea = archivo.readline()
		i = i + 1
	
	archivo.close()

def inicializoGrafo():
#el tadgrafo se toma como un modulo cerrado, dada su implementación, y debido a la necesidad de utilizar nombres para
# esclarecer el asunto, se creara un diccionario nodos, con clave = nombre y valor = numeroDeNodo 	
	grafo = Digraph(2+len(costo_areas)+len(ganancia_req))
	global nodos 
	nodos = {} 
	nodos["s"] = 0
	nodos["t"] = grafo.V()-1
	for i in range(0,len(ganancia_req)):
		nodos["proyecto"+ str(i+1)] = i+1
		grafo.add_edge( 0, i+1, ganancia_req[i].get_ganancia())
	for i in range(0,len(costo_areas)):
		numeroDeNodo = i+len(ganancia_req)+1
		nodos["especialista" + str(i+1)] = numeroDeNodo
		grafo.add_edge( numeroDeNodo, nodos["t"], costo_areas[i].get_sueldo_especialista())
	#creo las aristas entre los proyectos y los especialistas
	gananciaMaxima = 0
	for i in ganancia_req:
		gananciaMaxima = gananciaMaxima + i.get_ganancia()
	
	for i in range(0,len(ganancia_req)):
		areas_requeridas = ganancia_req[i].get_areas_requeridas() 
		for j in range(0,len(areas_requeridas)):
			#agrego la gananciaMaxima + 1 para simular infinito
			proyecto = str("proyecto") + str(i+1)
			especialista = "especialista"+ str(j+1)
			peso = gananciaMaxima +1
			grafo.add_edge(nodos[proyecto], nodos[especialista], peso)
	#prueba
	print grafo.V()
	print grafo.E()
	print "aristas de s"
	for i in grafo.adj_e(nodos["s"]):
		print i.get_weight()
	print "aristas de t"
	for i in grafo.adj_e(nodos["t"]):
		print i.get_weight()
	for j in range(1,3):
		print "arista de proyecto"+str(j)
		for i in grafo.adj_e(nodos["proyecto" + str(j)]):
			print i.get_weight()

	for j in range(1,4):
		print "arista de especialista"+str(j)
		for i in grafo.adj_e(nodos["especialista" + str(j)]):
			print i.get_weight()
	return grafo

	"""
	#prueba
	g = Digraph(6)
	g.add_edge(0,1,3)
	g.add_edge(0,2,3)
	g.add_edge(1,2,2)
	g.add_edge(1,3,3)
	g.add_edge(2,4,2)
	g.add_edge(4,5,3)
	g.add_edge(3,4,4)
	g.add_edge(3,5,2)
	print (g.max_flow(0,5))
	#print grafo.max_flow(nodos["s"],nodos["t"])
	"""


