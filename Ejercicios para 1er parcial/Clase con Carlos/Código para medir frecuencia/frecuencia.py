cliente = 0 #Inicio contador de clientes

respuesta = 1 #Necesario para que la condición del ciclo sea True
while respuesta == 1:
    tipo = int(input("Forma de pago (1, 2 ó 3):"))
    respuesta = int(input("Hay más clientes (SI-1, NO-2)?"))

    # Contador de clientes
    cliente = cliente + 1
    
    if cliente == 1:
        #Es el primer cliente, valores iniciales
        
        #Contador de frecuencia de modo de pago
        c = 0 
        
        #Variable que almacena la forma de pago de la repetición anterior
        #Al ser la primera vez, se guarda la actual
        tipo_anterior = tipo 
        
        #Como es primera vez, se define el primer mayor
        mayor = 1
        tipo_mayor = tipo
        
    if tipo == tipo_anterior:
        #Si el tipo de pago sigue siendo el mismo, incremento
        c = c + 1
    else:
        #No es el mismo tipo de pago del cliente anterior
        if c > mayor:
            #Si la frecuencia c es mayor a la guardada,
            #guarde los nuevos valores de mayor y tipo
            mayor = c
            tipo_mayor = tipo_anterior
        #****************    Esta parte es clave    *********************#
        #Inicio el contador de frecuencia en 1 ya que en esta  repetición#
        #cambió la forma de pago, por lo tanto tengo 1 vez del nuevo tipo#
        #de pago, al que guardo como tipo_anterior para que en la próxima#
        #repetición se chequee si sigue siendo la misma                  #
        c = 1
        tipo_anterior = tipo
        #****************************************************************#

#Salimos del cliclo, así que es el último cliente, verifico que el modo de
#pago no sea mayor que el guardado.
#Esto es necesario para los casos en el que la forma de pago con mayor
#frecuencia sea la que se usa al final. Ej: 1,1,2,2,2,3,3,3,3
#Sin este chequeo mostraría a 2 como el mayor ya  que al salir  del  ciclo
#todavía seguíamos leyendo la misma forma de pago que el penúltimo.
if c > mayor:
    #Si la frecuencia c es mayor a la guardada,
    #guarde los nuevos valores de mayor y tipo
    mayor = c
    tipo_mayor = tipo_anterior

#Como un extra a lo visto en clase, te muestro como usar un if dentro de una expresión f (imprime 'vez' si es 1 vez)
print(f"El tipo de pago usado con mayor frecuencia de forma consecutiva fue {tipo_mayor} con {mayor} {'vez' if mayor==1 else 'veces'}")