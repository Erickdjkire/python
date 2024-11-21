lista = [1,2,3,4,5,"alejandro",333,3]


print(lista.count(3))
print(lista[0:3]) # imprime desde x a y
print(lista[:3]) # imprime hasta el segundo digito en lista
print(lista[-1]) # imprime en reversa
print(len(lista)) # te muestra la cantidad de indices que tiene la lista, en este caso, 5
print(lista.append("hola")) #agrega un valor de cualquier tipo, al final la lista
print(lista.insert(2,"hola")) #esto agrega un valor a un lugar determinado de la lista.
print(lista.extend(["a",1,9])) #concatena la lista con otra lista que creamos
print(3 in lista) #el resultado da en un valor booleano como respuesta
print(lista.index(4)) # busca indice () donde esta este valor
print(lista.count(3)) #cuantas veces se repite el valor () en la lista
print(lista.pop(0)) #se elimina el valor indicando según indice. si se deja vacio, elimina ultimo
print(lista.remove(2)) #se elimina el valor en lista
print(lista.sort()) # se ordena la lista de menor a mayor
print(lista.sort(reverse=True)) #Lista ordenada de mayor a menor
print(lista.clear) #se borra toda la lista