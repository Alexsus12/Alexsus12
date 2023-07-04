f = open("Rechazados.txt","r")
manana = 0
tarde = 0
noche = 0
for linea in f:
    datos = linea.strip().split(",")
    turno = int(datos[0]) 
    nombre = datos[1]
    cantidad = int(datos[2])
    
    #1. Cantidad total de producto rechazado en el período en estudio, en cada uno de los turnos
    if turno ==1:
        manana += cantidad
    if turno ==2:
        tarde += cantidad
    if turno ==3:
        noche += cantidad
        
f.close()
print(f"Cantidad total de productos rechazados en la mañana: {manana} {'producto' if manana == 1 else 'productos'}")
print(f"Cantidad total de productos rechazados en la mañana: {tarde} {'producto' if tarde == 1 else 'productos'}")
print(f"Cantidad total de productos rechazados en la noche: {noche} {'producto' if noche == 1 else 'productos'}")

#2. Imprima un mensaje que indique en cual turno (mañana, tarde o noche) ocurrió la mayor cantidad total de producto
#rechazado en el período de estudio.
if manana > tarde and manana > noche:
    print("En el turno de la mañana ocurrió la mayor cantidad de productos rechazados")
if tarde > manana and tarde > noche:
    print("En el turno de la tarde ocurrió la mayor cantidad de productos rechazados")
if noche > tarde and noche > manana:
    print("En el turno de la noche ocurrió la mayor cantidad de productos rechazados")
if noche == tarde == manana:
    print("Los tres turnos tuvieron la misma cantidad de productos rechazados")
if noche == tarde and noche > manana:
    print("En el turno de la noche y la tarde ocurrió la mayor cantidad de productos rechazados")
if noche > tarde and noche == manana:
    print("En el turno de la noche y la mañana ocurrió la mayor cantidad de productos rechazados")
if manana == tarde and manana > noche:
    print("En el turno de la mañana y la tarde ocurrió la mayor cantidad de productos rechazados")
    