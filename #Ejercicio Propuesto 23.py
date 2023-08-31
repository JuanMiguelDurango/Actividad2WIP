#Ejercicio Propuesto 23
import math
A = int(input())
B = int(input())
C = int(input())
discriminante = B**2 - 4*A*C
if discriminante < 0:
    print("La ecuación de segúndo grado no tiene solución")
else:
    Solucion1 = (-B + math.sqrt(discriminante))/(2*A)
    Solucion2 = (-B - math.sqrt(discriminante))/(2*A)
    print("La ecuación tiene las soluciónes:", Solucion1, "y", Solucion2)