import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return "Está sobre un eje"
    
    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return (dx, dy)
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        print(f"La distancia entre los puntos {self} y {otro_punto} es {distancia:.2f}")
        return distancia
