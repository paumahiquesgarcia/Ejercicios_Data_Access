import random

class ErrorNoEsEnter (Exception):
    pass

class ErrorEnterMassaMenut (Exception):
    pass

class ErrorEnterMassaGran (Exception):
    pass

numale = random.randint(0,100)
while True:

    try:
        num = int(input('Introduce un numero del 0 al 100: '))
        if num > numale:
            raise ErrorEnterMassaGran
        elif num < numale:
            raise ErrorEnterMassaMenut
        elif num == numale:
            print('Felicidades, has acertado!!!')
            break
        else:
            raise ErrorNoEsEnter
    except ErrorEnterMassaGran:
        print('No has acertado, el numero es mas pequeño que el que has introducido')
    except ErrorEnterMassaMenut:
        print('No has acertado, el numero es mas grande que el que has introducido')
    except ErrorNoEsEnter:
        print('Error, no has introducido un numero')