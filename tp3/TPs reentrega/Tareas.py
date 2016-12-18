#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tareas():
    def __init__(self,cantDeTareas):
        self.listaTareas =[] 
        for i in range(0,cantDeTareas):
            self.listaTareas.append(None)
    
    def getTarea(self,i):
        return self.listaTareas[i]
    
    def setTarea(self, tarea, i):
        self.listaTareas[i] = tarea
        
    def verificador_pwd(self, certificado, k):
        resultado = 0
        fecha = 0
        for i in range(0, len(certificado)):
            t = certificado[i]
            if (fecha + t.getTiempoDeEjec()) < t.getFechaLimite():
                resultado = resultado + t.getGanancia()
            
            
        if resultado >= k : return True
        return False
    #es claramente polinomial, ya que al recorrer el for tenemos O(n), con n = len(certificado)

    def reduce_ss_to_pwd(self,values):
        for i in range(0,len(values)):
            t = Tarea()
            t.setTarea("t"+str(i))
            t.setGanancia(values[i])
            t.setFechaLimite(1)
            t.setTiempoDeEjec(0)
        return self
        
    