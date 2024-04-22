#EJERCICIO 1
for num in range(0, 100):
    print(num)


#EJERCICIO 2
def suma(first, second, third):
    return first + second + third

suma(2, 3, 4)

#EJERCICIO 3
suma_lambda = lambda a, b, c: a + b + c

print(suma_lambda(1, 2, 3))


#EJERCICIO 4
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print(f"{nombre} coincide con un valor de la lista!")
else:
    print(f"{nombre} no coincide con ningún valor de la lista")

