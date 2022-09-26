import math

class figura:
    
    def __init__(self):
        print()
    
    def area():
        print()
    
    def perimetro():
        print()

class cercle(figura):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio
    
    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * self.radio ** 2

class triangle(figura):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 3

    def area(self):
        altura = math.sqrt(3) * self.lado / 2
        return self.lado * altura / 2

class rectangle(figura):

    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    
    def perimetro(self):
        return self.base * 2 + self.altura * 2
    
    def area(self):
        return self.base * self.altura

class cuadrat(rectangle):

    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2
