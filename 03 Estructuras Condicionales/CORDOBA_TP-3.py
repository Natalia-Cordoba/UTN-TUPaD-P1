# TRABAJO PRÁCTICO N°3 ESTRUCTURAS CONDICIONALES

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# defino una constante para la mayoria de edad
MAYORIA_EDAD = 18

# defino la variable edad como un numero ingresado por el usuario
edad = int(input("Por favor, ingrese su edad: "))

# comparo con un condicional si la variable edad es mayor que MAYORIA_EDAD
# pide que sea mayor que 18 por eso utilizo mayor y no mayor o igual
if edad > MAYORIA_EDAD:
    # muestro un mensaje si se cumple la condicion
    print("Es mayor de edad")
elif edad < 0:
    print("La edad ingresada no es válida")

# ---------------------------------------------------------------------

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá 
# mostrar el mensaje “Desaprobado”.

# declaro mi variable nota como un numero float ingresado por el usuario 
# uso float y no int porque la nota puede ser un numero decimal ej: 7,50
nota = float(input("Por favor, ingrese su nota para saber si aprobó o desaprobó: "))

# comparo con un condicional si la nota es mayor o igual que 6 y menor o igual que 10 (nota máxima posible)
if nota >= 6 and nota <= 10:
    # muestro un mensaje por consola si se cumple la condicion
    print("Aprobado")
# comparo con un condicional si la nota es menor que 6 y mayor o igual que 0 (nota mínima posible)
elif nota < 6 and nota >= 0:
    # muestro un mensaje por consola si se cumple la condicion
    print("Desaprobado")
else:
    # aviso al usuario por consola que la nota ingresada no es válida
    print("La nota ingresada no es válida")

# ----------------------------------------------------------------------

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# declaro mi variable num_ingresado como un valor ingresado por el usuario 
num_ingresado = int(input("Por favor, ingrese un numero: "))

# comparo con un condicional si el numero ingresado por el usuario es par con el operador modulo
if num_ingresado % 2 == 0:
    # muestro un mensaje por consola si se cumple la condicion
    print("Ha ingresado un número par")
else:
    # muestro un mensaje diferente por consola si NO se cumple la condicion
    print("Por favor, ingrese un número par")

# ----------------------------------------------------------------------

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
    # Niño/a: menor de 12 años.
    # Adolescente: mayor o igual que 12 años y menor que 18 años.
    # Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    # Adulto/a: mayor o igual que 30 años.

# defino la variable edad como un numero ingresado por el usuario
edad = int(input("Por favor, ingrese su edad: "))

# analizo si pertenece a la categoría niño/niña
if edad > 0 and edad < 12:
    # muestro un mensaje si se cumple la condicion
    print("Usted pertenece a la categoría niño/niña")
# analizo si pertenece a la categoría adolescente
elif edad >= 12 and edad < 18:
    # muestro un mensaje si se cumple la condicion
    print("Usted pertenece a la categoría adolescente")
# analizo si pertenece a la categoría adulto/adulta joven
elif edad >= 18 and edad < 30:
    # muestro un mensaje si se cumple la condicion
    print("Usted pertenece a la categoría adulto/adulta joven")
# analizo si pertenece a la categoría adulto/adulta
elif edad >= 30:
    # muestro un mensaje si se cumple la condicion
    print("Usted pertenece a la categoría adulto/adulta")
# analizo si el valor ingresado para la edad es válido
else:
    # aviso al usuario que ingresó un valor inválido
    print("La edad ingresada no es válida")

# ----------------------------------------------------------------------

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado 
# una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de 
# entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad 
# de elementos que tiene un iterable tal como una lista o un string.

# declaro mi variable contraseña como un valor ingresado por el usuario
contrasenia = input("Por favor ingrese una contraseña: ")

# calculo la longitud de la contraseña ingresada
longitud_contrasenia = len(contrasenia)

# controlo con un condicional si la contraseña ingresada cumple con la longitud requerida
if longitud_contrasenia >= 8 and longitud_contrasenia <= 14:
    # muestro un mensaje si se cumple la condicion
    print("Ha ingresado una contraseña correcta")
else:
    # muestro un mensaje distinto si NO se cumple la condicion
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ----------------------------------------------------------------------

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana 
# y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

# genero 50 números aleatorios entre 1 y 100 y los guardo en la variable numeros_aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# calculo la moda, la mediana y la media de mi lista de números 
mi_moda = mode(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)
mi_media = mean(numeros_aleatorios)

# muestro por consola la lista de numeros y los resultados de los calculos 
print("Lista de números: ", numeros_aleatorios)
print("Moda: ", mi_moda)
print("Mediana: ", mi_mediana)
print("Media: ", mi_media)

# comparo los resultados con los condicionales para ver si hay sesgo positivo
if mi_media > mi_mediana and mi_mediana > mi_moda:
    # muestro un mensaje si se cumple la condicion
    print("Hay sesgo positivo")
# comparo los resultados con los condicionales para ver si hay sesgo negativo
elif mi_media < mi_mediana and mi_mediana < mi_moda:
    # muestro un mensaje si se cumple la condicion
    print("Hay sesgo negativo")
# comparo los resultados con los condicionales para ver si NO hay sesgo
elif mi_media == mi_mediana == mi_moda:
    # muestro un mensaje si se cumple la condicion
    print("No hay sesgo")
else:
    # aviso por un mensaje que no se pudo determinar
    print("No se puede determinar el sesgo")

# ----------------------------------------------------------------------

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina 
# con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# declaro la variable palabra_frase y guardo en ella la palabra o frase ingresada por el usuario
# antes de guardarla convierto los caracteres a minuscula para evitar errores
palabra_frase = input("Por favor, ingrese una palabra o frase: ").lower()

# tomo el ultimo caracter de la palabra o frase
ultimo_caracter = palabra_frase[-1]

# comparo con una estructura condicional si el caracter es una vocal
if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
    # si es una vocal reescribo el strig con un signo de admiracion al final
    print(palabra_frase + "!")
else:
    # si NO es una vocal reescribo el strig sin cambiar nada
    print(palabra_frase)

# ----------------------------------------------------------------------

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
    # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# declaro la variable nombre y guardo en ella el valor ingresado por el usuario
nombre = input("Por favor, ingrese su nombre: ")
# guardo en la variable num_elegido la opción que selecciona el usuario
num_elegido = int(input(
    "Por favor, seleccione cómo desea ver su nombre:\n"
    "Ingrese 1 si desea verlo todo en mayúsculas\n"
    "Ingrese 2 si desea verlo todo en minúsculas\n"
    "Ingrese 3 si desea verlo con la primera letra en mayúscula y el resto en minúsulas\n"
))

# controlo si el numero elegido es el 1
if num_elegido == 1:
    # muestro el nombre ingresado todo en mayusculas
    print(nombre.upper())
# controlo si el numero elegido es el 2
elif num_elegido == 2:
    # muestro el nombre ingresado todo en minusculas
    print(nombre.lower())
# controlo si el numero elegido es el 3
elif num_elegido == 3:
    # muestro el nombre ingresado con la primer letra mayuscula y el resto en minuscula
    print(nombre.title())
else:
    # aviso al usuario que la opcion ingresada no es valida
    print("El numero ingresado es inválido")

# ----------------------------------------------------------------------

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una 
# de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
    # Menor que 3: "Muy leve" (imperceptible).
    # Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    # Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
    # Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
    # Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    # Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# declaro la variable magnitud como un valor ingresado por el usuario
magnitud = float(input("Por favor ingrese un numero para indicar la magnitud del terremoto: "))

# analizo si pertenece a la clasificacion Muy leve
if magnitud > 0 and magnitud < 3:
    # muestro un mensaje por consola con su clasificacion
    print("El terremoto se clasifica como Muy leve (imperceptible)")
# analizo si pertenece a la clasificacion Leve
elif magnitud >= 3 and magnitud < 4:
    # muestro un mensaje por consola con su clasificacion
    print("El terremoto se clasifica como Leve (ligeramente perceptible)")
# analizo si pertenece a la clasificacion Moderado
elif magnitud >= 4 and magnitud < 5:
    # muestro un mensaje por consola con su clasificacion
    print("El terremoto se clasifica como Moderado (sentido por personas, pero generalmente no causa daños)")
# analizo si pertenece a la clasificacion Fuerte
elif magnitud >= 5 and magnitud < 6:
    # muestro un mensaje por consola con su clasificacion
    print("El terremoto se clasifica como Fuerte (puede causar daños en estructuras débiles)")
    # analizo si pertenece a la clasificacion Muy fuerte
elif magnitud >= 6 and magnitud < 7:
    # muestro un mensaje por consola con su clasificacion
    print("El terremoto se clasifica como Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    # muestro un mensaje por consola con su clasificacion Extremo
    print("El terremoto se clasifica como Extremo (puede causar graves daños a gran escala)")
else:
    # aviso al usuario que el numero ingresado es invalido
    print("El numero ingresado no es valido")

# ----------------------------------------------------------------------

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# pedimos al usuario que nos ingrese el hemisferio en que se encuentra N/S
hemisferio = input("¿En qué hemisferio se encuentra?\n"
                   "Ingrese la letra N para el hemisferio Norte\n"
                   "Ingrese la letra S para el hemisferio Sur: ").upper()

# controlamos que el hemisferio ingresado sea valido antes de continuar
if hemisferio != "N" and hemisferio != "S":
    # avisamos si el hemisferio es invalido
    print("Hemisferio no válido.")
else:
    # si el hemisferios es valido pedimos el mes en el que se encuentra
    mes = int(input("Ingrese el mes del año (número del 1 al 12): "))
    # controlamos que el mes ingresado sea valido antes de continuar
    if mes < 1 or mes > 12:
        # avisamos si el mes es invalido
        print("Mes no válido.")
    else:
        # si el hemisferio y el mes son validos definimos el máximo día posible según el mes
        # 28 para febrero
        if mes == 2:
            max_dia = 28
        # 30 para abril, junio, septiembre, noviembre 
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            max_dia = 30
        # 31 para los demás meses
        else:
            max_dia = 31

        # pedimos el día en el que se encuentra el usuario
        dia = int(input("Ingrese el número de día: "))
        # controlamos que la cantidad de días ingresados sea válida para el mes ingresado anteriormente
        if dia < 1 or dia > max_dia:
            # avisamos si el día es invalido
            print("Día no válido para el mes ingresado.")
        else:
            # definimos las condiciones para las estaciones de hemisferio norte
            if hemisferio == "N":
                # definimos las condiciones para la estación invierno
                if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                    estacion = "Invierno"
                # definimos las condiciones para la estación primavera
                elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                    estacion = "Primavera"
                # definimos las condiciones para la estación verano
                elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
                    estacion = "Verano"
                # definimos las condiciones para la estación otoño
                elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
                    estacion = "Otoño"
            # definimos las condiciones para las estaciones de hemisferio sur
            elif hemisferio == "S":
                # definimos las condiciones para la estación verano
                if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                    estacion = "Verano"
                # definimos las condiciones para la estación otoño
                elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                    estacion = "Otoño"
                # definimos las condiciones para la estación invierno
                elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
                    estacion = "Invierno"
                # definimos las condiciones para la estación primavera
                elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
                    estacion = "Primavera"
            
            # mostramos por consola un mensaje con la estacion en que se encuentra el usuario
            print(f"En tu hemisferio ahora es: {estacion}")

