f = open("Suscriptores.txt", "r")
g = open("Multados.txt", "w")
m = 0
acumpromact = 0
linea = f
P = 0
nm = 0
for linea in f:
    datos = linea.strip().split(",")
    numero = datos[0]
    consumomesant = int(datos[1])
    lecinicial = int(datos[2])
    lecfinal = int(datos[3])
    P += 1
    
    consumomesact = lecfinal - lecinicial
    
    if consumomesact > consumomesant*1.1:
        m += 1
        incremento = (consumomesact/consumomesant)*100
        acumpromact += consumomesact 
        g.write(f"Num.Contrato: {numero} -- Porc.Incemento: {incremento:6.2f} %")
        g.write("\n")
    
    if consumomesact > consumomesant and consumomesact <= consumomesant*1.1:
        nm += 1
        incrementonm = (consumomesact/consumomesant)*100
        if nm ==1:
            porcmayor = incrementonm
            numeromayor = numero
        elif incrementonm > porcmayor:
            porcmayor = incrementonm
            numeromayor = numero

f.close()
g.close()
        
#a) Consumo Promedio actual de los usuarios multados en KWh de la zona en estudio
if m !=0:
    prom = acumpromact/m 
    print(f"Promedio de consumo actual de los usuarios multados de la zona en estudio: {prom:6.2f} KWh")
else:
    print("No hubo usuarios multados")
    
#b) Porcentaje de suscriptores que serán multados y porcentaje de suscriptores que NO serán multados
if P !=0:
    print(f"Porc. de suscriptores que serán multados: {((m/P)*100):6.2f} %") #Otra forma de hacerlo
    print(f"Porc. de suscriptores que NO serán multados: {(((P-m)/P)*100):6.2f} %")
else:
    print("La lista está vacía")

#c) De los suscriptores que NO serán multados número de contrato del que tiene el mayor porcentaje de incremento de consumo
if nm != 0:
    print(f"Número de contrato del que tiene el mayor porcentaje de incremento de consumo y no está multado: {numeromayor}")
else:
    print("La lista está vacía o todos los de la lista fueron multados")