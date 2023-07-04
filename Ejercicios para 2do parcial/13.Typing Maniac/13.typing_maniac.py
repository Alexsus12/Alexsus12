f = open("Usuario.txt","r")
g = open("Resultados.txt","w")

linea = f.readline()
datos0 = linea.strip().split(",")
nombrejug = datos0[0]
numnivel = int(datos0[1])

c1 = 0
c2 = 0
c3 = 0
jugadas = 0
aciertos = 0
tipo3 = 0

for linea in f:
    datos = linea.strip().split(",")
    dificult = int(datos[0])
    pdada = datos[1]
    pescrita = datos[2]
    
    jugadas += 1
    
    if dificult ==1:
        if pescrita == pdada:
            aciertos += 1 
            g.write(f"Número de nivel: {numnivel} \n")
            g.write(f"Puntaje por acertar la palabra: 2 puntos \n")
            c1 += 2
        else:
            g.write(f"Número de nivel: {numnivel} \n")
            g.write("Puntaje: 0 puntos \n")
            
    if dificult ==2:
        if pescrita == pdada:
            aciertos += 1
            g.write(f"Número de nivel: {numnivel} \n")
            g.write(f"Puntaje por acertar la palabra: 4 puntos \n")
            c2 += 4
        else:
            g.write(f"Número de nivel: {numnivel} \n")
            g.write("Puntaje: 0 puntos \n")

    if dificult ==3:
        if pescrita == pdada:
            tipo3 += 1 
            if tipo3 ==1:
                primerapalabra = pescrita
            aciertos += 1
            g.write(f"Número de nivel: {numnivel} \n")
            g.write(f"Puntaje por acertar la palabra: 8 puntos \n")
            c3 += 8
        else:
            g.write(f"Número de nivel: {numnivel} \n")
            g.write("Puntaje: 0 puntos \n")

if jugadas !=0:
    #Número de Jugadas
    g.write(f"\nNúmero de jugadas: {jugadas} \n")
    
    #Puntaje final del jugador
    pfinal = c1 + c2 + c3
    g.write(f"Puntaje final del jugador: {pfinal} puntos \n")
    
    #Porcentaje de aciertos
    porc = (aciertos/jugadas)*100
    g.write(f"Porcentaje de aciertos: {porc:6.2f} % \n")
    
    #1. Primera palabra difícil en ser acertada
    if tipo3 !=0:
        print(f"Primera palabra difícil en ser acertada: {primerapalabra}")
    else:
        print("No hubo palabras difíciles en ser acertadas")
        
    #2. Si el jugador perdió o pasó de nivel
    if pfinal >= 100:
        print("El jugador pasó de nivel")
    else:
        print("El jugador perdió")
else:
    g.write("La lista está vacía")

f.close()
g.close()