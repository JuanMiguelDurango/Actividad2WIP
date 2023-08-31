#Ejercicio Resuelto 10
NumeroInscripcion = str(input())
Nombre = str(input())
Patrimonio = int(input())
EstratoSocial = int(input())
Matricula = 50000
if Patrimonio > 2000000 and EstratoSocial > 3:
    Matricula = Matricula + Patrimonio*0.03
print("El estudiante con número de inscripción", NumeroInscripcion, "y nombre", Nombre, "debe pagar $", Matricula)