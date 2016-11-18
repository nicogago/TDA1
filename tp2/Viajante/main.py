#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                              ###
###   Problema del viajante TSP  ###
###                              ###
import sys
from parser import *
from viajante import *

# Verificación de argumentos (validación)

cant_args = len(sys.argv) - 1
if cant_args != 2:
    print 'Cantidad de argumentos inválidos. Ejecute el siguiente comando:'
    print '> python main.py <vértice> <archivo_de_prueba>'
    quit()

testfile = str(sys.argv[2])

if not '.tsp' in testfile:
    print 'Archivo de prueba en formato inválido.'
    quit()

if str(sys.argv[1]).isdigit() == False:
    print 'Vértice inválido. Ingrese un número no negativo.'
    quit()

vertice_id = int(sys.argv[1])

M = parse(testfile)

viajante(vertice_id, M)
