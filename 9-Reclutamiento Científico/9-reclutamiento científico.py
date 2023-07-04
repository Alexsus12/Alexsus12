A = 1
P = 0
E = 0
contadortiempo1 = 0
contadortiempo2 = 0
contreclut = 0
while A == 1:
    P += 1
    nombre = input("Nombre del estudiante: ")
    escuela = int(input("""Escuela a la que pertenece:
                    1 = Eléctrica / 2 = Industrial / 3 = Civil / 4 = Química
                                                """))
    tiempo1 = int(input("Tiempo invertido para resolver el primer parcial EN MINUTOS: "))
    tiempo2 = int(input("Tiempo invertido para resolver el segundo parcial EN MINUTOS: "))
    
#1. Tiempo promedio en minutos que invirtió cada estudiante para resolver los parciales.
    B1 = tiempo1 + tiempo2
    prom1 = (B1)/2
    print(f"Usted invirtió {prom1:6.2f} minutos para resolver los dos parciales")
    
    #2. Un mensaje que indique, por cada estudiante, si esta reclutado o no.
    if prom1 < 90:
        contreclut += 1 
        print("¡Estás reclutado!")
    else:
        print("No estás reclutado.")
    if escuela == 1 and prom1 < 90:   
        E += 1 
        if E == 1:
            menortiempo = prom1
            asistente = nombre
    
        if prom1 < menortiempo:
                menortiempo = prom1
                asistente = nombre
            
    A = int(input("¿Desea agregar otro estudiante?: 1 = Sí / 2 = No "))
    

#3. Porcentaje de estudiantes que este científico reclutará.
porc = (contreclut/P)*100
print(f"El porcentaje de estudiantes reclutados es del {porc:6.2f} %")

#4. Nombre del estudiante que será el asistente directo de este científico loco.
print(f"El nombre del asistente del científico es: {asistente}")