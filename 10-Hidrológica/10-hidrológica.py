contmenor = 0
con_tipo_C = 0
consumidaC = 0
clientesC = 0
N = int(input("Ingrese el número de clientes: "))
for x in range(N):
    nombre = input("Nombre de la persona: ")
    tipo = input("Tipo de cliente: R = Residencial / C = Comercial ")
    tipo =  tipo.upper()
    lactual = float(input("Lectura de volumen actual EN METROS CÚBICOS: "))
    lanterior = float(input("Lectura de volumen anterior EN METROS CÚBICOS: "))
    
    #1. Cantidad de agua consumida por el cliente en m³.
    consumida = lanterior - lactual
    print(f"Cantidad de agua consumida: {consumida} {'metro cúbico' if consumida == 1 else 'metros cúbicos' }")
    
    #2. Monto a pagar por el agua consumida.
    if tipo == "R":
        if consumida < 40:
            contmenor += 1
        if consumida <= 40:
            print("El monto a pagar es Bs 80.00")
        else:
            adicional = consumida - 40
            totalR = adicional*5
            print(f"el total a pagar es Bs { 80 + totalR}")
            
    if tipo == "C":
        consumidaC += consumida 
        clientesC += 1
        if consumida < 40:
            contmenor += 1
        if consumida <= 100:
            print("El monto a pagar es Bs 100.00")
        else:
            adicional = consumida - 100
            totalC = adicional*10
            total = 100 + totalC
            print(f"el total a pagar es Bs {total:6.2F}")
    
            if total > 200:
                con_tipo_C += 1
                if con_tipo_C == 1:
                    nombre_primer_tipoc = nombre
                    consumo_agua = consumida
        
            
#3. Porcentaje de clientes residenciales cuyo consumo de agua es menor a los 40 m3.
porc = (contmenor/N)*100
print(f"Porcentaje de clientes con consumo de agua menor a 40 m3: {porc:6.2f} %")

#4. Nombre y consumo de agua del primer cliente comercial que pago más de 200 Bs, en caso de haber más de un cliente con este
# monto reporte el primero encontrado y cuente los demás.
print("Nombre de la primera persona tipo C que pagó más de Bs 200.00")
print(nombre_primer_tipoc)
print(f"Y su consumo de agua fue: {consumo_agua} metros cúbicos")
if con_tipo_C == 1:
    print("Fue el único cliente con estas características")
else:
    con_tipo_C -= 1
    print(f"Hubo {con_tipo_C} {'persona' if con_tipo_C == 1 else 'personas'} más con estas características")
    
#5. Promedio del consumo de agua de los clientes comerciales.
if clientesC != 0:
    prom = consumidaC/clientesC
    print(f"Promedio del consumo de agua de los clientes comerciales: {prom:6.2f} metros cúbicos")
else:
    print("No hubo clientes comerciales")