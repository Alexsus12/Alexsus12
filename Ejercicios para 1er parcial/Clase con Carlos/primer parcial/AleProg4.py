                                # Uso del comando "while"
                                # Dado un grupo de personas, de las que se conoce: nombre, edad, genero (1. femenino, 2. masculino). Det:
                                #1. promedio de edad
                                #2 porc de mayores de edad
                                #3 promedio de edad de las mujeres
continuar = 1
sumaE = 0
numP = 0
mayoresdeEdad = 0
femenino = 0
SumaM = 0
while continuar ==1 :
    nombre = str(input("Escriba el nombre: "))
    edad = int(input("Indique la edad de esa persona: " ))
    genero = int(input("¿Género? - 1) Femenino. 2) Masculino "))
    continuar = int(input("¿Desea seguir? (1 = si     0 = no)? "))
    sumaE = sumaE + edad  # Acumula las edades (Acumulador) #1) PROMEDIO DE EDAD
    numP = numP + 1 # Cuenta personas (Contador)
    if edad >= 18: # 2) PORCENTAJE DE MAYORES DE EDAD
        mayoresdeEdad = mayoresdeEdad + 1 # cuenta mayores de edad
    if genero == 1: #3) PORCENTAJE DE EDAD DE LAS MUJERES
        femenino = femenino + 1 # Cuenta mujeres 
        SumaM = SumaM + edad # Suma edades
        
# PROMEDIO DE EDAD
prom = sumaE / numP # Como necesito hacer un promedio final entonces irá fuera del ciclo while (sale de su indentación) para que no se repita el ciclo.
print(f"El promedio de las edades es {prom:6.2f} años")

# PORCENTAJE DE MAYORES DE EDAD
porc = (mayoresdeEdad / numP)*100
print(f"El porcentaje de mayores de edad es del {porc:6.2f} % ")

# PORCENTAJE DE EDAD DE LAS MUJERES
if femenino > 0: #Sí procesé mujeres :)
    promE = SumaM / femenino
    print(f"El promedio de edad de las mujeres es de {promE} años")
else:
    print("No se procesaron mujeres :(") 
    