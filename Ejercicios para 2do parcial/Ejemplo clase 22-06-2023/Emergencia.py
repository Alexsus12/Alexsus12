suscriptores = open("Suscriptores.txt","r")
multados = open("Multados.txt","w")
CNM=0
CM=0
SUMAM=0
CT=0
for suscriptor in suscriptores:
    datos=suscriptor.strip().split(",")
    Ncontrato=datos[0]
    conMA=int(datos[1])
    lecINI=int(datos[2])
    lecFIN=int(datos[3])
    Porcinc=(lecFIN-lecINI)/conMA*100-100
    CT=CT+1
    if Porcinc>10:
        multados.write(f"{Ncontrato} -- {Porcinc:6.2f} %\n")
        Consumoact=lecFIN-lecINI
        CM=CM+1
        SUMAM=SUMAM+Consumoact
    if Porcinc<=10:
        CNM=CNM+1
        if CNM==1:
            PorcM=Porcinc
            ContratoMayor=Ncontrato
        elif Porcinc>PorcM:
            PorcM=Porcinc
            ContratoMayor=Ncontrato
PromM=SUMAM/CM
print(f"El promedio es {PromM:6.2f}")
PorcSM=CM/CT*100
print(f"El procentaje de multados es{PorcSM:6.2f}")
PorcSNM=100-PorcSM
print(f"El porcentaje de NO MULTADOS es{PorcSNM:6.2f}")
print(f"{ContratoMayor}")