                    # Porcentajes de valores mayores a 45
c = 0                   
S = 0 # Debe ir inicialmente porque si lo meto dentro del for se va a resetear N veces
N = int(input("¿Cuántos valores se leen? "))
for i in range(N): # i hace función de un indicador, por lo que es necesaria colocarla
    x = int(input("Valor x: "))
    if x > 45:
        c = c + 1 # Esto es un contador porque suma de manera constante
porc = (c / N)*100
print(f"El porcentaje de valores mayores a 45 es {porc:6.2f} %")