f = open("Envios.txt","r")
linea = f.readline()
datos0 = linea.strip().split(",")
W = int(datos0[0])
p = 0
supera = 0
repetido = 0

for paquete in f:
    datos = paquete.strip().split(",")
    origen = datos[0]
    destino = datos[1]
    peso = float(datos[2])
    p += 1
    
    #Ciudad a donde llegó el paquete más pesado.
    if p ==1:
        primeraciudad= destino
        pesomayor = peso
        ciudadmayor = destino
    elif peso > pesomayor:
        pesomayor = peso
        ciudadmayor = destino
        
    #Porcentaje de paquetes enviados que superan los 150Kg.
    if peso > 150:
        supera += 1 
        
    #Cuantos envíos se hicieron a la primera ciudad destino registrada en el archivo.
    if destino == primeraciudad:
        repetido += 1

f.close()
print(f"Ciudad a donde llegó el paquete más pesado: {ciudadmayor}")

porc = (supera/W)*100
print(f"Porcentaje de paquetes enviados que superan los 150Kg: {porc:6.2f} %")

print(f"# de envíos que se hicieron a la primera ciudad destino registrada en el archivo: {repetido} {'envio' if repetido == 1 else 'envios'}")