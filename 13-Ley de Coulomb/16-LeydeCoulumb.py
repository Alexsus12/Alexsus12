A = 1
atraccion = 0
repulsion = 0
P = 0
vacio = 0
acumvacio = 0
contrmenor = 0

while A == 1: 
    q1 = float(input("Valor carga 1: "))
    q2 = float(input("Valor carga 2: "))
    r = float(input("Distancia de separación entre ellas: "))
    medio = int(input("""¿Medio que rodea a las cargas?
                      1 : Vacío / 2: Porcelana / 3: Baquelita
                                    """))   
    P += 1   
            
    if medio == 1:
        Fe = 9000*((q1*q2)/r**2) 
        print(f"La magnitud de la fuerza eléctrica es: {Fe:6.2f} N")
        vacio += 1
        acumvacio += Fe 
    
    if medio == 2:
        Fe = 1500*((q1*q2)/r**2) 
        print(f"La magnitud de la fuerza eléctrica es: {Fe:6.2f} N")
        
    if medio == 3:
        Fe = 2000*((q1*q2)/r**2) 
        print(f"La magnitud de la fuerza eléctrica es: {Fe:6.2f} N")
        
    if P == 1:
        rmenor = r
        Femenor = Fe
        
    if r < rmenor:
        rmenor = r
        Femenor = Fe
        
    if r == rmenor and P > 1: 
        contrmenor += 1
    
    if q1 < 0 and q2 > 0 or q1 > 0 and q2 < 0:
        atraccion += 1   
    
    A = int(input("""¿Desea agregar más datos?
                         1: Sí / 2 : No
                                """))
        
#2. Porcentaje de parejas en que la Fuerza Eléctrica es de atracción.
porc = (atraccion/P)*100
print(f"Porcentaje de parejas en que la Fuerza es de atracción: {porc:6.2f} %")

#3. Promedio de la Fuerza Eléctrica de las parejas que están en el vacío.
if vacio != 0:
    prom = acumvacio / vacio
    print(f"Promedio de la Fuerza Eléctrica de las parejas que están en el vacío: {prom:6.2f} N")
else:
    print("No hubo parejas en el vacío")
    
#Cuál es la magnitud de la Fuerza Eléctrica donde la distancia entre las cargas es la menor y de haber varias parejas con esta
#misma menor distancia, entonces indique la magnitud de Fe en la primera de ellas y cuantas parejas además de ella están
#separadas a esta misma distancia.
print(f"{Femenor:6.2f} N es la magnitud donde la distancia entre las cargas es la menor")
print(f"hay {contrmenor} {'pareja' if contrmenor == 1 else 'parejas'} más separadas a esta misma distancia")