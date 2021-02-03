class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Rectangulo:

    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        self.base = abs(self.final.x - self.inicio.x)
        self.altura = abs(self.final.y - self.inicio.y)
        self.area = self.base * self.altura

    def mostrar_base(self):
        print(f"La base del rectangulo es {self.base}")

    def mostrar_altura(self):
        print(f"La altura del rectangulo es {self.altura}")

    def mostrar_area(self):
        print(f"El area del rectangulo es {self.area}")


a = Punto(0, 0)
b = Punto(10, 10)

rec = Rectangulo(a, b)

rec.mostrar_area()
rec.mostrar_altura()
rec.mostrar_base()
