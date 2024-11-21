# 1.- Realizar Programa en PYTHON que maneje un arreglo de tamaño 5 
# y que entregue la Suma de todos los elementos del arreglo que tenga .

lista = []
sumar = 0
for x in range(1,6):
    ing = int(input("ingrese número: "))
    sumar +=ing
    lista.append(ing)
    suma = sum(lista)
    u = 0
    for i in lista:
      u+=i
    
print(f"{lista} es igual a {suma} 'con metodo sum'")
print(f"{lista} es igual a {sumar} 'con metodo incrementar'")

print(f"{lista} es igual a {u} 'con metodo recorriendo lista'")
