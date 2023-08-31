#Ejercicio Resuelto 15
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A == B and A == C:
    if D > A:
        print("La esfera D es la diferente y es de mayor peso")
    else:
        print("La esfera D es la diferente y es de menor peso")
if A == B and A == D:
    if C > A:
        print("La esfera C es la diferente y es de mayor peso")
    else:
        print("La esfera C es la diferente y es de menor peso")
if A == C and A == D:
    if B > A:
        print("La esfera B es la diferente y es de mayor peso")
    else:
        print("La esfera B es la diferente y es de menor peso")
if B == C and B == D:
    if A > B:
        print("La esfera A es la diferente y es de mayor peso")
    else:
        print("La esfera A es la diferente y es de menor peso")