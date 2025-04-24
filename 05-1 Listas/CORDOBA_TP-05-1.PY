# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range.

multiplos_de_cuatro = []

for i in range(1, 101):
    if i % 4 == 0:
        multiplos_de_cuatro.append(i)

print(multiplos_de_cuatro)

#-------------------------------------------------------------------------

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

mi_lista = ["libros", 17, True, "gatos", "café"]

print(mi_lista[3])
print(mi_lista[-2])

#-------------------------------------------------------------------------

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo: lista_vacia = []

lista_vacia = []

lista_vacia.append("frutillas")
lista_vacia.append("uvas")
lista_vacia.append("frambuesas")

print(lista_vacia)

#-------------------------------------------------------------------------

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#-------------------------------------------------------------------------

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# El programa crea una lista de números enteros positivos llamada numeros:
# numeros = [8, 15, 3, 22, 7]
# Después, elimina el número mayor de la lista usando el método remove().
# Para encontrar el mayor, se usa la función max() dentro del argumento del método:
# numeros.remove(max(numeros))
# Por último, muestra la lista con los cambios por pantalla con la función print().
# print(numeros)

#-------------------------------------------------------------------------

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista_numeros = []

for i in range(10, 31, 5):
    lista_numeros.append(i)

print(lista_numeros[:2])

#-------------------------------------------------------------------------

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "onix"
autos[2] = "fiesta"

print(autos)

#-------------------------------------------------------------------------

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []

for i in [5, 10, 15]:
    dobles.append(i * 2)

print(dobles)

#-------------------------------------------------------------------------

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#-------------------------------------------------------------------------

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # Posición lista_anidada[0]: 15
    # Posición lista_anidada[1]: True
    # Posición lista_anidada[2][0]: 25.5
    # Posición lista_anidada[2][1]: 57.9
    # Posición lista_anidada[2][2]: 30.6
    # Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

