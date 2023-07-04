N = int(input("¿Cuántos partidos se realizarán?: "))
localwin = 0
visitwin = 0
acumtplocal = 0
acumtpvisit = 0
contaempate = 0

if N == 0:
    print("No se puede ejecutar el programa con ningún partido")
else:
    for x in range(N):
        local = input("Nombre equipo local: ")
        visit = input("Nombre equipo visitante: ")
        tplocal = int(input("Tiros a puerta del equipo local: "))
        tpvisit = int(input("Tiros a puerta del equipo visitante: "))
        goleslocal = int(input("Goles anotados por el equipo local: "))
        golesvisit = int(input("Goles anotados por el equipo visitante: "))
        acumtplocal += tplocal
        acumtpvisit += tpvisit 
        
        if goleslocal >=1:
            eficiencialocal = goleslocal + (tplocal/goleslocal)
        else:
            eficiencialocal = goleslocal 
            
        if golesvisit >=1:
            eficienciavisit = golesvisit + (tpvisit/golesvisit)
        else:
            eficienciavisit = golesvisit
        
        if goleslocal > golesvisit:
            localwin += 1 
            print(f"El ganador del partido es: {local}")  
            if x == N-1:
                ganadortorneo = local 
        if goleslocal < golesvisit:
            visitwin += 1 
            print (f"El ganador es: {visit}")
            if x == N-1:
                ganadortorneo = visit 

        if goleslocal == golesvisit and x != N-1:
            contaempate += 1 
            if contaempate == 1:
                nombrelocal = local
                nombrevisit = visit
            print("EMPATE")
        
        if goleslocal == golesvisit and x == N-1:
            print("Se decidirá el ganador a penales")
            print("Los goles por penales NO PUEDEN ser iguales")
            penaleslocal = int(input("Goles por penales del equipo local: "))
            penalesvisit = int(input("Goles por penales del equipo visitante: "))
            if penaleslocal > golesvisit:
                localwin += 1 
                print(f"El ganador del partido es: {local}") 
                ganadortorneo = local 
            if penaleslocal < penalesvisit:
                visitwin += 1
                print(f"El ganador del partido es: {visit}")
                ganadortorneo = visit 
             
            
        if eficiencialocal > eficienciavisit:
            print(f"Equipo con mayor eficiencia: {local}")
        if eficiencialocal < eficienciavisit:
            print(f"Equipo con mayor eficiencia: {visit}")
        if eficiencialocal == eficienciavisit:
            print(f"Ambos equipos tuvieron la misma eficiencia")
                        
    #1. % de veces que gana el equipo local y % de veces que gana el equipo visitante (2 ptos)
    porlocal = (localwin/N)*100
    print(f"Porc. de veces que gana el equipo local: {porlocal:6.2f} %")
    porvisit = (visitwin/N)*100
    print(f"Porc. de veces que gana el equipo visitante: {porvisit:6.2f} %")

    #2. Cantidad promedio de tiros a puerta efectuados por partido durante el torneo (1 ptos)
    tptotales = acumtplocal + acumtpvisit
    prom = (tptotales/N)
    print(f"Prom de tiros a puerta por partido durante el Mundialito: {prom:6.2f} tiros a puerta")
    
    #3. Equipos involucrados en el primer partido procesado en condición de empate (2 ptos)
    if contaempate >= 1:
        print(f"Equipos involucrados en el primer partido en condición de empate: {nombrelocal} y {nombrevisit}")
    else:
        print("No hubo partidos con empates")

    #4. Ganador del torneo, conociendo que ganará el torneo el equipo que gane la Final. (1 pto)
    print(f"El ganador del torneo es: {ganadortorneo}")