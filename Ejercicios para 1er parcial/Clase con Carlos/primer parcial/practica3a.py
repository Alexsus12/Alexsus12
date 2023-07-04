N = int(input("¿Cuántos estudios se realizaron?: "))
cabeza = 2.75
torax = 2.50
columna = 5.25
extremidades = 2.25
acum_sin_iva_cabeza = 0
acum_sin_iva_torax = 0
acum_sin_iva_columna = 0
acum_sin_iva_extremidades = 0
acum_con_iva_cabeza = 0 
acum_con_iva_torax = 0
acum_con_iva_columna = 0
acum_con_iva_extremedidades = 0
A = 0
B = 0
c1 = 0
c2 = 0
con_edades = 0
for x in range(N):
    cedula = input("Ingrese cédula: ")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad de la persona: "))
    tipo = int(input("Tipo de estudio realizado: 1 = Cabeza / 2 =  Tórax / 3 = Columna / 4 = Extremidades "))
    
    #PRECIOS
    if tipo == 1:
        cabezabs = cabeza*127
        acum_sin_iva_cabeza += cabezabs
        cabezaiva = cabezabs*0.08
        acum_con_iva_cabeza += cabezaiva
        if edad > 40:
            c1 = c1 + 1
            A += A + cabezabs
        print(nombre)
        print(f"El monto a pagar es Bs {cabezabs:6.2f}")
        print(f"el monto del IVA es de Bs {cabezaiva:6.2f}")
        total = cabezabs + cabezaiva 
        print(f"Total = Bs {total:6.2f}")
        
        
    if tipo == 2:
        toraxbs = torax*127
        acum_sin_iva_torax += toraxbs
        toraxiva = toraxbs*0.08
        acum_con_iva_torax += toraxiva
        print(nombre)
        print(f"El monto a pagar es Bs {toraxbs:6.2f}")
        print(f"el monto del IVA es de Bs {toraxiva:6.2f}")
        total = toraxbs + toraxiva
        print(f"Total = Bs {total:6.2f}")
        
    if tipo == 3:
        columnabs = columna*127
        acum_sin_iva_columna += columnabs
        columnaiva = columnabs*0.08
        acum_con_iva_columna += columnaiva
        if edad > 40:
            c2 = c2 + 1 
            B += B + columnabs
        print(nombre)
        print(f"El monto a pagar es Bs {columnabs:6.2f}")
        print(f"el monto del IVA es de Bs {columnaiva:6.2f}")
        total = columnabs + columnaiva
        print(f"Total = Bs {total:6.2f}")
        
    if tipo == 4:
        extremidadesbs = extremidades*127
        acum_sin_iva_extremidades += extremidadesbs
        extremidadesiva = extremidadesbs*0.08
        acum_con_iva_extremedidades += extremidadesiva
        print(nombre)
        print(f"El monto a pagar es Bs {extremidadesbs:6.2f}")
        print(f"el monto del IVA es de Bs {extremidadesiva:6.2f}")
        total = extremidadesbs + extremidadesiva
        print(f"Total = Bs {total:6.2f}")
        
    if  45 <= edad <= 52:
        con_edades += 1
        

TOTALA = acum_sin_iva_torax + acum_sin_iva_cabeza + acum_sin_iva_columna + acum_sin_iva_extremidades
TOTALB = acum_con_iva_cabeza + acum_con_iva_torax + acum_con_iva_columna + acum_con_iva_extremedidades
print(f"El total recaudado SIN IVA es de: Bs {TOTALA}")
print(f"El total de IVA recaudado es: Bs {TOTALB}")
C = c1+c2
if C !=0:
    prom = (A+B)/(C)
    print(f"Promedio de Monto en Bs. sin IVA de Estudios 1 o 3, con edad mayor a 40 años es: Bs {prom:6.2f}")
else:
    print("No hubo pacientes mayores a 40 años con estudios de cabeza o columna")

porc = (con_edades / N)*100
print(f"Porcentaje de Personas con edad comprendida entre 45 y 52 años: {porc:6.2f} %")
