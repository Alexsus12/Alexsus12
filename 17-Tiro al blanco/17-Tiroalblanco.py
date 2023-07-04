N = int(input("Ingrese el número de participantes: "))
fem = 0
out = 0
edadout = 0
dentro = 0 
acumfem = 0
puntajetotal = 0

if N <=0:
    print("No puede ejecutar el programa con 0 participantes o número negativos")
else:
    for x in range(N):
        nombre = input("Nombre del participante: ")
        edad = int(input("Ingrese la edad: "))
        genero = int(input("1: Femenino // 2: Masculino "))
        x = float(input("Cordenada x del disparo: "))
        y = float(input("Cordenada y del disparo: "))
        circunferencia = x**2 + y**2 
        
        
        if circunferencia <= 1: #Asumiré que si cae justo en la línea vale ese punto
            dentro += 1
            print("¡En el blanco!")
            print("Puntaje obtenido: 100 puntos")
            puntajetotal += 100 
            if genero ==1:
                fem += 1 
                acumfem += 100 
                if fem ==1:
                    primernombre = nombre
                    primeraedad = edad
        
        if 1 < circunferencia <=4: 
            dentro += 1
            print("Puntaje obtenido: 50 puntos")
            puntajetotal += 50
            if genero ==1:
                acumfem += 50

        if 4 < circunferencia <=9: 
            dentro += 1
            print("Puntaje obtenido: 20 puntos")
            puntajetotal += 20
            if genero ==1:
                acumfem += 20
                 
        if 9 < circunferencia <=16: 
            dentro += 1
            print("Puntaje obtenido: 10 puntos")
            puntajetotal += 10 
            if genero ==1:
                acumfem += 10
        
        if circunferencia > 16:
            print("Disparo fuera de la diana")
            out += 1
            edadout += edad
            
    #2. Nombre y edad del primer participante de género femenino que acierta en el blanco.
    if fem ==1:
        print(f"Nombre de la primera mujer que acierta en el blanco: {primernombre}")
        print(f"Edad: {primeraedad} años")
    else:
        print("No hubo mujer que acertara en el blanco")
        
    #3. Promedio de Edad de los participantes que su disparo cayó fuera de la diana.
    if out >=1:
        prom = edadout/out
        print(f"Promedio de edad de los participantes que su disparo cayó fuera de la diana: {prom} años")
    else:
        print("No hubo disparos fuera de la diana")

    #4. Porcentaje de disparos que cayeron en la diana o figura.
    if dentro >= 1:
        porc = (dentro/N)*100
    else:
        print("Ningún disparo cayó en la diana")
        
    #5. Cual género (Femenino o Masculino) obtuvo menos puntos.
    puntajemasc = puntajetotal - acumfem
    if acumfem > puntajemasc:
        print("El género masculino obtuvo menos puntos")
    else:
        print("El género femenino obtuvo menos puntos")
    if acumfem == puntajemasc:
        print("Empate en puntajes masculino y femenino")