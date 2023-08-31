#Ejercicio Resuelto 11
Numero1 = int(input())
Numero2 = int(input())
Numero3 = int(input())
Mayor = 0
if Numero1 > Numero2 and Numero1 > Numero3:
    Mayor = Numero1
elif Numero2 > Numero1 and Numero2 > Numero3:
    Mayor = Numero2
else:
    Mayor = Numero3
print("El valor mayor entre:", Numero1, Numero2, "y", Numero3, "es:", Mayor)