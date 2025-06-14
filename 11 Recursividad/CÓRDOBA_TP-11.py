# TP N° 11: RECURSIVIDAD

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Definición de funciones
def factorial(num):
    if num == 0:  # Caso base
        return 1
    else:
        return num * factorial(num-1) # llamada recursiva

# Programa principal
# Pido un número al usuario
num_usuario = int(input("Ingrese un número: "))

# controlo que el número sea mayor a 1
while num_usuario < 1:
    num_usuario = int(input("Por favor, ingrese un número entero mayor o igual a 1: "))
    
#con un ciclo voy pasando por todos los numeros del rango y calculo su factorial
for i in range(1, num_usuario + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

# ------------------------------------------------------------------------------------------

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

# Definición de funciones
def fibonacci(posicion):
    if posicion == 0:   # Caso base
        return 0
    elif posicion == 1:   # Caso base
        return 1
    else:      # Llamada recursiva
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
 
# Programa Principal
# Pido al usuario el número de la variable posicion
posicion = int(input("Por favor ingresa hasta que número desea mostrar la serie Fibonacci: "))

# Controlo que el número sea mayor o igual a 0
while posicion < 0:
    posicion = int(input("El número debe ser mayor o igual a 0. Por favor, intentelo de nuevo: "))

# Imprimo la serie hasta la posicion indicada por el usuario
print(f"La serie de Fibonacci hasta la posición {posicion} es:")
for i in range(posicion + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# ------------------------------------------------------------------------------------------

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

# Definición de funciones
def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:  # Llamada recursiva
        return base * potencia(base, exponente - 1)

# Programa principal
# Pido al usuario los valores para la base y el exponente de la potencia
base = int(input("Por favor, ingrese el valor para la base de la potencia: "))
exponente = int(input("Por favor, ingrese el valor para el exponente de la potencia. /nDebe ser mayor o igual a 0: "))

# Controlo que el número sea mayor o igual a 0
while exponente < 0:
    exponente = int(input("El exponente debe ser mayor o igual a 0. Por favor, intentelo de nuevo: "))

resultado = potencia(base, exponente)

# Imprimo el resultado de la potencia por pantalla
print(f"{base} elevado a la {exponente} es igual a: {resultado}")

# ------------------------------------------------------------------------------------------

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
# procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# Definición de funciones
def decimal_a_binario(num):
    if num == 0:  # Caso base
        return "0"
    elif num == 1:  # Caso base
        return "1"
    else:  # Llamada recursiva
        return decimal_a_binario(num // 2) + str(num % 2)

# Programa principal
# Pido el número decimal
num = int(input("Por favor, ingrese el número decimal que desea convertir a binario: "))

# Controlo que el número sea mayor o igual a 0
while num < 0:
    num = int(input("El numero debe ser mayor o igual a 0. Por favor, intentelo de nuevo: "))

# Muestro el resultado
print(f"El número binario es: {decimal_a_binario(num)}")

# ------------------------------------------------------------------------------------------

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de 
# texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

# Definición de funciones
def es_palindromo(palabra):
    # cuando la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1: # Caso base
        return True
    # si las letras de los extremos no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:  
        return False
    # voy eliminando la primera y la última letra
    return es_palindromo(palabra[1:-1])  # Llamada recursiva

def palabra_valida(palabra):
    tildes = 'áéíóú'
    if ' ' in palabra: # ver si tiene espacios
        return False
    for letra in palabra:
        if letra in tildes:  # ver si tiene tildes
            return False
    return True

# Programa principal
# Pido la palabra al usuario
palabra = input("Por favor, ingresa una cadena de texto sin espacios ni tildes: ").lower()

# Controlo que la palabra no tenga ni tildes ni espacios
while not palabra_valida(palabra):
    palabra = input("La palabra no debe contener espacios ni tildes. Por favor, intentelo de nuevo: ").lower()

# Imprimo si la palabra es palindromo o no
if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo.")
else:
    print(f"La palabra {palabra} NO es un palíndromo.")

# ------------------------------------------------------------------------------------------

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número 
# entero positivo y devuelva la suma de todos sus dígitos. 
# Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 

# Definición de funciones
def suma_digitos(n):
    if n < 10:  # Caso base
        return n
    else:  # Lamada recursiva
        return n % 10 + suma_digitos(n // 10)

# Programa principal
# Pido al usuario un número
numero = int(input("Por favor, ingrese un número entero positivo: "))

# Controlo que el número sea positivo
while numero < 0:
    numero = int(input("El número debe ser positivo. Intente nuevamente: "))

# Imprimo el resultado de la suma de los dígitos
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# ------------------------------------------------------------------------------------------

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

# Definición de funciones
def contar_bloques(n):
    if n == 1:  # Caso base
        return 1
    else:  # Llamada recursiva
        return n + contar_bloques(n-1)

# Programa principal
# Pido al usuario un número
n = int(input("Por favor, ingrese un número para la base de la pirámide: "))

# Controlo que el número sea positivo
while n <= 0:
    n = int(input("El número debe ser mayor a cero. Por favor, intente nuevamente: "))

# Imprimo por pantalla el resultado
print(f"La cantidad total de bloques para esa pirámide es: {contar_bloques(n)}")

# ------------------------------------------------------------------------------------------

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número.

# Definición de funciones
def contar_digito(numero, digito):
    if numero == 0:  # Caso base
        return 0
    else:   # Llamada recursiva
        if numero % 10 == digito:  # Si el último dígito coincide sumo 1
            return 1 + contar_digito(numero // 10, digito)
        else:  # Si no coincide, no sumo nada
            return contar_digito(numero // 10, digito)

# Programa principal
# Pido un número al usuario
numero = int(input("Por favor, ingrese un número entero positivo: "))

# Controlo que el número sea mayor o igual a 0
while numero < 0:
    numero = int(input("El número debe ser positivo. Intente nuevamente: "))

# Pido al usuario un dígito
digito = int(input("Por favor, ingrese el dígito que desea contar (0-9): "))

# Controlo que el digito sea positivo y este en el rango (0,9)
while digito < 0 or digito > 9:
    digito = int(input("El dígito debe estar entre 0 y 9. Intente nuevamente: "))

# Imprimo la cantidad de veces que el digito aparece en el número
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")

