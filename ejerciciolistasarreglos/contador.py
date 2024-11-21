
contador = 5 # contar cuantos números ingresamos
acumulador = 0 # esta funcion suma los números
cuantos = int(input("¿cuantos números desea ingresar?: "))
for x in range(1,cuantos+1):
    ing = int(input("ingrese número: "))
    contador = contador + 1
    acumulador += ing
print("los numeros son: ", contador)
print("la suma de los números es: ", acumulador)

