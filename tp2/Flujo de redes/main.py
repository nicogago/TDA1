#!/usr/bin/python
# -*- coding: utf-8 -*-

from fdr import *

procesoArchivo()
grafo = inicializoGrafo()
print grafo.fordFulkerson(0,grafo.V()-1)