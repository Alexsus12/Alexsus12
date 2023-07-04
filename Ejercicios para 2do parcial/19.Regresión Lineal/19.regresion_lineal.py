f = open("Experimentos.txt","r")
primero  = f.readline()
N = int(primero)
Sxi = 0
Syi = 0
Sxiyi = 0
Sxi2 = 0
for i in range(N):
    linea = f.readline()
    datos = linea.strip().split(",")
    x = float(datos[0])
    y = float(datos[1])
    
    Sxi += x
    Syi += y 
    Sxiyi += x*y
    Sxi2 += x**2 
    
    if i == 0:
        rangomenor = y
    
    if i == N -1:
        rangomayor = y

m = (N*Sxiyi - Sxi*Syi)/(N*Sxi2-(Sxi)**2)

ym = Syi/N
xm = Sxi/N
b = ym -m*xm
bmodulo = abs(b)

if b ==0:
    print(f"La ecuación de la recta más probable es: Y= {m:6.3f}X")
    print(f"Rango de estudio de Y: [{rangomenor} , {rangomayor}]")
    
else:
    print(f"La ecuación de la recta más probable es: Y= {m:6.3f}X {'+' if b > 0 else '-'} {bmodulo:6.3f}")
    print(f"Rango de estudio de Y: [{rangomenor} , {rangomayor}]")
    
#Todo sea por ayudar a Isabela :3