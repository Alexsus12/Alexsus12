añoactual= int(input("Ingrese el año actual: "))
mesactual= int(input("Ingrese el mes actual: "))
diactual= int(input("Ingrese el dia actual (número) de ese mes: "))
cumpleanos = 0
c1 = 0
obreros = 0 
acumedad = 0
W = int(input("Ingrese el número de empleados / visitantes: "))
for x in range(W):
    nombre = input("Ingrese su nombre: ")
    tipo = int(input("""¿Tipo de personal?
                     1: Gerente / 2: Administrativo / 3: Obrero / 4: Visitante
                                                """))
    sexo = int(input("Sexo -- 1: M / 2: F "))
    año = int(input("Año de nacimiento: "))
    mes = int(input("Mes de nacimiento: 1: Enero / 2: Febrero / 3: Marzo /4: Abril...: "))
    dia = int(input("Día de nacimiento: "))
    print(f"Su año de nacimiento es el {dia}/{mes}/{año}") 
    
    if mes < mesactual:
        cumpleanos += 1
        if cumpleanos == 1:
            nombreprimero = nombre
            
    if mes == mesactual:
        if dia <= diactual:
            cumpleanos += 1
            if cumpleanos == 1:
                nombreprimero = nombre
    
    edad = añoactual - año
    
    if edad > 35:
        c1 += 1
        añoultimo = edad
        ultimovisit = nombre
    
    if tipo == 3:
        obreros += 1
        acumedad += edad
        
#1. Porcentaje de personas que no han cumplido año.
porc = ((W - cumpleanos)/W)*100
print(f"El porcentaje de personas que no han cumplido años es del {porc:6.2f}")

#2. Nombre del primer empleado que ya cumplió año.
print(f"El primer empleado que ya cumplió años es {nombreprimero}")

#3. Último Visitante con más de 35 años y si hay más de un visitante con el mismo rango de edad indique cuántos en total tienen
# esa edad
if c1 >= 1:
    print(f"Último visitante con más de 35 años: {ultimovisit}")
    if c1 - 1 !=0: 
        print(f"Hay {c1 - 1} {'persona' if c1-1 == 1 else 'personas'} más {'mayor' if c1-1==1 else 'mayores'} de 35 años")
    else:
        print(f"No hubo más personas mayores de 35 años salvo por {ultimovisit}")
else:
    print("No hubo personas con más de 35 años")

#4. Edad promedio de los obreros.
if obreros !=0:
    prom = acumedad/obreros
    print(f"Edad promedio de los obreros: {prom} {'año' if prom == 1 else 'años'}")
else:
    print("No se registraron obreros")