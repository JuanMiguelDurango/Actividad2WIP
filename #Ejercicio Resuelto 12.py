#Ejercicio Resuelto 12
Nombre = str(input())
Horas = int(input())
ValorHora = int(input())
Extras = 0
UltraExtras = 0
Salario = 0
if Horas > 40:
    Extras = Horas-40
    if Extras > 8:
        UltraExtras = Extras-8
        Salario += ValorHora*3*UltraExtras + ValorHora*2*8 + ValorHora*40
    else:
        Salario += ValorHora*2*Extras + ValorHora*40
else:
    Salario += ValorHora*Horas
print("El trabajador", Nombre, "devengó: $", Salario)