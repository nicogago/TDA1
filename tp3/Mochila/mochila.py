#!/usr/bin/env python
# -*- coding: utf-8 -*-
###                          ###
###  Problema de la mochila  ###
###     ...aproximado        ###


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
                reader.next()  # Ignora línea vacía tras cada test

                print test_name, '\t', "N*W =", (N+1) * (W+1), "\t ",
                sys.stdout.flush()
                start = time.clock()

                k = knapsack(N, W)

                elapsed = time.clock() - start

                print "best: ", z, "\tapprox: ", k, "\t",

                print elapsed, "s\t(vs", t, "s)\t",
                print "t / N*W =", elapsed / ((N+1) * (W+1))

        except StopIteration:
            print "----- eof -----"
            print
