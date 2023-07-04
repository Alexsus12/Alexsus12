f = open("Pacientes.txt","r")
g = open("Denque.txt","w")
h = open("Chikungunya.txt","w")
q = open("Zika.txt","w")
dengue = 0
chikungunya = 0
zika = 0
ninguno = 0
pacientes = 0

linea = f

for linea in f:
    datos = linea.strip().split(",")
    nombre = datos[0]
    edad = int(datos[1])
    diagnostico = int(datos[2])
    
    pacientes +=1
    
    if diagnostico ==1:
        dengue += 1
        g.write(f"Nombre: {nombre} -- Edad: {edad} \n")
        
    if diagnostico ==2:
        chikungunya += 1
        h.write(f"Nombre: {nombre} -- Edad: {edad} \n")

    if diagnostico ==3:
        zika += 1
        q.write(f"Nombre: {nombre} -- Edad: {edad} \n")
        
    if diagnostico ==4:
        ninguno += 1

if pacientes !=0:
    porc1 = (dengue/pacientes)*100
    g.write(f"Porcentaje de pacientes infectados de Dengue: {porc1:6.2f} %")
    
    porc2 = (chikungunya/pacientes)*100
    h.write(f"Porcentaje de pacientes infectados de Chikungunya: {porc2:6.2f} %")
    
    porc3 = (zika/pacientes)*100
    q.write(f"Porcentaje de pacientes infectados de Zika: {porc3:6.2f} %")
    
    f.close()
    g.close()
    h.close()
    q.close()
    
    #cual es la enfermedad con más pacientes infectados en el país.
    if dengue > chikungunya and dengue > zika:
        print("Enfermedad con más pacientes infectados en el país: Dengue")
        
    if chikungunya >  dengue and chikungunya > zika:
        print("Enfermedad con más pacientes infectados en el país: Chikungunya")
        
    if zika > chikungunya and zika > dengue:
        print("Enfermedad con más pacientes infectados en el país: Zika")
        
    if zika == chikungunya == dengue:
        print("Las tres enfermedades tienen el mismo número de infectados")
    
    if zika == chikungunya and zika > dengue:
        print("Enfermedades con más pacientes infectados en el país: Zika y Chikunguya")
    
    if zika == dengue and zika > chikungunya:
        print("Enfermedades con más pacientes infectados en el país: Zika y Dengue")
        
    if dengue == chikungunya and dengue > zika:
        print("Enfermedad con más pacientes infectados en el país: Dengue y Chikunguya")
        
else:
    print("La lista está vacía")
        