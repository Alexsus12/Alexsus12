A=2
con_area_1a = 0
con_area_1b = 0
con_area_2a = 0
cond = 0
procesado = 0
procesos = 0
while A == 2:
    procesos += 1 
    x = float(input("Ingrese la abcisa (x): "))
    y = float(input("Ingrese la ordenada (y): "))
    print(f"El par ordenado es ({x},{y})")

    #Circunferencias
    circun_1 = x**2 + y**2
    circun_2 = (x-2)**2 + y**2 

    if circun_1 <= 4 and y >= 0:
        print("El punto está en el área I")
        con_area_1a += 1
        if cond == 0:
            procesado += 1 

    if circun_1 <= 4 and y < 0:
        print("Está fuera del área I sombreada pero dentro de la figura I (parte blanca)")
        con_area_1b += 1
        if cond == 0:
            procesado += 1 
        
    if circun_1 > 4 and circun_2 > 4:
        print("Está fuera de las circunferencias ")
        if cond == 0:
            procesado += 1 
        
    if circun_2 <= 4 and circun_1 > 4:
        print("El punto está en el área II")
        con_area_2a += 1
        cond = 1
    
    #Metodo para el inciso de la suma de x + y con mínimo valor 
    suma = x + y  
    if procesos == 1:
        valor_minimo = suma
    if suma <= valor_minimo:
        valor_minimo = suma
        X = x
        Y = y
        
    A = int(input("¿Ha ingresado todos los puntos?: 1 = Sí / 2 = No "))
    
#Porcentaje de puntos en el área I con respecto a los puntos que caen dentro de la figura dada.
Area1 = con_area_1b + con_area_1a
if Area1 != 0:
    porc = (con_area_1a/Area1)*100
    print(f"% de puntos en el área I respecto a los puntos que caen dentro de la figura I: {porc:6.2f} %")
else:
    print("No hubo puntos dentro de la figura I")
    
#Cuantos puntos fueron procesados antes de que apareciera el primer punto en el área II.
if cond == 1:
    print(f"{'Fue' if procesado == 1 else 'Fueron'} {'procesado' if procesado == 1 else 'procesados' } {procesado} {'punto' if procesado == 1 else 'puntos'} antes del primer punto en el área II")
else:
    print("No hubo puntos en el área II")

#Par (X, Y) donde la suma de ellos (X + Y) genera el mínimo valor
print(f"El último par (x,y) donde la suma de ellos genera el mínimo valor es el par: ({X},{Y})")

#En qué área (I o II) están la mayor cantidad de puntos.
if con_area_1a > con_area_2a:
    print(f"La mayor cantidad de puntos es en el área I: {con_area_1a} {'punto' if con_area_1a == 1 else 'puntos'}")
    
if con_area_1a < con_area_2a:
    print(f"La mayor cantidad de puntos es en el área II: {con_area_2a} {'punto' if con_area_2a == 1 else 'puntos'}")
    
if con_area_1a == con_area_2a:
    print(f"Ambas áreas tienen la misma cantidad de puntos: {con_area_1a} {'punto' if con_area_1a == 1 else 'puntos'}")   

if con_area_2a == 0 and con_area_1a == 0:
    print("Ninguna de las áreas tienen puntos existentes")