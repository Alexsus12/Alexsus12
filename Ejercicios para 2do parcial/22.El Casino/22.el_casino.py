f = open("Jugadas.txt","r")
linea1 = f.readline()
datos0 = linea1.strip().split(":")
N = int(datos0[1])
gano = 0
suma10 = 0
monto10 = 0

for jugadas in f:
    datos = jugadas.strip().split(",") 
    numapostado = int(datos[0])
    cara1 = int(datos[1])
    cara2 = int(datos[2])
    montoapostado = float(datos[3])
    
    sumadados = cara1 + cara2
    
    if numapostado == sumadados:
        gano += 1
        
    if numapostado ==10:
        suma10 += 1 
        monto10 += montoapostado 

f.close()
        
#Porcentaje de veces que ganó el apostador.
porc = (gano/N)*100
print(f"Porcentaje de veces que ganó el apostador: {porc:6.2f} %")

#Promedio de Bolívares apostados en aquellas jugadas donde los dados sumaban 10.
if monto10!=0 and suma10>0:
    prom = monto10/suma10
    print(f"Promedio de Bs apostados en aquellas jugadas donde los dados sumaban 10: {prom:6.2f} Bs")
else:
    print("No se apostaron Bs para jugadas donde los dados sumaran 10")
    
        