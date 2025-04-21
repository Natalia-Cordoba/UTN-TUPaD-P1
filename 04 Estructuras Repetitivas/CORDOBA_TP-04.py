# Trabajo Práctico N° 4: Estructuras repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

cantidad_num = 100 

for i in range(cantidad_num + 1):  # formulo la condición
    print(i)          # muestro los numeros por consola

#-------------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad 
# de dígitos que contiene.

# declaro las variables necesarias y las inicializo
numero = int(input("Ingresá un número entero: "))
contador = 0

# me quedo con el absoluto de los numeros ya que si ingresan numeros negativos 
# va a contar como digito el signo menos (-)
num = abs(numero)

# el número 0 lo manejo aparte porque si la condicion es num >= 0 caemos en un bucle infinito
# y con la condicion num > 0 no entra al bucle porque es falsa 
if num == 0:
    contador = 1
else:
    while num > 0:
        num = num // 10
        contador += 1

# muestro la cantidad de digitos por consola
print("La cantidad de dígitos es:", contador)

#-------------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores

# declaramos e inicalizamos variable
num_1 = int(input("Ingresá el primer número entero: "))
num_2 = int(input("Ingresá el segundo número entero: "))
suma = 0

# definimos dos opciones para sumar, ya que el debemos tener en cuenta que el usuario nos puede dar
# un numero menor en la segunda opcion, para ello invertimos los valores del rango
if num_1 < num_2:
    for i in range(num_1 + 1, num_2):
        suma += i
else:
    for i in range(num_2 + 1, num_1):
        suma += i

# mostramos la suma por de los numero por consola
print("La suma de los números enteros entre los dos valores es:", suma)

#-------------------------------------------------------------------------------------------

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# defino e inicializo la variable
suma = 0

# pido el primer numero al usuario
num = int(input("Ingrese un número, (para finalizar ingrese 0): "))

# mientras el numero sea distinto de 0 me quedo en el ciclo
while num != 0:
    # hago la sumatoria de los numeros que va ingresando actualizando la variable suma
    suma += num
    # pido un nuevo numero
    num = int(input("Ingrese otro número, (para finalizar ingrese 0): "))

# muestro el resultado de la suma por consola
print("La suma de los numeros ingresados es: ", suma)

#-------------------------------------------------------------------------------------------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

# importo random para poder tener un numero aleatorio
import random

# defino variables y las inicializo
num_secreto = random.randint(0, 9)  # defino el rango para mi num aleatorio 
intentos = 1    #inicia en 1 porque el primer intento se hace fuera del ciclo

# primer intento del usuario
num_elegido = int(input("Adivina un número entre el 0 y el 9: "))   

while num_elegido != num_secreto:
    intentos += 1       # actualizo contador de intentos
    # si no adivina nuevo a pedir numero
    num_elegido = int(input("Incorrecto. Intenta otra vez: ")) 

# muestro cantidad de intentos por consola
print(f"Felicitaciones, adivinaste el número en {intentos} intentos")

#-------------------------------------------------------------------------------------------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
    
# entre 0 y 100, no incluye los extremos. Iniciamos en 100-2(98) y terminamos en 0 sin incluirlo
# -2 para solo imprimir los pares
for i in range(100-2, 0, -2):
    print(i)  # muestro los numero por consola

#-------------------------------------------------------------------------------------------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# declaramos e inicalizamos variable
num = int(input("Ingrese un número entero positivo: "))
suma = 0

# nuevamento comprendidos entre 0 y un numero indicado por el usuario no incluye los extremos
# se podría dejar range(0, num) porque el 0 no cambia la suma
for i in range(0 + 1, num):
    suma += i # vamos sumando el nuevo valor a la variable suma y la actualizamos

# mostramos la suma por de los numero por consola
print(f"La suma de los números enteros entre 0 y {num} es:", suma)

#-------------------------------------------------------------------------------------------

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# declaro e inicializo mis variables
cantidad_num = 5 
contador = 0
pares = 0
impares = 0 
positivos = 0
negativos = 0

# explico al usuario lo que debe hacer
print(f"Por favor, ingrese {cantidad_num} números enteros:")

for contador in range(cantidad_num): # el ciclo se ejecuta la cantidad de numeros que definimos
    # pedimos un numero
    num = int(input(f"Ingrese el número {contador + 1}: "))
    # actualizamos la variable que lleva la cuenta de los numeros ingresados
    contador += 1

    # evaluamos si el numero es par o impar (contamos 0 como par) y actualizamos la
    # variable que corresponda
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # evaluamos si el numero es positivo o negativo y actualizamos la variable que 
    # corresponda. Excluimos el 0 en ambas condiciones porque no es ni positivo 
    # ni negativo, puede ingresarlo pero no actualiza ninguna variable 
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# mostramos por consola cuantos número se ingresaron de cada categoría
print("En los numero ingresador hay: \n"
      f"{pares} numeros pares \n"
      f"{impares} numeros impares \n"
      f"{positivos} numeros positivos \n"
      f"{negativos} numeros negativos \n")

#-------------------------------------------------------------------------------------------

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# declaro e inicializo mis variables
cantidad_num = 5 
contador = 0
suma = 0

# explico al usuario lo que debe hacer
print(f"Por favor, ingrese {cantidad_num} números enteros:")

for contador in range(cantidad_num): # el ciclo se ejecuta la cantidad de numeros que definimos
    # pedimos un numero
    num = int(input(f"Ingrese el número {contador + 1}: "))
    # actualizamos la variable que lleva la cuenta de los numeros ingresados
    contador += 1
    suma += num


media = suma / cantidad_num
print("La media de los números ingresados es:", media)

#-------------------------------------------------------------------------------------------

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_original = int(input("Ingrese un número entero: "))
num_absoluto = abs(num_original)
num_inverso = 0

while num_absoluto > 0:
    digito = num_absoluto % 10
    num_inverso = num_inverso * 10 + digito
    num_absoluto = num_absoluto // 10

if num_original < 0:
    num_inverso = -num_inverso


print(f"El número inverso a {num_original} es: {num_inverso}")

