#!/usr/bin/python
# -*- coding: utf-8 -*-

from proyecto import *
from especialista import *


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
costo_areas = {}
ganancia_req = {}

linea = archivo.readline()
i = 0
while i < n:
	numeros = linea.split(" ")
	nuevaLinea = []	 
	for elem in numeros:
		nuevaLinea.append(int(elem.rstrip('\n'))) 
	especialista = Especialista(nuevaLinea.pop())
	costo_areas[i+1] = especialista
	linea = archivo.readline()
	i = i + 1

i = 0
while i < m:
	numeros = linea.split(" ")
	nuevaLinea = []	 
	for elem in numeros:
		nuevaLinea.append(int(elem.rstrip('\n')))
	proyecto = Proyecto(nuevaLinea.pop(0),nuevaLinea)
	ganancia_req[i+1] = proyecto
	linea = archivo.readline()
	i = i + 1

archivo.close()

# FIN DE PROCESAMIENTO DEL ARCHIVO INICIAL


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

def ganancia():
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

# prueba de la desicion tomada

"""
costo_areas[3].contratar()
ganancia_req[2].contratar()
print ganancia()
"""

