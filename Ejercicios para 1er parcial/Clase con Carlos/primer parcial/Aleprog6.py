from math import pi #PARA TRAER EL NÚMERO PI
M = int(input("Ingrese la cantidad de solicitudes: "))
X = float(input("El costo por metro cuadrado del acero (en dólares): $ "))
tasa = float(input("Ingrese la tasa Bs/USD al día de hoy: "))
T = X*tasa
tipo1 = 0
tipo2 = 0
costo2a = 0
costo1a = 0 

for x in range(M):
    empresa = input("Ingrese el nombre de la empresa solicitante: ")
    tipo = int(input("¿Tipo de tanque? - 1 = Cilindro circular recto -- 2 = Cilindro circular recto con semiesferas en los extremos "))
    R =float(input("Ingrese el valor del radio (en pies): "))
    L = float(input("Ingrese la longitud (en pies): "))
     
    if tipo == 1:
        tipo1 = tipo1 +1
        if tipo1 == 1: #AQUI INDICAMOS QUE PARA EL PRIMER VALOR TIPO 1 SE GUARDARÁ EL NOMBRE DE LA EMPRESA
            primeraempresa = empresa
        R= R*0.3048 
        L= L*0.3048
        Vc1 = pi*R**2*L
        print(f"El volumen del recipiente a diseñar es de {Vc1:6.2f} metros cùbicos")
        costo1 = (2*pi*R*L + 2*pi*R**2)*T
        print(f"el costo del recipiente es de Bs {costo1:6.2f}")
        
    if tipo == 2:
        tipo2 = tipo2 + 1
        R= R*0.3048 
        L= L*0.3048
        Vc2 = pi*R**2*L + (4/3)*pi*R**3
        print(f"El volumen del recipiente a diseñar es de {Vc2:6.2f} metros cùbicos")
        costo2 = (4*pi*R**2 + 2*pi*R*L)*T
        print(f"el costo del recipiente es de Bs {costo2:6.2f}")
        costo2a = costo2a + costo2
        
porc2 = (tipo2/M)*100
print(f"El porcentaje de tanques tipo 2 solicitados es del {porc2:6.2f} %")
if tipo2 != 0:
    prom2 = costo2a / tipo2
    print(f"El promedio del costo en bolívares de los tanques tipo 2 solicitados es de {prom2:6.2f} bolívares")
else:
    print("No fueron solicitados tanques tipo 2")
    
if tipo1 >= 1:
    print(f"La empresa que solicitó el primer tanque tipo 1 es {primeraempresa}")
else:
    print("No hubo empresa que solicitara tanques tipo 1")
    