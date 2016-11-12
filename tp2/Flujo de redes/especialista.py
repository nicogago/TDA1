#!/usr/bin/python
# -*- coding: utf-8 -*-

class Especialista:
    def __init__(e,sueldo):
        e.costo = sueldo  
        e.fue_contratado = False
    
    def get_sueldo_especialista (self):
        return self.costo
    
    def contratar(self):
        self.fue_contratado = True

    def tiene_trabajo(self):
        return self.fue_contratado
