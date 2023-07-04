K = int(input("¿Cuántos contratos de alquiler se realizarán?: "))
tipo1 = 0
tipo2 = 0
tipo3 = 0
suma1 = 0
suma2 = 0 
suma3 = 0
suma1a = 0
suma2a = 0
suma3a = 0
sumaalta1 = 0
sumaalta2 = 0
sumaalta3 = 0

for x in range(K):
    nombre = input("Por favor, ingrese su nombre: ")
    cedula = input("Por favor, ingrese su número de cédula: ")
    apartamento = int(input("""
                            Escoja el tipo de apartamento que desee alquilar:
                                    Tipo 1 -- ingrese el número 1
                                    Tipo 2 -- ingrese el número 2
                                    Tipo 3 -- ingrese el número 3  
                                                """))
    temporada = int(input("""
                                            ¿Tipo de temporada?
                                    Baja = 1                    Alta = 2 
                                                       """))
    cantidad = int(input("Noches que desea quedarse: "))
    
    #MONTO TOTAL A PAGAR POR ALQUILER DEL APARTAMENTO CON TEMPORADA BAJA
    if apartamento == 1 and temporada == 1:
        noche1 = cantidad*580
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 1 es de Bs {noche1:6.2f}")
        suma1 = suma1 + noche1 #ACUMULADOR DE BS PARA EL APARTAMENTO TIPO 1
     
    if apartamento == 2 and temporada == 1:
        noche2 = cantidad*650
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 1 es de Bs {noche2:6.2f}")
        suma2 = suma2 + noche2 #ACUMULADOR DE BS PARA EL APARTAMENTO TIPO 2
        
    if apartamento == 3 and temporada ==1:
        noche3 = cantidad*715
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 3 es de Bs {noche3:6.2f}")
        suma3 = suma3 + noche3 #ACUMULADOR DE BS PARA EL APARTAMENTO TIPO 3
        
    #MONTO TOTAL A PAGAR POR ALQUILER DEL APARTAMENTO CON TEMPORADA ALTA
    if apartamento == 1 and temporada == 2:
        noche1a = cantidad*580 + 580*0.1
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 1 es de Bs {noche1a}")
        sumaalta1 = sumaalta1 + noche1a #ACUMULADOR DE BS PARA EL APARTAMENTO TIPO 1 EN TEMPORADA ALTA
        suma1a = suma1a + 1 #CONTADOR DE ALQUILERES DEL APARTAMENTO TIPO 1 EN TEMPORADA ALTA
        
    if apartamento == 2 and temporada ==2:
        noche2a = cantidad*650 + 650*0.1
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 1 es de Bs {noche2a:6.2f}")
        sumaalta2 = sumaalta2 + noche2a #ACUMULADOR DE BS PARA EL APARTAMENTO TIPO 2 EN TEMPORADA ALTA
        suma2a = suma2a + 1 #CONTADOR DE ALQUILERES DEL APARTAMENTO TIPO 2 EN TEMPORADA ALTA
        
    if apartamento == 3 and temporada ==2:
        noche3a = cantidad*715 + 715*0.1
        print(f"El monto total a pagar por {cantidad} noches en el apartamento tipo 3 es de Bs {noche3a:6.2f}")
        sumaalta3 = sumaalta3 + noche3a 
        suma3a = suma3a + 1 #CONTADOR DE ALQUILERES DEL APARTAMENTO TIPO 3 EN TEMPORADA ALTA
        
    #PORCENTAJES DE APARTAMENTOS ALQUILADOS DE CADA TIPO (VARIABLES INTERNAS):
    if apartamento == 1:
        tipo1 = tipo1 + 1   #CONTADOR DE APARTAMENTOS TIPO 1
    if apartamento == 2:
        tipo2 = tipo2 + 1   #CONTADOR DE APARTAMENTOS TIPO 2
    if apartamento == 3:
        tipo3 = tipo3 + 1   #CONTADOR DE APARTAMENTOS TIPO 3

#PORCENTAJES DE APARTAMENTOS ALQUILADOS DE CADA TIPO (IMPRESIÓN):
porc1 = (tipo1/K)*100
print(f"El porcentaje de apartamentos tipo 1 alquilados es del {porc1:6.2f} ")
porc2 = (tipo2/K)*100
print(f"El porcentaje de apartamentos tipo 2 alquilados es del {porc2:6.2f} ")
porc3 = (tipo3/K)*100
print(f"El porcentaje de apartamentos tipo 3 alquilados es del {porc3:6.2f} ")

#MONTO TOTAL QUE RECIBIRÁ LA EMPRESA POR EL ALQUILER DE LOS APARTAMENTOS
total = suma1 + suma2 + suma3 +sumaalta1 + sumaalta2 + sumaalta3
print(f"El monto total que recibirá la empresa por el alquiler de los apartamentos es de {total}")

#MONTO PROMEDIO DEL ALQUILER DE LOS APARTAMENTOS EN TEMPORADA ALTA
promalta = (suma1a + suma2a + suma3a)/K
print(f"El promedio es de {promalta:6.2f} alquileres de apartamentos en temporada alta")