#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                          ###
###  Problema de la mochila  ###
###                          ###
import csv
import time
from os import listdir
from os.path import isfile, join

# a: array, p: profit, v: value, w: weight

# Sin programación dinámica
def P_dull(i, w):
    if i < 0:
        return 0
    if aw[i] > w:
        return P_dull(i-1,w)
    return max( P_dull(i-1, w),  P_dull(i-1, w-aw[i]) + av[i] )

def knapsack_dull(N, W):
    return P_dull(N, W)


def knapsack(N, W):
    M = [[0 for p in xrange(W+1)] for p in xrange(N+1)]

    def P(i, w):
        if i <= 0 or w == 0:
            return 0
        if aw[i] > w:
            return M[i-1][w]
        return max( M[i-1][w], M[i-1][w-aw[i]] + av[i] )

    for i in xrange(1, N+1):
        for w in xrange(1, W+1):
            M[i][w] = P(i, w)
    return M[N][W]


dirname = "smallcoeff_pisinger"
# dirname = "hardinstances_pisinger"

files = [f for f in listdir(dirname) if isfile(join(dirname, f))]
for filename in files:
    if ".csv" not in filename:
       continue

    with open(join(dirname, filename)) as csvfile:
        print "--------------"
        print filename
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
                reader.next()  # Ignora línea vacía tras cada test

                print test_name, '\t', "size(M) =", (N+1)*(W+1), '\t',
                start = time.clock()

                k = knapsack(N, W)

                elapsed = time.clock() - start

                if k != z:
                    print
                    print k, "!=", z, "!!!"
                    assert k == z

                print elapsed, "s\t(vs", t, "s)"

        except StopIteration:
            print "--- passed ---"
            print
