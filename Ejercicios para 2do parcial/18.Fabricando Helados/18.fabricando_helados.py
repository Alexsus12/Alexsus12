f = open("Produccion.txt","r")
g= open("Nacionales.txt","w")
h= open("Importadas.txt","w")
g.write(f"# de órdenes procesadas de tipo nacional: \n")
h.write(f"# de órdenes procesadas de tipo importadas: \n")
ttotal = 0
p = 0
for ordenes in f:
    datos = ordenes.strip().split(",")
    fecha = datos[0]
    numorden = datos[1]
    tipo = int(datos[2])
    tiempo = float(datos[3])
    
    ttotal += tiempo 
    p += 1
    if p ==1:
        tiempomayor = tiempo
        fechamayor = fecha
        numordenmayor = numorden
    elif tiempo > tiempomayor:
        tiempomayor = tiempo
        fechamayor = fecha
        numordenmayor = numorden
    
    if tipo ==1:
        g.write(f"número de orden: {numorden} -- Fecha de fabricación: {fecha} -- Tiempo de Fabricación: {tiempo} {'minuto' if tiempo == 1 else 'minutos'} \n")

    if tipo ==2:
        h.write(f"número de orden: {numorden} -- Fecha de fabricación: {fecha} -- Tiempo de Fabricación: {tiempo} {'minuto' if tiempo == 1 else 'minutos'} \n")
    
f.close()
g.close()
h.close()

horas = ttotal//60
minutos = (ttotal/60 - horas)*60
print(f"Tiempo de fabricación de todas las órdenes:")
print(f"Horas: {horas} -- Minutos: {minutos:6.2f}")