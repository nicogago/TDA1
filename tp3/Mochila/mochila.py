#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                          ###
###  Problema de la mochila  ###
###     ...aproximado        ###
import sys
import csv
import time
import math
from os import listdir
from os.path import isfile, join

def knapsack_approx(N, W):
    # Valores reducidos
    e = 0.1
    b = (e / (2 * N)) * max(av)
    # Valor artificial para limitar M
    # de forma que mi computadora no explote
    b_max = sum(av) * N / 100000000
    b = max([b, b_max])
    if b < 1:
        b = 1
    e = b * (2 * N) / max(av)

    ava = [int(math.ceil(v/b)) for v in av]
    V = sum(ava)
    print "b =", b, "| e =", e, "|",
    print "V~ =", V, "| s(M) =", (N+1)*(V+1), "\t",
    sys.stdout.flush()

    M = [[0 for p in xrange(V+1)] for p in xrange(N+1)]

    def P(i, v, suma_anteriores):
        if v <= 0:
            return 0
        if i == 0:
            return W+1  # representa infinito
        if v > suma_anteriores:
            return aw[i] + M[i-1][max(0,v-ava[i])]
        return min( M[i-1][v], aw[i] + M[i-1][max(0,v-ava[i])] )

    for i in xrange(1, N+1):
        suma_hasta_anterior = sum(ava[1:i-1])
        for v in xrange(1, suma_hasta_anterior + ava[i]):
            M[i][v] = P(i, v, suma_hasta_anterior)

    for v in reversed(xrange(V+1)):
        if M[N][v] <= W:
            sol = b*v
            if not 0 < sol <= (1 + e) * z:
                print "No!\t",
            return sol


dirname = "smallcoeff_pisinger"
#dirname = "hardinstances_pisinger"

files = [f for f in listdir(dirname) if isfile(join(dirname, f))]
for filename in files:
    if ".csv" not in filename:
        continue

    with open(join(dirname, filename)) as csvfile:
        print "---------------"
        print filename
        print
        reader = csv.reader(csvfile, delimiter=' ')
        seguir = True

        try:
            while (seguir):
                test_name = reader.next()[0]
                N = int(reader.next()[1])
                W = int(reader.next()[1])
                z = int(reader.next()[1])
                t = float(reader.next()[1])
                av = [0]
                aw = [0]
                xl = [0]
                for row in reader:
                    if "--" in row[0]:
                        break
                    (i, vi, wi, xi) = map(int, row[0].split(','))
                    av.append(vi)
                    aw.append(wi)
                    xl.append(xi)
                    if wi > W:
                        print "hay casos wi > W" ##
                reader.next()  # Ignora línea vacía tras cada test

                V = sum(av)
                print test_name, '\t', "N*V =", (N+1) * (V+1), "\t",
                sys.stdout.flush()
                start = time.clock()

                k = knapsack_approx(N, W)

                elapsed = time.clock() - start
                print "approx =", k, "| expect =", z, "| app/exp=", k/z, "\t",
                print elapsed, "s\t(vs", t, "s)\t"

        except StopIteration:
            print "----- eof -----"
            print
