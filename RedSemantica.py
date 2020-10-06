# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:35:01 2020

Integrantes:
    
    Hernandez Luna Juan Renan
    Martinez Ronquillo Esmeralda

@author: jrena
"""

import json
Conocimiento = False

with open("base.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']

def es(A, B,C, CON):
    r = 0
    l = len(CON)
    while r != l:
        if CON[r][0] == A:
            if CON[r][1] == B:
                if CON[r][2] == C:
                    return True
        r += 1
    else:
        return False

def tiene(A,B,C,CON1):
   return es(A,B,C,CON1)

def vive(A, B, C, CON2):
    return es(A,B,C, CON2)

def es_un(A,B,C):
    return es(A,B,C,Conocimiento)

def tiene_car(A,B,C):
    return tiene(A,B,C,Conocimiento)

def vive_en(A,B,C):
    return vive(A,B,C,Conocimiento)

def main():
    print("Bienvenido a este programa")
    print('Puedes consultar escribiendo tiene_car("<Animal>","<Tiene>","<Caracteristica>")')
    print('Puedes consultar escribiendo vive_en("<Animal>","Vive","<Tierra/Agua>")') 
    print('Puedes consultar escribiendo es_un("<Animal/Clase>","Es","<Clase>")')
    print("Para salir presiona q o escribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)

if __name__ == '__main__':
    main()
