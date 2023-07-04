A = 1
niños = 0
adultos = 0
pagoadultos = 0
pagoniños = 0
P = 0
while A == 1:
    P += 1
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    tiempo = float(input("tiempo recorrido en el parque EN MINUTOS: "))

    if edad < 10:
        niños += 1
        pagoniños += 100 
    
    else:
        adultos += 1
        pagoadultos += 200
        
    if edad < 10 and tiempo > 60:
        ult_visit = nombre
    A =int(input("¿Era el último visitante?: 1 = No / 2 = Sí "))
    
#Porcentaje de niños que asistieron al parque
porcnin = (niños/P)*100
print(f"El porcentaje de niños que asistieron al parque es del {porcnin} %")

#¿Cuánto dinero en total recaudo el parque por todos los visitantes adultos que recibió?
print(f"El dinero total recaudado por adultos es de Bs {pagoadultos:6.2f}")

#Un mensaje que indique si el funcionamiento del parque es rentable o no.
recaudacion = pagoadultos + pagoniños
if recaudacion > 150000:
    print("El funcionamiento del parque es rentable")
else:
    print("El funcionamiento del parque NO es rentable")
    
#Nombre del último visitante niño que recorrió el zoológico en más de una hora
print(f"El nombre del último niño que visitó más de una hora el paque es {ult_visit} ")