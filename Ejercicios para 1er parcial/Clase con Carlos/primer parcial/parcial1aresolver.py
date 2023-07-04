A = 0 
P = 0 #PERSONAS
efectivo = 0
montoscompra = 0
maximo = 0
consecutivo = 0
cont_consec = 1
while A==0:
    nombre= input("Ingrese nombre: ")
    cedula = input("Ingrese cédula: ")
    monto = float(input("Ingrese el monto EN BOLÍVARES: Bs "))
    forma = int(input("¿Forma de pago?: 1 = Efectivo / 2 = Débito / 3 = Tarjeta de Crédito "))
    montoscompra += monto 
    P += 1
    if forma == 1:
        efectivo += 1
        consecutivo = 1
        A = 0
        if A == 0 and consecutivo == 1:
            cont_consec += 1
            cont_consec_def = cont_consec
            if cont_consec_def >= 1:
                ContA = cont_consec_def
        
            consecutivo = 1

    A = int(input("¿Desea finalizar el programa?: 0 = Sí / 1 = No "))
    
    if forma == 2:
        if monto >= maximo:
            maximo = monto
            nombremax = nombre
    
    if forma == 3:
        ultimo = nombre
    
        
prom = montoscompra / P
print(f"El promedio de monto de compra es: Bs {prom:6.2f} ")
porc = (efectivo / P)*100
print(f"El porcentaj de clientes con pago en efectivo es del {porc:6.2f} % ")
print(f"El nombre del cliente con mayor monto de compra cancelado con tarjeta de débito es {nombremax}")
print(f"El último cliente que canceló con tarjeta de crédito es {ultimo}")