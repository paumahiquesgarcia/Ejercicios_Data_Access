import os

def abrirfichero (nombrefichero,lecturaescritura):
    ruta_base = os.path.dirname(__file__)
    ruta_a_recurs = os.path.join(ruta_base, nombrefichero)
    return open(ruta_a_recurs,lecturaescritura)

f = abrirfichero('operacions.txt','r')
g = abrirfichero('resultats.txt','w')

lista = f.read().splitlines()
lista2 = list(map(lambda x: eval(x),lista))

for i in range(0,len(lista)):
    g.write(lista[i]+' = '+ str(lista2[i])+'\n')
    
f.close()
g.close()