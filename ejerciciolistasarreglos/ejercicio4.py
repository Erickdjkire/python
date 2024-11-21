# 4.- Se desea crear un programa en PYTHON que calcule el promedio final de un Estudiante de los ramos: 
# Matemática, Castellano e Historia (5 notas) , luego calcule el promedio final de todo

mat = []
cast = []
hist = []
promedio =[]
sumat = 0
sumcast = 0
sumhist = 0
for x in range(1,6):
    ingmat = int(input(f"ingrese nota {x}/5 para Matematicas: "))
    sumat += ingmat
    mat.append(ingmat)
print("\n")
for f in range(1,6):
    ingcast = int(input(f"ingrese nota {f}/5 para Castellano: "))
    sumcast += ingcast
    cast.append(ingcast)
print("\n")
for g in range(1,6):
    inghist = int(input(f"ingrese nota {g}/5 para Historia: "))
    sumhist += inghist
    hist.append(inghist)
print("\n")
finmat = sumat/5
promedio.append(finmat)
fincast = sumcast/5
promedio.append(fincast)
finhist = sumhist/5
promedio.append(finhist)
prom = int(sum(promedio)/3)

print(f"las notas de :\n\tmatematicas son: {mat} y su promedio es {finmat}\n\tcastellano son: {cast} y su promedio es {fincast}\n\thistoria son: {hist} y su promedio es {finhist}\n\n\tsu promedio final es {prom}\n\n\n".title())
    
