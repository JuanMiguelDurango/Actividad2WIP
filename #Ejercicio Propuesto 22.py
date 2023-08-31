#Ejercicio Propuesto 22
Nombre = str(input())
SalarioHora = int(input())
HorasMes = int(input())
SalarioMensual = SalarioHora*HorasMes
if SalarioMensual > 450000:
    print(Nombre, SalarioMensual)
else:
    print(Nombre)