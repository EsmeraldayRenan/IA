# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:35:10 2020


"""

"""
Integrantes:
    Juan Renan Hernandez Luna
    Esmeralda Martinez Ronquillo
"""

import json

with open ("tableroGrafo.json","r") as read_file:
    data = json.load(read_file)
    tabI= data['TableroI']
    tabF= data['TableroF']
    grafo= data['Grafo']
    

caba = [[0,1],[2,1],[6,-1],[8,-1]]
cabaf = [[0,-1],[2,-1],[6,1],[8,1]]

resul = [
	["0","0","0"],
	["0","0","0"],
	["0","0","0"]
    ]

m=[]
n=[]
a=0
e=-1
z=0

def caballo (caba,a,z):
    m=[]
    if caba == cabaf:
        return True
    else:
        for i in range(len(caba)):
            for j in range(len(grafo)):
                if caba[i][0]==grafo[j][0]:
                    m.append(grafo[j][a])
        for k in range(len(caba)):
            caba[k][0]=m[k]
        caba.sort()
        z=z+1
        print()
        print ("Estado #",z,":", caba)
        print()
    return caballo(caba,a,z)

def mostrar (e,resul,caba):
    for i in range(len(caba)):
        n=caba[i]
        e=-1    
        for j in range (len(resul)):
            for k in range(len(resul[j])):
                e=e+1
                if e ==n [0]:
                    resul[j][k]= n[1]
    print ("Tablero final:")
    print()
    for fila in resul:
        for valor in fila:
            print("\t", valor, end="")
        print()

def mostrar1 (tabI):
    print ("Estado inicial", caba)
    print()
    print ("Tablero inicial:")
    print()
    for fila in tabI:
        for valor in fila:
            print("\t", valor, end="")
        print()
    
        
a=1
a = int(input("Eliga la direccion en la que se hara el recorrido: Hacia la derecha (1), Hacia la izquierda (2): "))
print()
mostrar1(tabI)
caballo(caba,a,z)          
mostrar(e,resul,caba)  


                
        
