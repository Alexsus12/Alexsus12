cantprincipal = 0
hi5 = 0
myspace = 0
facebook = 0
nombreprim = "nombre"

W = int(input("¿A cuántas personas se le realizará la encuesta?: ")) 
for x in range(W):
    nombre = input("Ingrese su nombre: ")
    genero = int(input("¿Género?: 1: Femenino / 2: Masculino "))
    edad = int(input("Ingrese su edad: "))
    redsocial = int(input("Ingrese la red social más usada: 1: Facebook /  2: Myspace / 3: Hi5 / 4: Ninguna "))
    
    if 1 <= redsocial <= 3:
        cantprincipal += 1
        if redsocial == 3:
            hi5 += 1 
            if hi5 ==1:
                nombreprim = nombre
                edadprim = edad
        if redsocial == 2:
            myspace += 1
        if redsocial == 1:
            facebook += 1
    

#Cantidad de personas encuestadas que utilizan
# cada uno de las tres principales redes sociales
# considerados en la encuesta (2 ptos)
print(f"Hubo {cantprincipal} {'persona' if cantprincipal == 1 else 'personas'} que utilizaron las redes sociales consideradas en la escuesta")

#Porcentaje de personas encuestadas que utilizan
#alguna de las tres principales redes sociales(2 ptos)
porc = (cantprincipal/W)*100
print(f"El porcentaje de personas que utilizaron las redes sociales principales es del: {porc:6.2f} %")

#Nombre y edad de la primera persona encuestada que usa hi5 (3 ptos)
if nombreprim == "nombre":
    print("No hubo persona que usara Hi5")
else:
    print(f"{nombreprim}, de {edadprim} {'año' if edadprim == 1 else 'años'} fue la primera persona encuestada en usar Hi5")

#¿En cuál de las tres redes sociales sería más rentable invertir en publicidad? (3.5 ptos)
if facebook > myspace and facebook > hi5:
    print("Es más rentable invertir publicidad en Facebook")
if myspace > facebook and myspace > hi5:
    print("Es más rentable invertir publicidad en Myspace")
if hi5 > myspace and hi5 > facebook:
    print("Es más rentable invertir publicidad en Hi5")
if facebook == myspace and facebook > hi5:
    print("Es rentable invertir publicidad en Facebook o Myspace")
if facebook == hi5 and facebook > myspace:
    print("Es rentable invertir publicidad en Facebook o Hi5")
if hi5 == myspace and hi5 > facebook:
    print("Es rentable invertir publicidad en Hi5 o Myspace")
if hi5 == myspace == facebook:
    print("Es rentable invertir en cualquiera de la tres redes sociales")
