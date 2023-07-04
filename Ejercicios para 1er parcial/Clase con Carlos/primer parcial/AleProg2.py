                    # Determinar el promedio de N valores enteros
                    
S = 0 # Debe ir inicialmente porque si lo meto dentro del for se va a resetear N veces
N = int(input("¿Cuántos valores se leen? "))
for i in range(N): # i hace función de un indicador, por lo que es necesaria colocarla
    x = int(input("Valor x: "))
    S = S + x # Esto es un acumulador porque suma de manera variable
prom = S / N # Debe estar fuera de la indentación del for para evitar que se repita N veces 
print(f"El promedio es de {prom:6.2f} unidades")