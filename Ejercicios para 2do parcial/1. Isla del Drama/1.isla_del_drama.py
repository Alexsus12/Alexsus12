f = open("puntuaciones.txt", "r")
lineas = f #Con esto podemos crear nuestro indicador de posición de las filas de la lista
seleccionado = 0
P = 0
acumdef = 0
for lineas in f:
    datos = lineas.strip().split(",")
    nombre = datos[0]
    p1 = float(datos[1])
    p2 = float(datos[2])
    p3 = float(datos[3])
    
    P += 1
    definitiva = (p1+p2+p3)/3
    
    if definitiva >= 7.5:
        seleccionado += 1 
        acumdef += definitiva 
    
f.close()

#1.Porcentaje de candidatos que fueron seleccionados como participantes del reality show
if P !=0:
    porc = (seleccionado / P)*100
    print(f"Porcentaje de candidatos que fueron seleccionados como participantes del reality show: {porc:6.2f} %")
else:
    print("La lista está vacía")
    
#2. Promedio de la puntuación definitiva obtenida por los candidatos que pasaron a ser participantes.
if seleccionado !=0:    
    prom = acumdef / seleccionado
    print(f"Promedio de la puntuación definitiva obtenida por los candidatos que pasaron a ser participantes: {prom:6.2f} puntos")
else:
    print("No hubo candidato que pasara a ser participante")
    
if seleccionado < 20 or seleccionado > 24:
    print("Es necesaria una segunda etapa de selección")