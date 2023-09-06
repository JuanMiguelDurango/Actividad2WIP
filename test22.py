import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def hipotenusa(self):
       return (self.base**2 + self.altura**2)**0.5

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa

    def tipo(self):
        if self.base == self.altura == self.hipotenusa:
            return "Es un triángulo equilátero"
        elif self.base != self.altura != self.hipotenusa:
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"

circle = Circulo(2)
rectangle = Rectangulo(1, 2)
square = Cuadrado(3)
triangle = Triangulo(3, 5)

print("El área del círculo es:", circle.area(), "El perímetro del círculo es:", circle.perimetro())
print("El área del rectángulo es:", rectangle.area(), "El perímetro del rectángulo es:", rectangle.perimetro())
print("El área del cuadrado es:", square.area(), "El perímetro del cuadrado es:", square.perimetro())
print("El área del triángulo es:", triangle.area(), "El perímetro del triángulo es:", triangle.perimetro(), triangle.tipo())