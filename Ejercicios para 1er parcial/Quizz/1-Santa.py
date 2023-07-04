A = 1
P = 0
ninos16 = 0
acum_costo_ninos = 0
S = 0
print("Lista de todos los niños del mundo para Santa")
while A == 1:
    nombre = input("Nombre del niño: ")
    edad = int(input("Ingrese la edad: "))
    dias = int(input("# de días de buen comportamiento: "))
    costo = float(input("Costo del regalo solicitado en Bs: "))
    P += 1 #Contador de niños
    S += costo #acumulador de costos total
    
    #Por cada niño unmensaje que indique “RECIBIRÁ REGALO
    #EXTRA” o “NO RECIBIRÁ REGALO EXTRA” dependiendo de
    #su comportamiento. (1,5 ptos)
    if dias >= 250:
        print("Recibirá regalo extra :)")
    else:
        print("No recibirá regalo extra :(")

    if P ==1:
        costomayor = costo
        edadmayor = edad
        nombremayor = nombre
    
    if costo > costomayor:
        costomayor = costo
        edadmayor = edad
        nombremayor = nombre
    
    if 1 <= edad <= 6:
        ninos16 += 1
        acum_costo_ninos += costo 

    A = int(input("¿Desea agregar otro niño a la lista?: 1: Sí / 2: No "))
    
#Nombre y edad del niño que pidió el juguete más caro.
#(3,5 ptos)  
print(f"{nombremayor}, de {edadmayor} {'año' if edad == 1 else 'años'} pidió el juguete más caro")

#¿Cuánto debe pagar Santa en promedio por los regalos
#de los niños que tienen entre 1 y 6 años, ambos inclusive? (4 ptos.)
if ninos16 !=0:
    prom = acum_costo_ninos / ninos16
    print(f"El pago en promedio por regalos a niños entre 1 y 6 años es de Bs {prom:6.2f}")
else:
    print("No hubo niños con la edad comprendida entre 5 y 6 años")

#Cantidad de dinero que deberá tener santa para complacer a todos los niños (1,5 ptos)
print(f"Santa deberá tener Bs {S} para complacer a todos los niños")