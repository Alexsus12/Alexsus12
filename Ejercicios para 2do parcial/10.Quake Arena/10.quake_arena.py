f = open("Juego.txt","r")
g = open("Resultados.txt","w")
menores = 0
j = 0
edadestotales = 0
edadesconmuerte = 0
c=0
linea = f.readline()
datos0 = linea.strip().split(",")
nombregrupo = datos0[0]
participantes = int(datos0[1])
iguales = 0

for linea in f:
    datos = linea.strip().split(",")
    nombre = datos[0]
    edad = int(datos[1])
    muertes = int(datos[2])
    
    j += 1 
    edadestotales += edad  
    
    #1. Porcentaje de jugadores menores de 23 años.
    if edad <23:
        menores += 1
    
#     #2. Nombre y edad del jugador con mayor cantidad enemigos exterminados, si hay varios con la misma
# cantidad de enemigos exterminados escriba el primero de ellos y cuantos además de él, exterminaron esa cantidad de
# enemigos.
    if j == 1:
        mayormuerte = muertes
        nombremayor = nombre
        edadmayor = edad
        
    if muertes > mayormuerte:
        mayormuerte = muertes
        nombremayor = nombre
        edadmayor = edad
    
    if muertes == mayormuerte and j !=1:
        iguales += 1 #Recordar restarle 1 al final para que no cuente al primero
        
    #3. Edad Promedio, de los jugadores que eliminaron a más de 5 enemigos
    if muertes > 5:
        edadesconmuerte += edad
        c+=1
        
if j !=0:
    g.write(f"Nombre del grupo: {nombregrupo} \n")
    g.write(f"Cantidad de participantes: {participantes} \n")
    porc = (menores/j)*100
    g.write(f"Porcentaje de jugadores menores de 23 años: {porc:6.2f} % \n")
    g.write(f"Jugador con mayor cantidad enemigos exterminados: {nombremayor} -- Edad: {edadmayor} años \n")
    g.write(f"Hubo {iguales - 1} {'persona' if iguales -1 == 1 else 'personas'} más que {'exterminó' if iguales -1  == 1 else 'exterminaron'} esa cantidad de enemigos \n")
    
    if c !=0:
        prom = edadesconmuerte/c
        g.write(f"Edad promedio de los jugadores que eliminaron a más de 5 enemigos: {prom:6.2f} años\n")
    else:
        g.write("No hubo jugadores que eliminaran a más de 5 enemigos \n")

else:
    g.write("La lista está vacía")     

f.close()
g.close()
