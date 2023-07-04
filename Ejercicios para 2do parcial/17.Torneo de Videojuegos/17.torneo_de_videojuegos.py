f = open("Torneo.txt","r")
g = open("Resultados.txt","w")
linea0 = f.readline()
datos0 =linea0.strip().split(",")
nombrejug1 = datos0[0]
nombrejug2 = datos0[1]
print(nombrejug1)
print(nombrejug2)

vidajug1 = 100
vidajug2 = 100
g1 = 0
g2 = 0
danoacum1 = 0
danoacum2 = 0
c = 0
iguales = 0

for linea in f:
    datos = linea.strip().split(",")
    golpedejug = int(datos[0])
    porcdano = float(datos[1])
    c += 1
    
    if c ==1:
        mayorporcdano = porcdano
        mayornombrejug = golpedejug
        
    elif porcdano > mayorporcdano:
        iguales = 0
        mayorporcdano = porcdano
        mayornombrejug = golpedejug

    if porcdano == mayorporcdano:
        iguales += 1 
        
    if golpedejug ==1:
        g1 += 1 
        danoacum1 += porcdano 
        vidajug2 -= porcdano  
        g.write(f"Golpe dado por: {nombrejug1} \n")
        g.write(f"Vida del enemigo: {vidajug2}% \n")
        g.write("\n")

    if golpedejug ==2:
        g2 += 1
        danoacum2 += porcdano 
        vidajug1 -= porcdano 
        g.write(f"Golpe dado por: {nombrejug2} \n")
        g.write(f"Vida del enemigo: {vidajug1}% \n")
        g.write("\n")
     
    if vidajug1 <=0:
        nombreganador = nombrejug2
    if vidajug2 <=0:
        nombreganador = nombrejug1
            

g.write(f"Ganador(a): {nombreganador} \n")
if nombreganador == nombrejug1:
    g.write(f"Golpes dados: {g1} \n")
    g.write(f"Porcentaje de vida que le quedó: {vidajug1}% \n")
    
else:
    g.write(f"Golpes dados: {g2} \n")
    g.write(f"Porcentaje de vida que le quedó: {vidajug2}% \n")
    
f.close()
g.close()

promdano1 = danoacum1/g1
print(f"Porcentaje de daño promedio de golpes del jugador 1: {promdano1:6.2f} % de daño promedio")
promdano2 = danoacum2/g2
print(f"Porcentaje de daño promedio de golpes del jugador 2: {promdano2:6.2f} % de daño promedio")

if mayornombrejug ==2:
    print(f"Nombre del jugador con el mayor porcentaje de daño: {nombrejug2}")
if mayornombrejug ==1:
    print(f"Nombre del jugador con el mayor porcentaje de daño: {nombrejug1}")

if iguales - 1  > 0:
    print(f"{'hubo' if (iguales - 1) == 1 else 'hubieron'} {iguales - 1} {'golpe' if (iguales - 1) ==1 else 'golpes'} más con este porcentaje mayor de daño")