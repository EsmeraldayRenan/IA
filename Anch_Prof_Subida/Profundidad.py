# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:02:56 2020

@author: jrena
"""

import json
Grafo = False

with open ("arbol.json","r") as read_file:
    data = json.load(read_file)
    Grafo = data['Grafo']

camino=[]
 
def buscar(inicio,valorBuscar):
    camino.append(inicio)
    if inicio==valorBuscar:
        return valorBuscar
    for k,v in Grafo.items():
        if v==inicio:
            resultado=buscar(k,valorBuscar)
            if resultado:
                return resultado
    camino.pop()
resultado=buscar("10","30")

if resultado:
    print("Numero encontrado")
else:
    print("Numero no encontrado")
print(camino)


