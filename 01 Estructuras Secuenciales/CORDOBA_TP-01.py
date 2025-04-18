# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre 
# ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola " + nombre + "!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por 
# pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, 
# “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
lugar_residencia = input("Por último, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia} ")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
numero_ingresado = input("Por favor, ingresa el radio del circulo: ")
pi = 3.141592653589793
radio = float(numero_ingresado)
perimetro = 2 * pi * radio
area = pi * (radio ** 2)
print(f"El perimetro del circulo es: {perimetro} y el area del circulo es: {area}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
numero_ingresado = input("Por favor, ingresa un cantidad de segundos: ")
segundos = int(numero_ingresado)
horas = segundos // 60
print(f"{segundos} segundos equivalen a {horas} hora/s")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero_ingresado = input("Por favor, ingresa el número del que quieras conocer su tabla: ")
num = int(numero_ingresado)
print(num, "x 1 =", num * 1)
print(num, "x 2 =", num * 2)
print(num, "x 3 =", num * 3)
print(num, "x 4 =", num * 4)
print(num, "x 5 =", num * 5)
print(num, "x 6 =", num * 6)
print(num, "x 7 =", num * 7)
print(num, "x 8 =", num * 8)
print(num, "x 9 =", num * 9)
print(num, "x 10 =", num * 10)


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de 
# sumarlos, dividirlos, multiplicarlos y restarlos.
numero_ingresado1 = input("Por favor, ingresa el primer número: ")
num1 = int(numero_ingresado1)
numero_ingresado2 = input("Por favor, ingresa el segundo número: ")
num2 = int(numero_ingresado2)
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "x", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg / (altura en m)2
peso_ingresado = input("Por favor, ingresa tu peso en kilogramos: ")
peso = float(peso_ingresado)
altura_ingresada = input("Por favor, ingresa tu altura en centímetros: ")
altura = float(altura_ingresada)
altura_metros = altura / 100
imc = peso / (altura_metros ** 2)
print(f"Según su peso y altura, su IMC es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados 
# Fahrenheit. Tener en cuenta la siguiente equivalencia: Temperatura en Fahrenheit = 9/5.Temperatura en Celsius + 32
temperatura_ingresada = input("Por favor, ingresa la temperatura en Celsius: ")
temp_celsius = float(temperatura_ingresada)
temp_fahrenheit = (1.8 * temp_celsius) + 32
print(f"El equivalente en Fahrenheit a {temp_celsius} grados Celsius es: {temp_fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero_ingresado1 = input("Por favor, ingresa el primer número: ")
num1 = int(numero_ingresado1)
numero_ingresado2 = input("Por favor, ingresa el segundo número: ")
num2 = int(numero_ingresado2)
numero_ingresado3 = input("Por favor, ingresa el tercer número: ")
num3 = int(numero_ingresado3)
promedio = (num1 + num2 + num3) / 3
print(f"El promedio entre {num1}, {num2}, {num3} es de: {promedio}")