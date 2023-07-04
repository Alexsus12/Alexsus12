terminar = 0
N = 0
totalhoras = 0 
P = 0
while terminar == 0:
    nombre = input("Ingrese su nombre: ")
    dia = int(input("""
                                Ingrese un día de la semana
                    0 = Lunes -- 1 = Martes -- 2 = Miércoles -- 3 = Jueves 
                        4 = Viernes -- 5 = Sábado -- 6 = Domingo
                                            """))
    diurnas = int(input("""
                            ¿Número de horas diurnas trabajadas?:
                        (Si no laboró en este turno ingrese el número 0)
                                            """))
    nocturnas = int(input("""
                          ¿Número de horas nocturnas trabajadas?:
                        (Si no laboró en este turno ingrese el número 0)
                                            """))
    
    #CONTADOR DE PERSONAS
    P = P + 1
    
    #DEDUCCIÓN DE JORNALES
    if dia != 6:
        tardiurna = diurnas*10
        tarnocturna = nocturnas*15
        jornalltotal =  tardiurna + tarnocturna
        print(f"Su jornal diario es de Bs {jornalltotal}")
    if dia == 6:
        tardiurna = diurnas*50
        tarnocturna = nocturnas*100
        jornalltotal =  tardiurna + tarnocturna
        print(f"Su jornal diario es de Bs {jornalltotal}")
    
    #TRABAJADORES QUE TRABAJARON MÁS HORAS NOCTURNAS QUE DIURNAS
    if nocturnas > diurnas:
        N = N + 1 #CONTADOR DE PERSONAS QUE TRABAJARON MÁS HORAS NOCTURNAS QUE DIURNAS
    
    #ACUMULADOR DE HORAS TRABAJADAS 
    totalhoras = totalhoras + diurnas + nocturnas
    
    terminar = int(input("""
                     ¿Se han ingresado todos los trabajadores del día?
                     No = 0                  --                Sí =  1
                                            """))
    
#PORCENTAJE DE TRABAJADORES QUE TRABAJARON MÁS HORAS NOCTURNAS QUE DIURNAS
porc = (N/P)*100
print(f"El porcentaje de trabajadores que trabajaron más horas nocturnas que diurnas es del {porc:6.2f} %")

#PROMEDIO DE HORAS TRABAJADAS
prom = (totalhoras)/P
print(f"El promedio de horas trabajadas por los trabajadores de la fábrica es de {prom:6.2f} horas")