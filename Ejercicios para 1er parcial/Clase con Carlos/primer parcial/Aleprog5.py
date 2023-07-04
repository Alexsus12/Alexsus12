N = int(input("¿Cuántas encuestas desea realizar?: "))
mayor = 0
menor= 0
for x in range(N):
    modelo = input("Ingrese el modelo del celular: ")
    PP = float(input("Del 1 al 10 indique la puntuación del celular en perfomance: "))
    PD = float(input("Del 1 al 10 indique la puntuación del celular en diseño: "))
    PA = float(input("Del 1 al 10 indique la puntuación del celular en autonomía: "))
    suma = 0.45*PP + 0.30*PA + 0.25*PD #ESTE ES EL PUNTAJE DEFINITIVO Y ESTA FORMULA FUE DADA POR EL ENUNCIADO
    
    #A) PUNTUACIÓN DEFINITIVA DE CADA MODELO
    print(f"La puntuación definitiva de este modelo de celular es de {suma:6.2f} puntos")
    
    #B) PORCENTAJE DE CELULARES CON PUNTUACIÓN DEFINITIVA MAYOR O IGUAL A 7 Y 
    #C) CANTIDAD DE CELULARES CON PUNTAJE DEFINITIVO MENORES A 7
    if suma >= 7:
        mayor = mayor + 1 #CONTADOR DE PUNTUACIONES MAYORES O IGUALES A 7
        
    else:
        menor = menor + 1 #CONTADOR DE PUNTUACIONES MENORES A 7
    porc = (mayor/N)*100

    #D) MODELO DEL CELULAR CON MAYOR PUNTUACIÓN DEFINITIVA 
    if x == 0: 
        maximo = suma #ESTO INDICA QUE PARA LA PRIMERA VUELTA (X == 0) EL MÁXIMO PORCENTAJE DEFINITIVO SERÁ EL PRIMERO QUE SE INGRESE
        modelmaximo = modelo #ESTO INDICA QUE EL NOMBRE DEL MODELO CON MAYOR PORCENTAJE DEFINITIVO SERÁ EL PRIMERO
        
    elif suma > maximo: #ESCRIBIMOS ESTO PARA DAR LAS INSTRUCCIONES QUE SE DARÁN EN LA SEGUNDA VUELTA EN CASO DE HABERLA
        maximo = suma
        modelmaximo = modelo #CON ESTO ESPECIFICAMOS QUE SI EN LA VUELTA NUEVA EL VALOR INGRESADO ES MAYOR, ENTONCES SE SOBREESCRIBEN LOS VALORES ANTERIORES 
       
print(f"El porcentaje de celulares con puntuación definitiva mayor o igual a 7 es del {porc:6.2f}")   
     
print(f"El número de celulares con puntuación definitiva menores a 7 es de {menor} celulares")
#ESTE ÚLTIMO TAMBIÉN SE PUDO ESCRIBIR COMO: print("el número de celulares es de {N - mayor} celulares")   

print(f"El celular con mayor puntaje definitivo es el modelo {modelmaximo}")