# 2.- Realizar Programa en PYTHON que maneje tres arreglos de tamaño 3. 
# Que pueda Sumar los elementos de los dos arreglos y guardar el resultado en el tercer arreglo

lista1 = []
lista2 = []
final = []
for x in range(1,4):
    ing = int(input(f"ingrese un número {x}/3: "))
    lista1.append(ing)
for y in range(1,4):
    ing2 = int(input(f"ingrese un número {y}/3: "))
    lista2.append(ing2)

suma = sum(lista1)+sum(lista2)
final.append(suma)
print(f"\tlos números de la lista 1 son: {lista1}")
print(f"\tlos números de la lista 2 son: {lista2}")
print(f"\tla suma de las 2 listas es: {suma}")

