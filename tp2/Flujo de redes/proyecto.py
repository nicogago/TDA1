#!/usr/bin/python
# -*- coding: utf-8 -*-

class Proyecto:
    def __init__(p,ganancia,areas_requeridas):  
        p.ganancia = ganancia
        p.areas_requeridas = areas_requeridas
        p.realizar_proyecto = False

    def contratar (self):
        self.realizar_proyecto = True

    def no_contratar(self):
        self.realizar_proyecto = False    

    def fue_contratado(self):
        return self.realizar_proyecto

    def get_ganancia(self):
        return self.ganancia

    def get_areas_requeridas(self):
        return self.areas_requeridas
