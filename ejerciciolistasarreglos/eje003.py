
"""
str = palabra = "texto aqui"
float = numeros_decimales = 3,4
int = numeros_enteros = 7
bool = boolean  = True or False

if, elif,else

append = abrir lista
"""

#  3.- Realizar un Programa en PYTHON que tenga  un arreglo de 
# tamaño 10 con números enteros (números positivos ó negativos). 
# Mostrar la cantidad de números positivos y negativos que hay en 
# dicho arreglo

lista = []
for i in range(1,11):
    numeros = int(input("ingrese número: "))
    lista.append(numeros)
    mayor = 0
    menor = 0
    for o in lista:
        if o > 0:
           mayor = mayor+1
        else:
            menor = menor+1
print("los números positivos son:",mayor,"y los números negativos son:",menor)
print("los números en lista son: ",lista)






