#Ejercicio Resuelto 14
Ventas1 = int(input())
Ventas2 = int(input())
Ventas3 = int(input())
SalarioGeneral = int(input())
UmbralVentas = (Ventas1+Ventas2+Ventas3)*0.33
if Ventas1 > UmbralVentas:
    SalarioV1 = SalarioGeneral + 0.2*SalarioGeneral
else:
    SalarioV1 = SalarioGeneral
if Ventas2 > UmbralVentas:
    SalarioV2 = SalarioGeneral + 0.2*SalarioGeneral
else:
    SalarioV2 = SalarioGeneral
if Ventas3 > UmbralVentas:
    SalarioV3 = SalarioGeneral + 0.2*SalarioGeneral
else:
    SalarioV3 = UmbralVentas
print("Salario vendedores depto. 1:", SalarioV1, "Salario vendedores depto. 2", SalarioV2, "Salario vendedores depto. 3", SalarioV3)