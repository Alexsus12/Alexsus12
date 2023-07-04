N = int(input("Ingrese el número de compradores: "))
nacionales = 0
orquideas = 0
ramostotales = 0
ramosorquideas = 0

if N <=0:
    print("No se puede ejecutar el programa con números negativos o ningún comprador")
else:
    for x in range(N):
        nombre = input("Ingrese el nombre del comprador: ")
        tipo = int(input("Tipo de flor comprada -- 1: Rosas // 2: Orquídeas "))
        origen = input("Origen -- N: Nacional // I: Importado ")
        cantidad= int(input("Cantidad de ramos comprados: "))
        origen = origen.upper()
        ramostotales += cantidad
        
        #Rosas
        if tipo ==1:
            if origen == "N":
                nacionales += 1
                costo = cantidad*150
                print(f"Monto de compra: Bs {costo:6.2f}")
            if origen == "I":
                costo = cantidad*200
                print(f"Monto de compra: Bs {costo:6.2f}")
                
       #Orquideas
        if tipo ==2:
            if origen == "N":
                ramosorquideas += cantidad 
                costo = cantidad*250
                print(f"Monto de compra: Bs {costo:6.2f}")
            if origen == "I":
                orquideas += 1 
                costo = cantidad*350
                ultimonombre = nombre
                ultimomonto = costo
                if orquideas ==1:
                    primernombre = nombre
                    primermonto = costo   
                print(f"Monto de compra: Bs {costo:6.2f}")
    
    #2. Promedio de la compra de rosas nacionales.
    if nacionales >=1:
        prom = nacionales/N
        print(f"Promedio de la compra de rosas nacionales: {prom:6.2f} {'compra' if prom ==1 else 'compras'}")
    else:
        print("No se compraron rosas nacionales")
        
    #3. Nombre y monto de la compra del primer y último comprador de orquídeas importadas.
    if orquideas ==0:
        print("No hubo compradores de orquídeas importadas")
    if orquideas ==1:
        print(f"Nombre del primer comprador de orquídeas importadas: {primernombre}")
        print(f"Monto de la compra: Bs {primermonto}")
        print(f"{primernombre} fue el único comprador de orquídeas importadas")
    if orquideas >1:
        print(f"Nombre del primer comprador de orquídeas importadas: {primernombre}")
        print(f"Monto de la compra: Bs {primermonto}")
        print(f"Nombre del último comprador de orquídeas importadas: {ultimonombre}")
        print(f"Monto de la compra: Bs {ultimomonto}")
        
    #4. Porcentaje de ramos de orquídeas nacionales compradas.
    if ramosorquideas >=1:
        porc = (ramosorquideas /ramostotales)*100
        print(f"Porcentaje de ramos de orquídeas nacionales compradas: {porc:6.2f} %")
    else:
        print("No se compraron ramos de orquideas nacionales")
