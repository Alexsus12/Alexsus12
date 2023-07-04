f = open("notas.txt","r") #Abrimos el programa, por lo que debemos crear un archivo .txt en la pc así esté en blanco
#En este caso hice un archivo con los datos para entender mejor lo que se hace, pero en posteriores ejercicios no lo haré.
g = open("definitivas.txt","w") #Aquí especificamos que al programa que cree un archivo .txt llamado "definitivas.txt" 

linea = f.readline() #readline() nos permite leer la primera línea del archivo notas.txt
datos = linea.strip().split(",") #Aquí transformamos esa línea leída en una lista mediante split(",") y como el archivo tiene separaciones con comas
#entonces dentro del () se especifica que su separación de lista serán las comas strip() lo que hizo fue eliminar los espacios que pudieran haber quedado (\n)
p1 = int(datos[0]) #Como split() siempre transforma a toda la lista de la línea en str, entonces el siguiente paso es a cada valor de la lista volverlo int 
p1 = int(datos[1]) #Eso quiere decir que entonces, por ejemplo, el dato de la primera lista en la posición 2 (35) se transforma a int
p1 = int(datos[2]) #Lo mismo para este.
asis_total = int(datos[3])
sec_reporte = int(input("¿Cuál sección reporto?: ")) #Aquí preguntamos si quiere la sección 91 o 92 por saber sus definitivas
s = 0
c = 0
cap = 0
asisperfect = 0

for linea in f: #con este for lo que hacemos es leer línea por línea el archivo "notas.txt" a partir de la segunda línea porque la primera ya se leyó
    datos = linea.strip().split(",") #Lo mismo que al principio para hacer una lista de cada línea nueva que se lea
    sec = int(datos[0]) #Para esta línea nueva la sección es la posición 0
    cedula = datos[1]
    nombre = datos[2]
    asistencia = int(datos[3])
    nota1 = int(datos[4])
    nota2 = int(datos[5])
    nota3 = int(datos[6])
    
    definitiva = (nota1*25 + nota2*35 + nota3*40)/100 #Definitiva de esa persona en esa línea
    definitiva = round(definitiva) #round() lo que hace es redondear al número par más cercano. Con esto se redondea la definitiva
    
    if asistencia == asis_total and definitiva < 20: #Nos aseguramos que la definitiva no sea 20 puntos porque es el puntaje máximo
        definitiva += 1    
        
    #2. Porcentaje de estudiantes con asistencia perfecta (2 ptos)
    porcasist = (asistencia/asis_total)*100 #Y sabemos que si el resultado es 100, es porque la asistencia fue perfecta
    if porcasist == 100:
        asisperfect += 1 
        
    if sec == sec_reporte: #Si la sección de esta línea coincide con la sección que reportó
        g.write(f"{cedula}    {nombre}    {porcasist}    {definitiva}") #Con esto especificamos que se escriba en el archivo definitivas
        g.write("\n") #aquí indicamos que una vez imprima eso para la próxima vez lo haga en una línea nueva (Para eso sirve el "\n")
        s += definitiva #Acumulador de definitivas para la sección pedida
        c += 1   
        if c ==1:
            menorasist = asistencia
            nombremenor = nombre
        elif asistencia < menorasist:
            menorasist = asistencia
            nombremenor = nombre
        
f.close()
g.close() #Recordar cerrar los archivos al terminar FUERA DEL CICLO
    
#1.
print(f"Nombre del estudiante con la menor asistencia: {nombremenor}")

#2.
porc = (asisperfect/c)*100
print(f"Porcentaje de asistencia perfecta de la sección: {porc:6.2f} %")

#3. Definitiva promedio de la sección (1 pto)
prom = s/c
print(f"La definitiva promedio de la sección {sec_reporte} es: {prom:6.2f} puntos")