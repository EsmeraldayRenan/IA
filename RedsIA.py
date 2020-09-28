"""
Created on Fri Sep 25 17:21:25 2020

Integrantes------------------------
HERNANDEZ LUNA JUAN RENAN
MARTINEZ RONQUILLO ESMERALDA
-----------------------------------

"""

conocimientoes = [
        ("Gallo","Es","Vertebrado"),
        ("Gallo","Es","Oviparo"),
        ("Ballena","Es","Mammalia"),
        ("Ballena","Es","Vivipara"),
        ("Oso","Es","Mammalia"),
        ("Oso","Es","Viviparo"),
        ("Tortuga","Es","Sauropsido"),
        ("Tortuga","Es","Oviparo"),
        ("Cocodrilo","Es","Sauropsido"),
        ("Cocodrilo","Es","Oviparo"),
        ("Iguana","Es","Sauropsido"),
        ("Iguana","Es","Oviparo"),
        ("Gato","Es","Mammalia"),
        ("Gato","Es","Viviparo"),
        ("Delfin","Es","Mammalia"),
        ("Delfin","Es","Viviparo"),
        ("Sauropsido","Es","Mammalia"),
        ("Sauropsido","Es","Tetrapodo"),
        ("Mammalia","Es","Tetrapodo"),
        ("Mammalia","Es","Vertebrado"),
        ("Vertebrado","Es","Tetrapodo"),
        ("Vertebrado","Es","Sauropsido"),
]

conocimientotiene = [
        ("Gallo","Tiene","Plumas"),
        ("Ballena","Tiene","Piel"),
        ("Oso","Tiene","Garras"),
        ("Oso","Tiene","Pelo"),
        ("Tortuga","Tiene","Garras"),
        ("Tortuga","Tiene","Escamas"),
        ("Cocodrilo","Tiene","Garras"),
        ("Cocodrilo","Tiene","Escamas"),
        ("Iguana","Tiene","Garras"),
        ("Iguana","Tiene","Escamas"),
        ("Gato","Tiene","Garras"),
        ("Gato","Tiene","Pelo"),
        ("Delfin","Tiene","Piel"),
]

conocimientovive = [
        ("Gallo","Vive","Tierra"),
        ("Ballena","Vive","Agua"),
        ("Oso","Vive","Tierra"),
        ("Tortuga","Vive","Agua"),
        ("Tortuga","Vive","Tierra"),
        ("Cocodrilo","Vive","Agua"),
        ("Cocodrilo","Vive","Tierra"),
        ("Iguana","Vive","Tierra"),
        ("Gato","Vive","Tierra"),
        ("Delfin","Vive","Agua"),
]

def es(A,B,C,CON1):
    r=0
    l=len(CON1)
    while r!=l :
        if CON1[r][0] == A:
            if CON1[r][1] == B:
                if CON1[r][2] ==C:
                    return True
        r+=1
    else:
        return False
    
def tiene(A,B,C,CON2):
    r=0
    l=len(CON2)
    while r!=l :
        if CON2[r][0] == A:
            if CON2[r][1] == B:
                if CON2[r][2] ==C:
                    return True
        r+=1
    else:
        return False
    
def vive(A,B,C,CON3):
    r=0
    l=len(CON3)
    while r!=l :
        if CON3[r][0] == A:
            if CON3[r][1] == B:
                if CON3[r][2] ==C:
                    return True
        r+=1
    else:
        return False

print(es("Cocodrilo","Es","Sauropsido",conocimientoes))
print(es("Tortuga","Es","Mammalia",conocimientoes))
print(tiene("Ballena","Tiene","Piel",conocimientotiene))
print(tiene("Iguana","Tiene","Piel",conocimientotiene))
print(vive("Tortuga","Vive","Agua",conocimientovive))
print(vive("Delfin","Vive","Tiera",conocimientovive))

