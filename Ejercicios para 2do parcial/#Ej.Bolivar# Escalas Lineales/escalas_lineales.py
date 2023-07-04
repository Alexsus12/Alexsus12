f = open("Medidas.txt","r")
g = open("Medidasdesviadas.txt","w")
h = open("Medidasaceptadas.txt","w")

g.write("MEDICIONES DESVIADAS \n")
h.write("MEDICIONES ACEPTADAS \n")

c = 0
linea0 = f.readline()
pesoideal = float(linea0)

for linea in f:
    datos = linea.strip().split(",")
    numoperador =  datos[0]
    medicion = float(datos[1])
    unidadmed = datos[2]
    unidadmed = unidadmed.strip().lower() #En caso de que tenga espacios y esté en mayúsculas
    
    if unidadmed == "k":
        transformada = medicion*1000
    if unidadmed == "l":
        transformada = medicion*0.4536*1000
    if unidadmed == "g":
        transformada = medicion
        
    desviacion = (abs(pesoideal - transformada)/pesoideal)*100
    print(f"Número de operador: {numoperador}")
    print(f"Valor de la medición: {transformada:6.2f} g")
    
    if desviacion > 5:
        print("La medición NO es aceptable")
        g.write(f"Numero del operador: {numoperador} -- Medicion: {transformada:6.2f} g -- Porc. de Desviación: {desviacion:6.2f} % \n")
    else:
        print("La medición es aceptable")
        c += 1
        if c ==1:
            mayordesviacion = desviacion
            mayornumop = numoperador
            mayormedicion = transformada
            mayorunidadmed = unidadmed
        elif desviacion > mayordesviacion:
            mayordesviacion = desviacion
            mayornumop = numoperador
            mayormedicion = transformada
            mayorunidadmed = unidadmed
        h.write(f"Numero del operador: {numoperador} -- Medicion: {transformada:6.2f} g -- Porc. de Desviación: {desviacion:6.2f} % \n")
    
if c > 0:
    print(f"Para el mayor porcentaje de desviación aceptada, los valores son:")
    print(f"Número del operador: {mayornumop}")
    print(f"Medición registrada: {mayormedicion:6.2f}")
    print(f"Unidad de medición utilizada: {mayorunidadmed}")
else:
    print("No hubo mediciones aceptables")