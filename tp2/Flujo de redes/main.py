#!/usr/bin/python
# -*- coding: utf-8 -*-

from fdr import *

procesoArchivo()
grafo = inicializoGrafo()
grafo.fordFulkerson(0,grafo.V()-1)