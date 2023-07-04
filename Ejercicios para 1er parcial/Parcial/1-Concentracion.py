solutototal = float(input("Cantidad total de soluto (Kg): "))
solventetotal = float(input("Cantidad total de solvente (Kg): "))
A = 1
solutototal = solutototal*1000 #Para transformar lo que me dieron a gramos
solventetotal = solventetotal*1000
storestante = solutototal
sterestante = solventetotal
exptotal = 0
expreal = 0
acumconcent = 0
noreal = 0

while A == 1:
    sto = float(input("Cantidad de soluto a utilizar (gramos): "))
    ste = float(input("Cantidad de solvente a utilizar (gramos): "))
    exptotal += 1
    
    #1. Concentración de la solución expresado como % en
    #masa y si pudo realizarse o no. (2 ptos)
    if sto <= storestante and ste <= sterestante:
        expreal += 1 
        porcmasa = (sto/(sto+ste))*100
        print("Pudo realizarse la concentración.")
        print(f"Concentración de la solución: {porcmasa:6.2f} %")
        acumconcent += porcmasa
        storestante -= sto
        sterestante -= ste 
    
    else:
        print("No pudo realizarse la concentración")
        noreal += 1 
        if noreal == 2:
            numero2 = exptotal
            if sto > storestante and ste < sterestante:
                Respuesta = "Falta de soluto."

            if ste > sterestante and sto < sterestante:
                Respuesta = "falta de solvente."
            
            if ste > sterestante and sto > storestante:
                Respuesta = "Falta de soluto y de solvente."
    
    A = int(input("¿Desea realizar otra experiencia?: 1: Sí / 2: No "))      

#2. Porcentaje de experiencias que se pudieron realizar con las cantidades de soluto y solvente
#disponibles. (2 ptos)
porcexp = (expreal/exptotal)*100
print(f"Porcentaje de experiencias realizadas: {porcexp:6.2f} %")

#3. Concentración promedio de las experiencias que se pudieron realizar. (2 ptos)
if expreal !=0:
    prom = acumconcent / expreal
    print(f"La concentración promedio de experiencias realizadas es: {prom:6.2f} %")
else:
    print("No se pudo realizar ninguna experiencia")

#4. Número de la segunda experiencia que no pudo realizarse, por no disponer de los reactivos necesarios,
#indicando si fue por falta de soluto o de solvente o ambos. (4 ptos)
if noreal >= 2:
    print(f"Número de la segunda experiencia que no pudo realizarse: {numero2}")
    print(Respuesta)
else:
    print("No hubo segunda experiencia que no se pudiera realizar")
    
#5. Un mensaje final que indique si se pudieron o no realizar todas las experiencias programadas, y las
#cantidades que quedaron de soluto y de solvente. (2 ptos)
if noreal == 0:
    print("Se pudieron realizar todas las experiencias programadas")
    storestante /= 1000
    sterestante /= 1000
    print(f"Cantidad restante de soluto: {storestante:6.2f} Kg")
    print(f"Cantidad restante de solvente: {sterestante:6.2f} Kg")
else:
    print("No se pudieron realizar todas las experiencias programadas")
    storestante /= 1000
    sterestante /= 1000
    print(f"Cantidad restante de soluto: {storestante:6.2f} Kg")
    print(f"Cantidad restante de solvente: {sterestante:6.2f} Kg")