#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

# def matriz_ceros(N):
#     return [[0 for i in xrange(N)] for i in xrange(N)]

'''
Secciones de los archivos de ejemplo
'NAME'
'TYPE'
'DIMENSION'
'EDGE_WEIGHT_TYPE'
'EDGE_WEIGHT_FORMAT'
'NODE_COORD_TYPE'
'DISPLAY_DATA_TYPE'
'TOUR_SECTION'
'''

filename = "p01.tsp"
#filename = "fri26.tsp"
# Para probar att48_d.txt, metelo en un archivo con DIMENSION
# y EDGE_WEIGHT_FORMAT setteados, la 2da a FULL_MATRIX, y la
# etiqueta EDGE_WEIGHT_SECTION antes de la matriz.

dicc = {}
tour_section = []
matriz = []

with open(filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    for linea in reader:
        #print linea #
        if (linea[0] == 'EOF'):
            break
        elif (linea[0] == 'TOUR_SECTION'):
            for i in xrange(int(dicc['DIMENSION']) + 2): #ema revisar
                 linea = reader.next()
                 tour_section.append(int(linea[-1]))
        elif (linea[0] == 'EDGE_WEIGHT_SECTION'):
            matriz = []
            if (dicc['EDGE_WEIGHT_FORMAT'] == 'FULL_MATRIX'):
                for i in xrange(int(dicc['DIMENSION'])):
                    linea = reader.next()
                    matriz.append(map(int, filter(lambda x: x != '', linea)))
            elif (dicc['EDGE_WEIGHT_FORMAT'] == 'LOWER_DIAG_ROW'):
                for i_fila in xrange(int(dicc['DIMENSION'])):
                    fila = []
                    for i_col in xrange(i_fila + 1):
                        linea = reader.next()
                        fila.append(int(linea[0]))
                    #for aux in xrange(i_fila + 1, int(dicc['DIMENSION'])):
                    #    fila.append(0)
                    matriz.append(fila)
                # Faltaría espejar la matriz si es necesario
        else:
            dicc[linea[0].split(":")[0]] = " ".join(
                                    filter(lambda x: x != ':', linea[1::]))

print dicc
print
print tour_section
print
#print matrix
for i in xrange(int(dicc['DIMENSION'])):
    print matriz[i]
print
