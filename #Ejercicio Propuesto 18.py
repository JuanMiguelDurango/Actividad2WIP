#Ejercicio Propuesto 18
Codigo = int(input("Inserte código: "))
Nombre = str(input("Inserte nombre: "))
HorasMes = int(input("Inserte horas al mes: "))
ValorHora = int(input("Inserte el valor de hora: "))
retencion = float(input("Inserte porcentaje de retención: "))
SalarioBruto = ValorHora*HorasMes
SalarioNeto = SalarioBruto-SalarioBruto*(retencion/100)
print("Código:", Codigo, "Nombre:", Nombre, "Salario bruto:", SalarioBruto, "Salario neto:", SalarioNeto)