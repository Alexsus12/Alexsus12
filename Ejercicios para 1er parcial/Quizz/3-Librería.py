A = 1
cont_300mas = 0
L = 0
paginas1 = 0
tasa = float(input("Ingrese la tasa del dolar actual: Bs "))
precio1bs = 0
precio2bs = 0
precio3bs = 0

while A==1:
    
    codigo = input("Ingrese código del libro: ")
    paginas = int(input("Número de páginas que contiene: "))
    L += 1
    
    #1. (3 ptos) El código y el precio de cada uno de los libros registrados.
    if paginas <= 300:
        precio1 = 5 + paginas*0.20
        print(f"El código del libro es {codigo}")
        print(f"El precio del libro es $ {precio1:6.2f}")
        paginas1 += paginas 
        precio1bs += precio1*tasa
        
    if 300 < paginas <= 550:
        precio2 = 15 + paginas*0.20
        print(f"El código del libro es {codigo}")
        print(f"El precio del libro es $ {precio2:6.2f}")
        cont_300mas += 1 
        paginas1 += paginas
        precio2bs += precio2*tasa
       
    if paginas > 550:
        precio3 = 22.5 + paginas*0.20
        print(f"El código del libro es {codigo}")
        print(f"El precio del libro es $ {precio3:6.2f}")
        cont_300mas += 1
        paginas1 += paginas
        precio3bs += precio3*tasa
        
    A = int(input("¿Desea agregar más libros? -- 1: Sí / 2: No "))
        
#(2 ptos) Porcentaje de libros cuyo número de páginas excede las 300 páginas.
porc = (cont_300mas / L)*100
print(f"Porcentaje de libros cuyo número de páginas excede las 300 páginas: {porc:6.2f} %")

#(2 ptos) Promedio de páginas que tienen los libros de la librería.
prom = paginas1/L
print(f"El promedio de páginas que tienen los libros de la librería es de {prom:6.2f} {'página' if prom == 1 else 'paginas'}")

#(3 ptos) Monto total en Bs. del conjunto de libros. El valor del $ en Bs es un dato que debe ser leído desde el
#teclado.

totalbs = precio1bs + precio2bs + precio3bs
print(f"Monto total: Bs {totalbs:6.2f}")