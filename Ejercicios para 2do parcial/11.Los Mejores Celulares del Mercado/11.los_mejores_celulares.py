f = open("Encuesta.txt","r")
g = open("Definitivas.txt","w")

c1 = 0
c2 = 0
for linea in f:
    datos = linea.strip().split(",")
    modelo = datos[0]
    perfomance = float(datos[1])
    diseño = float(datos[2])
    autonomia = float(datos[3])
    c1 += 1
    
    pdef = 0.45*perfomance + 0.30*autonomia + 0.25*diseño
    
    #1. Para cada modelo de celular la puntuación definitiva
    g.write(f"modelo: {modelo} -- Puntuación def: {pdef:6.2f} \n")
    
    #2. Modelo de celular con mayor puntuación definitiva y el que tenga menor puntuación definitiva
    if c1 ==1:
        modelomayor = modelo
        mayor = pdef
        menor = pdef
        
    elif pdef > mayor:
        modelomayor = modelo
        mayor = pdef
        
    elif pdef < menor:
        modelomenor = modelo
        menor = pdef
        
    #3. Porcentaje de celulares que obtuvieron una puntuación definitiva mayor o igual a 7
    if pdef >=7:
        c2 += 1 

g.write(f"Modelo de celular con mayor puntuación definitiva: {modelomayor} \n")
g.write(f"Modelo de celular con menor puntuación definitiva: {modelomenor} \n")
porc = (c2/c1)*100
g.write(f"Porcentaje de celulares que obtuvieron una puntuación definitiva mayor o igual a 7: {porc:6.2f} \n")

f.close()
g.close()
