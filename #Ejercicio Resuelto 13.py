#Ejercicio Resuelto 13
ValorCompra = int(input())
Color = str(input())
Descuento = 0
if Color == "VERDE":
    Descuento = 10
if Color == "AMARILLO":
    Descuento = 25
if Color == "AZUL":
    Descuento = 50
if Color == "ROJO":
    Descuento = 100
Pago = ValorCompra-ValorCompra*(Descuento/100)
print("El cliente debe pagar: $", Pago)