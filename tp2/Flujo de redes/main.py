#!/usr/bin/python
# -*- coding: utf-8 -*-

from fdr import *

procesoArchivo()
grafo = inicializoGrafo()
print "flujo maximo = " + str(grafo.fordFulkerson(0,grafo.V()-1))
print "corte minimo = " + str(grafo.minimalCut(0))