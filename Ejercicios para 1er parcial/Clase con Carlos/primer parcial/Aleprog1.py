a = float(input("Escriba el dividendo "))
b = float(input("Escriba el divisor "))
if b != 0 :
    resultado = a/b
    print(f"La división de {a} entre {b} es {resultado:6.2f}")
else:
    print("ERROR")
    