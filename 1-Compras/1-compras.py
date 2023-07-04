terminar = 0
maximo = 0
codigodelmayor= ""
dolares = 0
articulo = 0
B = 0
excento = 0

while terminar == 0:
    codigo = input("Ingrese el código del artículo: ")
    cantidad = int(input("Indique la cantidad de ese artículo: "))
    preciodolar = float(input("Precio del artículo (en dólares): $ "))
    impuesto = int(input("¿Tipo de impuesto? -- 0: Exento (0 %) -- 1: No exento (21 %) "))
    
    #CONTADORES DE PRECIOS UNITARIOS
    if preciodolar > maximo:
        maximo = preciodolar 
        codigodelmayor = codigo      
    
    #CONTADOR DE ARTICULOS
    articulo = articulo + cantidad 
    
    #MONTO TOTAL DOLARES
    totaldolares = preciodolar * cantidad
    print(f"Su monto total en dólares es: $ {totaldolares:6.2f}")
    
    #MONTO TOTAL BOLÍVARES
    totalbolivares = totaldolares*4.6
    print(f"Su monto en bolívares es de: Bs {totalbolivares:6.2f}") 
    B = B + totalbolivares #ACUMULADOR DEL TOTAL DE BOLÍVARES 
    
    #IMPUESTO A PAGAR 
    if impuesto == 1:
        impapagar = totalbolivares * 0.21
        print(f"El impuesto a pagar es de: Bs {impapagar:6.2f}")
    if impuesto ==0:
        impapagar = 0
        print(f"El impuesto a pagar en bolívares es de {impapagar:6.2f}")
    terminar = int(input("""
                         ¿Ha terminado de ingresar todos sus productos? 
                                   0: no                1: si 
                                                """))
    
    #PORCENTAJES DE ARTICULOS EXCENTOS A PAGAR
    if impuesto == 0:
        excento = excento + cantidad

#TOTAL A PAGAR
print(f"Su total a pagar es de: Bs {B:6.2f}")

#PORCENTAJE DE ARTICULOS EXCENTOS DE IMPUESTOS
porc = (excento/articulo)*100
print(f"El porcentaje de articulos excentos de impuestos es del {porc:6.2f}")

#CODIGO DEL ARTÍCULO CON MAYOR PRECIO UNITARIO
print(f"El artículo con mayor precio por unidad es el del código {codigodelmayor}")