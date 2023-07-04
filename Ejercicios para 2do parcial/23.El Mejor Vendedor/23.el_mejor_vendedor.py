f = open("Mejor.txt","r")
g = open("Mayor.txt","w")
h = open("Detal.txt","w")

g.write("VENTAS AL MAYOR: \n")
h.write("VENTAS AL DETAL: \n")

linea1 = f.readline()
datos0 = linea1.strip().split(":")
nombre = datos0[1]
acumtipo1 = 0
acumtipo2 = 0

for productos in f:
    datos = productos.strip().split(",")
    nombrejuguete = datos[0]
    cantidad = int(datos[1])
    tipo = int(datos[2])
    costo = float(datos[3])
    costototal = cantidad*costo
    
    if tipo ==1:
        acumtipo1 += costototal
        g.write(f"Nombre del juguete: {nombrejuguete} -- Cantidad: {cantidad} -- Total: Bs {costototal} \n")

    if tipo ==2:
        acumtipo2 += costototal
        h.write(f"Nombre del juguete: {nombrejuguete} -- Cantidad: {cantidad} -- Total: Bs {costototal} \n")
        
f.close()
g.close()
h.close()

print(f"Nombre del vendedor: {nombre}")
print(f"Monto total vendido al mayor: Bs {acumtipo1}")
print(f"Monto total vendido al detal: Bs {acumtipo2}")
