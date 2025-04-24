# TRABAJO PRÁCTICO N° 5.1 LISTAS

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range.

# creo la lista
multiplos_de_cuatro = []

# con un ciclo verifico que numero son divisibles por 4
for i in range(1, 101):
    if i % 4 == 0:
        # si lo son los agrego a la lista
        multiplos_de_cuatro.append(i)

# muestro la lista por pantalla
print(multiplos_de_cuatro)

#-------------------------------------------------------------------------

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

# creo la lista con los 5 elementos
mi_lista = ["libros", 17, True, "gatos", "café"]

# obtengo el penúltimo accediendo con índice positivo y los muetro por pantalla
print(mi_lista[3])
#obtengo el penúltimo accediendo con índice negativo y lo muestro por pantalla
print(mi_lista[-2])

#-------------------------------------------------------------------------

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo: lista_vacia = []

# creo la lista vacía
lista_vacia = []

# con el metodo append agrego 3 elementos
lista_vacia.append("frutillas")
lista_vacia.append("uvas")
lista_vacia.append("frambuesas")

# muestro la lista por pantalla
print(lista_vacia)

#-------------------------------------------------------------------------

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

# creo la lista de animales
animales = ["perro", "gato", "conejo", "pez"]

# modifico el segundo accediendo con índice positivo
animales[1] = "loro"
# modifico el último accediendo con índice negativo
animales[-1] = "oso"

# muestro la lista por pantalla
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

# creo la lista de numeros
lista_numeros = []

# con un ciclo recorro del 10 al 30, cada 5 y agrego a la lista 
for i in range(10, 31, 5):
    lista_numeros.append(i)

# muestro por pantalla solo los primeros dos numeros de la lista
print(lista_numeros[:2])

#-------------------------------------------------------------------------

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

# creo la lista de autos
autos = ["sedan", "polo", "suran", "gol"]

# modifico los autos de los indices 1 y 2
autos[1] = "onix"
autos[2] = "fiesta"

# muestro la lista por pantalla
print(autos)

#-------------------------------------------------------------------------

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

# creo la lista dobles
dobles = []

# con un ciclo for recorro los tres numeros y agrego sus dobles a la lista
for i in [5, 10, 15]:
    dobles.append(i * 2)

# muestro la lista por pantalla
print(dobles)

#-------------------------------------------------------------------------

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# creo la lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# agrego un elemento a la lista
compras[2].append("jugo")
# modifico el valor de un elemento existente
compras[1][1] = "tallarines"
# elimino un elemento de la lista
compras[0].remove("pan")

# muestro la lista
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

# creo la lista con sus elementos teniendo en cuenta las consignas
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# muestro la lista por pantalla
print(lista_anidada)

