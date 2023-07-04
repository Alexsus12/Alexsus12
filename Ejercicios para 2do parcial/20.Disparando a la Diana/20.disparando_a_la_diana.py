f = open("Disparos.txt","r")
linea1 = f.readline()
datos0 = linea1.strip().split(":")
M = int(datos0[1])
dianacentro = 0

for disparo in f:
    datos = disparo.strip().split(",")
    nombre = datos[0]
    x = float(datos[1])
    y = float(datos[2])
    
    circunferencia = x**2 + y**2
    
    if x == 0 and y == 0:
        dianacentro += 1 
        if dianacentro ==1:
            nombrecentro = nombre
            print(f"{nombrecentro} -- Primer participante en acertar en el centro de la diana")
            print("Puntaje: 100 puntos")
            
    if circunferencia <=4 and dianacentro !=1:
        print(nombre) 
        print(f"Puntaje: 100 puntos")
        
    if circunferencia > 4 and circunferencia <=9:
        print(nombre) 
        print(f"Puntaje: 50 puntos")
        
    if circunferencia >9:
        print(nombre) 
        print(f"¡Fuera de la diana! -- 0 puntos")

f.close()