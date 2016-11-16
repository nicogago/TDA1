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
	global grafo
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

	"""
	def fordFulkerson(s="s",t="t"):
		path = find_path(s, t, [])
		residual = []
		while path != None:
			for i in range(0,len(path)):
				aristasAdyacentes = grafo.adj_e(path[i])
				for arista in aristasAdyacentes:
					if path[i+1] == arista.get_to():
						residual.append(arista.get_weight())
			flujo = min(residual)
			for i in range(0,len(path)):
				aristasAdyacentes = grafo.adj_e(path[i])
				for arista in aristasAdyacentes:
					if path[i+1] == arista.get_to():
						arista.set_weight(arista.get_weight()-flujo)
						path = find_path(s, t, [])
	"""
	#prueba
	print grafo.max_flow(nodos["s"],nodos["t"])
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


"""	
def find_path( s, t, path):
	if s == t:
		return path
	resultado = None
	for e in grafo.adj_e(s):
		residual = s.get_weight(e) 
		if residual > 0 and e not in path:
			resultado = find_path( e.get_to(), t, path + [e]) 
			if resultado != None:
				return resultado
"""	
	
# Se imprimen los seteos inicializados, prueba.
"""
key_costo_areas = costo_areas.keys()
for area in costo_areas:
	#print area
	esp = costo_areas[area]
	print esp.get_sueldo_especialista()


key_ganancias_req = ganancia_req.keys()
for proy in ganancia_req:
	#print proy
	proy = ganancia_req[proy]
	print proy.get_ganancia()
	print proy.get_areas_requeridas()
"""

# Se define la ganancia de una desicion tomada

"""def ganancia():
	sueldos_especialistas = 0
	for area in costo_areas:
		esp = costo_areas[area]
		if esp.tiene_trabajo():
			sueldos_especialistas = sueldos_especialistas + esp.get_sueldo_especialista()
	ganancia_proy = 0
	print sueldos_especialistas
	for proy in ganancia_req:
		proy = ganancia_req[proy]
		if proy.fue_contratado():
			ganancia_proy = ganancia_proy + proy.get_ganancia()
	return (ganancia_proy - sueldos_especialistas)
(como no se si sirve por ahora lo comento esto!!!!!!!!!!!!!!!!!!!!)
"""

# prueba de la desicion tomada

"""
costo_areas[3].contratar()
ganancia_req[2].contratar()
print ganancia()
"""

