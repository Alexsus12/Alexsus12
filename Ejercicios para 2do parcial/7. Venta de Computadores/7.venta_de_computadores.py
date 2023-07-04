f = open("Ventas.txt","r")
g = open("Salida.txt","w")
linea = f
acum1 = 0
acum2 = 0
acum3 = 0
quadcore = 0
p = 0
dualcore = 0
unidadestotales = 0
tipo2 = 0

for linea in f:
    datos = linea.strip().split(",")
    nombre = datos[0]
    tipo = int(datos[1])
    precio =float(datos[2])
    unidadesvend = int(datos[3])
    
    p+=1
    unidadestotales += unidadesvend
    
    if tipo ==1:
        montototal1 = precio*unidadesvend
        acum1 += montototal1 
    
    if tipo ==2:
        tipo2 += 1 
        dualcore += unidadesvend
        montototal2 = precio*unidadesvend
        acum2 += montototal2
    
    if tipo ==3:
        quadcore += unidadesvend
        montototal3 = precio*unidadesvend
        acum3 += montototal3

if p !=0:
    #1. Monto total de las ventas por tipo de procesador.
    g.write(f"Monto total -> Proc. Simple: $ {acum1:6.2f} \n")
    g.write(f"Monto total -> Proc. Dualcore: $ {acum2:6.2f} \n")
    g.write(f"Monto total -> Proc. Quadcore: $ {acum3:6.2f} \n")
    
    #2. Porcentaje de Procesadores tipo Quad Core.
    porc = (quadcore/unidadestotales)*100
    g.write(f"Porcentaje de Procesadores tipo Quad Core Vendidas: {porc:6.2f} % \n")
        
    #3. Promedio de unidades vendidas de procesadores tipo DUAL CORE por cliente.
    prom = dualcore/tipo2
    g.write(f"Promedio de unidades vendidas de procesadores tipo DUAL CORE por cliente: {prom:6.2f} unidades \n")

else:
    print("La lista a leer está vacía")
f.close()
g.close()
