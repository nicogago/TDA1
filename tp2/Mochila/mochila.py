#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                          ###
###  Problema de la mochila  ###
###                          ###
import csv

# a: array, p: profit, v: value, w: weight

# Sin programación dinámica
def P_dull(i,w,aw,av):
    if i < 0:
        return 0
    if w < aw[i]:
        return P_dull(i-1,w,aw,av)
    return max( P_dull(i-1, w, aw, av),  P_dull(i-1, w-aw[i], aw, av) + av[i] )


weight_list = [1,2,3,4]
values_list = [4,3,2,1]
print P_dull(3,8,weight_list,values_list)

with open('smallcoeff_pisinger/knapPI_9_50_1000.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    seguir = True

    try:    # Medio feo pero sirve
        while (seguir):
            test_name = reader.next()[0]
            N = reader.next()[1]
            W = reader.next()[1]
            z = reader.next()[1]
            t = reader.next()[1]
            vl = []
            wl = []
            xl = []
            for row in reader:
                if "--" in row[0]:
                    break
                (i, vi, wi, xi) = map(int, row[0].split(','))
                vl.append(vi)
                wl.append(wi)
                xl.append(xi)
            print test_name, N, W, z, t
            reader.next()

            # P()

    except StopIteration:
        print "-----"
