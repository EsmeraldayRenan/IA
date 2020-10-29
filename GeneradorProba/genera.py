"""
En el comentario del archivo anterior, hice varias cosas, 
para poder sacar la matriz de probabilidades, 
ahora hay que hacer un programa que a partir de 10 tweets genere la misma 
matriz de probabilidades
sabiendo de ante mano cuales son los de stream
Sugiero esta estructura, para lo tweets
{
    "Tweets" : [
        {"Stream":true, "texto":"Vamos a darle a Among Us con famosos"},
        {"Stream":false, "texto":"El Fugitivo: La Historia en 1 Video"},
    ]
}
y debe generar el  json compatible con el programa de clasificacion
"""
"""
Integrantes:
    Hernandez Luna Juan Renan
    Martinez Ronquillo Esmeralda
"""

import json
conocimiento = False

with open("tweet.json","r") as read_file:
    data = json.load(read_file)
    conocimiento = data['Tweets']

excluir = ['¿', '?', '¡', '!', '-', '+', ',', ':', ';','Así', 'más','Cuando', 'te','si','Que','Vez', 'de', 'con','ni', 'sin','a', 'X', 'asi',
          'es', 'Hoy','Es', 'más', 'y', 'al','el','Todo', 'hoy',  '0', '1', '2', '3','4','5', '6', '7', '8', '9']

def probabilidad(mAt):
    i = 0
    datos = {}
    datos["Probabilidades"] = []
    while i < len(mAt):
        datos["Probabilidades"].append([mAt[i][0],mAt[i][4]])
        i = i + 1
    with open('base_fedelobo.json', 'w') as file:
        json.dump(datos, file, indent=1)
    return ("Archivo base_fedelobo.json creado con exito")

def matriz(conocimiento,palabra,ntweet):
    i = 0
    siAparece = 0
    noAparece = 0
    m = []
    print("La matriz de probabilidad es:")
    while i < len(palabra):
        j = 0
        while j < len(conocimiento):
            if conocimiento[j] == palabra[i]:
                siAparece = siAparece + 1
            noAparece = ntweet - siAparece
            j = j + 1
        total = siAparece + noAparece
        m.append([palabra[i], noAparece, siAparece, total, siAparece/total, noAparece/total])
        siAparece = 0
        noAparece = 0
        i=i + 1
    print(m)
    return probabilidad(m)

def exclusiones(con,excluir):
    j = 0
    k = []
    C = []
    while j < len(con):
        i = 0
        while i < len(con[j]):
            if not con[j][i] in excluir:
                s = con[j][i]
                k = k + [s]
            i = i + 1
        j = j + 1
    j = 0
    while j < len(k):
        if not k[j] in C:
            C = C + [k[j]]
        j = j + 1 
    return matriz(k,C, len(con))

def separar(conocimiento,excluir,t = []):
    i = 0
    while i < len(conocimiento):
        tw = conocimiento[i]
        Stream = tw['Stream']
        texto = tw['texto']
        if Stream == True:
            texto = texto.split()
            t = t + [texto]
        i = i +1
    return exclusiones(t,excluir)

print(separar(conocimiento,excluir))