#Ejercicio Propuesto 24
A = int(input())
B = int(input())
C = int(input())
if A > B and A > C:
    print("A tiene mayor peso")
elif B > A and B > C:
    print("B tiene mayor peso")
else:
    print("C tiene mayor peso")