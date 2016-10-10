###                          ###
###  ESTADISTICO DE ORDEN K  ###
###                          ###


# En ambas formas, cand es el indice en conj del numero candidato
# Asumiendo minimo k cuando hay repetidos
def fuerza_bruta1(conj, cand, k):
    real_k = 1
    for i in conj:
        if (i < conj[cand]):
            real_k += 1
            if (real_k > k):
                return False
    if (real_k < k):
        return False
    return True

# Sin esa restriccion
def fuerza_bruta2(conj, cand, k):
    min_real_k = 1
    diff_max_k = 0

    for idx, i in enumerate(conj):
        if (i < conj[cand]):
            min_real_k += 1
            if (min_real_k > k):
                return False
        elif (i == conj[cand] and idx != cand):
            diff_max_k += 1
    if (min_real_k + diff_max_k < k):
        return False
    return True


def ordenar_y_seleccionar(conj, k):
    conj.sort()
    return conj[k-1]

## K SELECCIONES
# k > 0
def k_selecciones(array, k):
    for i in range(0, k):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        if i != min:
            array[i] , array[min] = array[min] , array[i]
    return array[k-1]


# Para heapificar
def moveDown(conj, actual, last):
    hijo = 2 * actual + 1
    while (hijo <= last):
        if (hijo < last and conj[hijo] > conj[hijo + 1]):
            hijo += 1
        if (conj[actual] > conj[hijo]):
            conj[actual], conj[hijo] = conj[hijo], conj[actual]
            actual = hijo
            hijo = 2 * actual + 1
        else:
            return


def k_heapsort(array, k):
    last = len(array)
    for i in xrange(0, k):
        last -= 1
        #heapifico
        for j in xrange(last // 2, -1, -1):
            moveDown(array, j, last)
        if i != (k-1):
            array[0], array[last] = array[last], array[0]
    return array[0]


# k >= 1
def heapselect(conj, k):
    last = len(conj) - 1
    # heapifico
    for i in xrange(last // 2, 0-1, -1):
        moveDown(conj, i, last)
    limit = last - k + 1
    for i in xrange(last, limit, -1):
        if (conj[0] < conj[i]):
            conj[0], conj[i] = conj[i], conj[0]
            moveDown(conj, 0, i - 1)
    return conj[0]

## QUICKSELECT
# Funcion para encontrar pivote para luego particionar el arreglo
def particionar(array, ini, fin, k):
    i = ini - 1
    for j in range(ini, fin):
        if (array[j] < array[fin]):
            i += 1
            if (i != j):
                array[i], array[j] = array[j], array[i]
    # i+1 se va a convertir en el pivote (swap)
    array[i+1], array[fin] = array[fin], array[i+1]
    return i + 1

def quickSelect(array, ini, fin, k):
    if (ini == fin):
        return array[k]
    # descartamos el subarray que no contiene al elemento k
    pivote = particionar(array, ini, fin, k)
#    print array
#    print "pivote: ", pivote
    if (k == pivote):
        return array[k]
    if (k > pivote):
        ini = pivote + 1
    else:
        fin = pivote - 1
    return quickSelect(array, ini, fin, k)
