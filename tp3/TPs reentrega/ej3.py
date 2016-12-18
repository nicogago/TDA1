#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tareas import *
from Tarea import *
    
t = Tareas(5)
    
for i in range(0,5):
    tarea = Tarea()
    tarea.setFechaLimite(50+i)
    tarea.setGanancia(10*i)
    tarea.setTiempoDeEjec(40/(i+1))
    tarea.setTarea("t" + str(i))
    t.setTarea(tarea, i)
    print i

for i in range(0,5):
    tareita = t.getTarea(i) 
    print "tarea = " + str(tareita.getTarea())
    print "Ganancia = " + str(tareita.getGanancia())
    print "fechalimite = " + str(tareita.getFechaLimite())
    print "tiempoDeEjec = " + str(tareita.getTiempoDeEjec())
    
k = 10
certificado = []
certificado.append(t.getTarea(1))
certificado.append(t.getTarea(2))

print "resultado = " + str(t.verificador_pwd(certificado, k))

values = set([1,2,3,-4])
t2 = Tareas(len(values))
t2.reduce_ss_to_pwd(values)
