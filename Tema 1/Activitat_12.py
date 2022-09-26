import os
import sys

def abrirfichero (nombrefichero,lecturaescritura):
    ruta_base = os.path.dirname(__file__)
    ruta_a_recurs = os.path.join(ruta_base, nombrefichero)
    return open(ruta_a_recurs,lecturaescritura)

try:
    f = abrirfichero('operacions.txt','r')
    g = abrirfichero('resultats.txt','w')
    pass
except FileNotFoundError:
    print('El fichero pasado por argumento no existe')
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

lista = f.read().splitlines()
try:
    lista2 = list(map(lambda x: eval(x),lista))
    pass
except SyntaxError:
    print('Alguna operacion esta mal definida')
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

for i in range(0,len(lista)):
    g.write(lista[i]+' = '+ str(lista2[i])+'\n')

f.close()
g.close()