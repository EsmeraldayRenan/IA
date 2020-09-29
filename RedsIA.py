"""
Created on Fri Sep 25 17:21:25 2020

Integrantes------------------------
HERNANDEZ LUNA JUAN RENAN
MARTINEZ RONQUILLO ESMERALDA
-----------------------------------

"""

conocimientoes = [
        ("Gallo","Vertebrado"),
        ("Gallo","Oviparo"),
        ("Ballena","Mammalia"),
        ("Ballena","Vivipara"),
        ("Oso","Mammalia"),
        ("Oso","Viviparo"),
        ("Tortuga","Sauropsido"),
        ("Tortuga","Oviparo"),
        ("Cocodrilo","Sauropsido"),
        ("Cocodrilo","Oviparo"),
        ("Iguana","Sauropsido"),
        ("Iguana","Oviparo"),
        ("Gato","Mammalia"),
        ("Gato","Viviparo"),
        ("Delfin","Mammalia"),
        ("Delfin","Viviparo"),
        ("Sauropsido","Mammalia"),
        ("Sauropsido","Tetrapodo"),
        ("Mammalia","Tetrapodo"),
        ("Mammalia","Vertebrado"),
        ("Vertebrado","Tetrapodo"),
        ("Vertebrado","Sauropsido"),
]

conocimientotiene = [
        ("Gallo","Plumas"),
        ("Ballena","Piel"),
        ("Oso","Garras"),
        ("Oso","Pelo"),
        ("Tortuga","Garras"),
        ("Tortuga","Escamas"),
        ("Cocodrilo","Garras"),
        ("Cocodrilo","Escamas"),
        ("Iguana","Garras"),
        ("Iguana","Escamas"),
        ("Gato","Garras"),
        ("Gato","Pelo"),
        ("Delfin","Piel"),
]

conocimientovive = [
        ("Gallo","Tierra"),
        ("Ballena","Agua"),
        ("Oso","Tierra"),
        ("Tortuga","Agua"),
        ("Tortuga","Tierra"),
        ("Cocodrilo","Agua"),
        ("Cocodrilo","Tierra"),
        ("Iguana","Tierra"),
        ("Gato","Tierra"),
        ("Delfin","Agua"),
]

def es(A,B,CON1):
    r=0
    l=len(CON1)
    while r!=l :
        if CON1[r][0] == A:
            if CON1[r][1] == B:
                return True
        r+=1
    else:
        return False
    
def tiene(A,B,CON2):
    r=0
    l=len(CON2)
    while r!=l :
        if CON2[r][0] == A:
            if CON2[r][1] == B:
                return True
        r+=1
    else:
        return False
    
def vive(A,B,CON3):
    r=0
    l=len(CON3)
    while r!=l :
        if CON3[r][0] == A:
            if CON3[r][1] == B:
                return True
        r+=1
    else:
        return False

print(es("Cocodrilo","Sauropsido",conocimientoes))
print(es("Tortuga","Mammalia",conocimientoes))
print(tiene("Ballena","Piel",conocimientotiene))
print(tiene("Iguana","Piel",conocimientotiene))
print(vive("Tortuga","Agua",conocimientovive))
print(vive("Delfin","Tiera",conocimientovive))

