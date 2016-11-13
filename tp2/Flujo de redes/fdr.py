#!/usr/bin/python
# -*- coding: utf-8 -*-

from proyecto import *
from especialista import *
from tadgrafo import *

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
	
	"""	
	grafo = Digraph(2+len(costo_areas)+len(ganancia_req))
	nodos = {} 
	nodos[0] = "s"
	for i in range(0,len(ganancia_req)):
		nombres.append("proyecto"+ str(i+1))
		nodos[i]
		grafo.add_edge( 0, i+1, ganancia_req[i].get_ganancia())
	for i in range(0,len(costo_areas)):
		nombres.append("especialista" + str(i+1))
		grafo.add_edge( i+len(ganancia_req)+1, grafo.V()-1, costo_areas[i].get_sueldo_especialista())
	nombres.append("t")
	grafo.changeNames(nombres)
	#creo las aristas entre los proyectos y los especialistas
	gananciaMaxima = 0
	for i in ganancia_req:
		gananciaMaxima = gananciaMaxima + i.get_ganancia()
	
	for i in ganancia_req:
		areas_requeridas = i.get_areas_requeridas() 
		for j in areas_requeridas:
			#agrego la gananciaMaxima + 1 para simular infinito
			aaa="proyecto"+str(i)
			bbb= gananciaMaxima +1
			grafo.add_edge(aaa, "especialista"+areas_requeridas[j],str(bbb))
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

