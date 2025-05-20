# TRABAJO PRÁCTICO N° 5: FUNCIONES

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definición de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#------------------------------------------------------------------------------------------------

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
# y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
# deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando 
# el nombre al usuario.

# Definición de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
nombre = input("Por favor, ingrese su nombre: ")  # pido el nombre al usuario
saludar_usuario(nombre)

#------------------------------------------------------------------------------------------------

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba 
# cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
# Primero pido al usuario los datos
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
residencia = input("Por favor, ingrese su lugar de residencia: ")

# Segundo llamo a la función
informacion_personal(nombre, apellido, edad, residencia)

#------------------------------------------------------------------------------------------------

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva 
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Definición de funciones
import math
pi = math.pi
def calcular_area_circulo(radio):
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

# Programa principal
# Pido el radio al usuario
radio = int(input("Por favor, ingrese el radio del circulo para calcular el área y el perímetro: "))

# Llamo a las funciones
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del circulo es: {area:.2f}")
print(f"El perímetro del circulo es: {perimetro:.2f}")

#------------------------------------------------------------------------------------------------

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y 
# devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado 
# usando esta función.

# Definición de funciones
def segundos_a_horas(segundos):
    horas = segundos // 3600
    resto_segundos = segundos % 3600
    minutos = resto_segundos // 60
    segundos_finales = resto_segundos % 60
    resultado = f"{segundos} segundos son: {horas} horas, {minutos} minutos y {segundos_finales} segundos"
    return resultado

# Programa principal
segundos = int(input("Por favor, ingrese una cantidad de segundos para saber cuántas horas son: "))
cantidad_horas = segundos_a_horas(segundos)
print(cantidad_horas)

#------------------------------------------------------------------------------------------------

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla 
# de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones
def validar_num():
    num = int(input("Por favor, ingrese un numero para conocer su tabla: "))
    while num < 1 or num > 10:
        num = int(input(f"Debe ser un número del 1 al 10. Ingrese otro número: "))
    return num

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")

# Programa principal
numero = validar_num()
tabla_multiplicar(numero)

#------------------------------------------------------------------------------------------------

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Definición de funciones
def operaciones_basicas(a, b):
    # operaciones
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # me aseguro de que no se divida por 0 para evitar errores 
    if b == 0:
        division = "Lo siento, no es posible dividir por 0"
    else:
        division = a / b
    return (suma, resta, multiplicacion, division)

# Programa principal
# Pido al usuario los dos números 
a = int(input("Por favor, ingresa el primer número: "))
b = int(input("Por favor, ingrese el segundo número: "))

# Llamo a la funcion y muestro los resultados
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")

#------------------------------------------------------------------------------------------------

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar 
# el resultado con dos decimales.

# Definición de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
# Pido los valores de peso y altura
peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

# Llamo a la función y muestro los resultados
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

#------------------------------------------------------------------------------------------------

# # 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva 
# # su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (1.8 * celsius) + 32
    return fahrenheit

# Programa principal
celsius = float(input("Por favor, ingresa la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius es igual a {fahrenheit} grados Fahrenheit")

#------------------------------------------------------------------------------------------------

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva 
# el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
# Pido los 3 numero al usuario
a = float(input("Por favor, ingrese el primer número: "))
b = float(input("Por favor, ingrese el segundo número: "))
c = float(input("Por favor, ingrese el tercer número: "))

# Llamo a la función y muestro los resultados
promedio = calcular_promedio(a, b, c)
print(f"El promedio entre {a}, {b} y {c} es: {promedio:.2f}")

