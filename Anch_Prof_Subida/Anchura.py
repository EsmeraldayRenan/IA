# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:39:14 2020

@author: jrena
"""

import json
Grafo = False

with open ("arbol.json","r") as read_file:
    data = json.load(read_file)
    Grafo = data['Grafo']

camino=[]
cola=[]
 
def buscar(inicio,valorBuscar,iteraciones):
    camino.append(inicio)
    if inicio==valorBuscar:
        return (True,iteraciones)
    agreCola(inicio)
    if len(cola)==0:
        return (False,iteraciones)
    return buscar(cola.pop(0),valorBuscar,iteraciones+1)

def agreCola(inicio):
    for k,v in Grafo.items():
        if v==inicio:
            cola.append(k)
 
resultado,iteraciones=buscar("10","161",1)

if resultado:
    print("Numero encontrado")
else:
    print("Numero no encontrado")
    
print(camino)