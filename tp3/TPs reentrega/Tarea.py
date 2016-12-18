#!/usr/bin/python
# -*- coding: utf-8 -*-

class Tarea():
    #se toma la fecha como un entero, asumiendo que ya fue pasada desde la fecha de inicio
    #ej: si la fecha de inicio es el 12/12, y la fecha limite el 24/12, se pondra como fecha limite 12
    def __init__(self):
        self.id =""
        self.tiempoDeEjec = None
        self.fechaLimite = None
        self.ganancia = None
    
    def setTarea(self, tarea):
        self.tarea = tarea
    def getTarea(self):
        return self.tarea
    
    def setTiempoDeEjec(self, tiempoDeEjec):
        self.tiempoDeEjec = tiempoDeEjec
    def getTiempoDeEjec(self):
        return self.tiempoDeEjec
    
    def setFechaLimite(self, fechaLimite):
        self.fechaLimite = fechaLimite
        
    def getFechaLimite(self):
        return self.fechaLimite

    def setGanancia(self, ganancia):
        self.ganancia = ganancia
    def getGanancia(self):
        return self.ganancia
    