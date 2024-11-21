# 5.- se desea un programa en PYTHON que tenga un 
# arreglo de tamaño 10 con números positivos y negativos, 
# y colocar los números que son positivos en otro arreglo 
# llamado POS y los negativos en un arreglo llamado NEG 

array1 = []
POS = []
NEG = []
for x in range(1,11):
    ing = int(input(f"ingrese un número {x}/10: "))
    array1.append(ing)
    if ing > 0:
        POS.append(ing)
    else:
        NEG.append(ing)
print(f"los números de la lista son:\n {array1}")
print(f"los números positivos son:\n\t{POS}")
print(f"los números negativos son:\n\t{NEG}")
