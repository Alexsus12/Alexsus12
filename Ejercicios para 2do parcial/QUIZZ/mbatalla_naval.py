# La libreria math permite el uso de math.sqrt
import math

# g es la aceleración de la gravedad
g = 9.8

# Abrir los archivos
lanzamientos = open("mlanzamientos.txt","r")
destruidos = open("destruidos.txt","w")
nodestruidos = open("nodestruidos.txt","w")

# Leer el número de disparos que se leeran desde el archivo
M = int(lanzamientos.readline().strip())

# Vo inicial
vo = 250

# Contadores de destruidos (d) y no destruidos (nd)
d = 0
nd = 0

# Ciclo repetitivo de M vueltas.
# La variable i tendrá desde el valor 0 hasta el valor M-1
for i in range(M):
    
    # Se lee una linea (lanzamiento) desde el archivo de lanzamientos
    lanzamiento = lanzamientos.readline()
    
    # Se separan los tres datos del lanzamiento
    datos = lanzamiento.strip().split(",")
    
    # Se guardan en variables individuales
    barco = datos[0]
    dist = float(datos[1])
    vox = float(datos[2])
    
    # Realizamos los cálculos para obtener el alcance del disparo
    voy = math.sqrt(vo**2 - vox**2)
    tvuelo = 2*voy/g
    alcance = vox*tvuelo
    
    # Se disminuye 1% para el próximo lanzamiento.
    # Dado que el cálculo ya fue realizado en las lineas anteriores,
    # la primera vez usa el valor 250 inicial.
    vo = vo*0.99 # Este cálculo es para el siguiente disparo
    
    # Si la diferencia entre el alcance y la distancia es menor a 10⁻³
    # El barco será destruido, de lo contrario, no lo será.
    if abs(alcance-dist) < 1E-3:
        destruidos.write(f"{barco}\n")
        d += 1
        #Si es el primer barco destruido, guardar
        if d == 1:
            primero = barco
    else:
        nodestruidos.write(f"{barco},{alcance:8.2f} m \n")
        nd += 1
        # Si es el primer barco no destruido, guardar
        # su distancia y su identificación como el mayor
        if nd == 1:
            mayor = dist
            bmayor = barco
        # Si no es el primer barco no destruido,
        # Chequear si está a una distancia mayor que la
        # guardada en la variable mayor
        elif dist > mayor:
            mayor = dist
            bmayor = barco

# Cerrar los archivos
lanzamientos.close()
destruidos.close()
nodestruidos.close()

# Imprimir de los NO DESTRUIDOS, si hay alguno, el que estaba más lejos 
if nd > 0:
    print(f"De los NO DESTRUIDOS, {bmayor} estaba más lejos")
else:
    print("Todos los barcos fueron destruidos")

# Determinar el porcentaje de barcos DESTRUIDOS y mostrarlo
porc = d/(d+nd)*100
print(f"El porcentaje de acierto fue de {porc:6.2f}%")

# Imprimir de los DESTRUIDOS, si hay alguno, cuál fue el primero
if d > 0:
    print(f"De los DESTRUIDOS, {primero} fue el primero")
else:
    print("No se destruyó ningún barco")
