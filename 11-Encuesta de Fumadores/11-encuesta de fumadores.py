cont_caracas = 0
cont_valencia = 0
cont_edad_mayor = 0
cont_mujeres = 0
acum_cigarrillo = 0
caracasmasculino = 0
N = int(input("¿Cuántas encuestas procesará?: "))
for x in range(N):
    ciudad = input("¿Ciudad?: C = Caracas / V = Valencia ")
    ciudad = ciudad.upper()
    nombre = input("Ingrese el nombre: ") 
    edad = int(input("Ingrese la edad: "))
    genero = int(input("¿Género?: 1: Femenino / 2: Masculino "))
    marca = input("Marca que fuma: ")
    cantidad = int(input("Cantidad de cigarrillos consumidos al día: "))
    
    #1. Indique si el fumador está en riego o no de contraer una enfermedad pulmonar
    if cantidad >= 10:
        print("Está en riesgo de contraer una enfermedad pulmonar")
        if ciudad == "C":
            cont_caracas += 1 
        
        if ciudad == "V":
            cont_valencia += 1
            if edad > 40:
                cont_edad_mayor += 1  
                if cont_edad_mayor == 1: #De esta manera solo guardamos los datos del primero
                    nombreprimero40 = nombre
                    marcaquefuma = marca
                    
    if ciudad == "V" and genero == 1:
            cont_mujeres += 1
            acum_cigarrillo += cantidad
    
    if ciudad == "C" and genero == 2:
        caracasmasculino += 1 
        
#2. Ciudad con el porcentaje más alto de fumadores de contraer una enfermedad pulmonar.
porccaracas = (cont_caracas/N)*100
porcvalencia = (cont_valencia/N)*100

if porccaracas > porcvalencia:
    print("La ciudad con porcentaje más alto de contraer los fumadores una enfermedad pulmonar es Caracas")
elif porccaracas == porcvalencia:
    print("Ambas ciudades tienen el mismo porcentaje de fumadores en contraer una enfermedad pulmonar")
else:    
    print("La ciudad con porcentaje más alto de contraer los fumadores una enfermedad pulmonar es Valencia")

#3. Nombre del fumador y marca que fuma del primer fumador con riesgo de contraer una enfermedad pulmonar, con edad superior
#a 40 años y es de Valencia.
print(f"Nombre del primer fumador de Valencia con riesgo de contraer una enfermedad pulmonar, mayor de 40 años: {nombreprimero40}")
print(f"Marca que fuma: {marcaquefuma}")

#4. Promedio de cigarrillos consumidos por el género femenino en la ciudad de Valencia.
prom = acum_cigarrillo / cont_mujeres
print(f"Promedio de cigarrillos consumidos por el género femenino en la ciudad de Valencia: {prom:6.2f} {'cigarrillo' if prom == 1 else 'cigarrillos'}")

#5. Cuantos fumadores se procesaron de Caracas y de género masculino.
print(f"Se {'procesó' if caracasmasculino == 1 else 'procesaron'} de Caracas y de género masculino {caracasmasculino} {'fumador' if caracasmasculino == 1 else 'fumadores'}")