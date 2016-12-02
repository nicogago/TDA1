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

##############################################
def testing(N):
    # Valores reducidos
    #e = 0.1
    #b = (e / (2 * N)) * max(av)
    b = 10
    print "e: ", b * (2*N) / max(av)
    print max(av), b, N, len(av)
    ava = [int(math.ceil(v/b)) for v in av]
    print av
    print ava


def knapsack_approx(N, W):
    # Valores reducidos
    #e = 0.1
    #b = (e / (2 * N)) * max(av)
    b = 10
    ava = [int(math.ceil(v/b)) for v in av]

    V = sum(ava)
    M = [[0 for p in xrange(V+1)] for p in xrange(N+1)]
    print "N =", N, "V =", V, "size M =", (V+1)*(N*1), "\t",
    sys.stdout.flush()
    #time.sleep(20)

    def P(i, v, suma_parcial):
        if i <= 0 or v == 0:
            return 0
        if v > suma_parcial:
            return aw[i] + M[i-1][max(0,v-ava[i])]
        return min( M[i-1][v], aw[i] + M[i-1][max(0,v-ava[i])] )
    # Algo que hacer para considerar elementos aw[i] > W?

    for i in xrange(1, N+1):
        suma_parcial = sum(ava[1:i-1])
        for v in xrange(1, suma_parcial + ava[i]):
            #print "i", i, ", v", v, ", sp", suma_parcial
            M[i][v] = P(i, v, suma_parcial)

    for v in reversed(xrange(V+1)):
        print v##
        if M[N][v] <= W:
            print "M[N][v] =", M[N][v], "W =", W, "v =", v,
            return v



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
                        print "hay casos wi > W"
                reader.next()  # Ignora línea vacía tras cada test

                V = sum(av)
                print test_name, '\t',# "N*V =", (N+1) * (V+1), "\t ",
                sys.stdout.flush()
                start = time.clock()

                print z
                k = knapsack_approx(N, W)
                print k
                #exit(0)

                elapsed = time.clock() - start

                print "best: ", z, "\tapprox: ", k, "\t",

                print elapsed, "s\t(vs", t, "s)\t",
                print "t / N*W =", elapsed / ((N+1) * (W+1))

        except StopIteration:
            print "----- eof -----"
            print
