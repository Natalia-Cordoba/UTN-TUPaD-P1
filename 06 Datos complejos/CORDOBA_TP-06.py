# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

# creo el diccionario de frutas y precios 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# agrego los elementos uno a uno
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# los muestro por consola
print(precios_frutas)

#--------------------------------------------------------------------------------------

print("\n")
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

# copio el diccionario que resultó del ejercicio anterior
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# actualizo los elementos uno a uno
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# los muestro por consola
print(precios_frutas)

# ------------------------------------------------------------------------------------------

print("\n")
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# copio el diccionario que resultó del ejercicio anterior
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# actualizo los elementos uno a uno
frutas = list(precios_frutas.keys())

# los muestro por consola
print(frutas)

# -------------------------------------------------------------------------------------------

print("\n")
# 4)  Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# creo el diccionario para almacenar nombres y numeros de telefono
numeros_telefonicos = {}   # si inicia vacío

# con un ciclo pido los 5 nombres con sus telefonos
for i in range (1, 6):
    nombre = input("Por favor, ingrese el nombre del contacto: ")
    telefono = int(input(f"Ahora ingrese el numero de telefono de {nombre}: "))
    numeros_telefonicos[nombre] = telefono   # añado al diccionario el nuevo contacto

# pido el nombre que quiere saber el número
nombre_a_buscar = input("Ingrese el nombre del contacto que desea buscar: ")

# verifico si existe y muestro el resultado porconsola
if nombre_a_buscar in numeros_telefonicos:
    print(f"El número de teléfono de {nombre_a_buscar} es: {numeros_telefonicos[nombre_a_buscar]}")
else:
    print("Lo siento. El contacto que buscas no existe.")

# ------------------------------------------------------------------------------------------------

print("\n")
# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra

# pido la frase al usuario
frase = input("Por favor, ingresa una frase: ")

# divido la frase en palabras
palabras = frase.split()

# con ayuda de set busco las palabras únicas y las imprimo
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# creo un diccionario para contar las repeticiones y los inicio vacío
recuento = {}

# con un ciclo for recorro las palabras
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1   # si la palabra ya está aumento en uno el contador
    else:
        recuento[palabra] = 1   # si la palabra no está igualo la cantidad a 1

# muestro la cantidad por consola
print(f"Recuento: {recuento}")

# -------------------------------------------------------------------------------------

print("\n")
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# creo el diccionario para almacenar los alumnos y sus notas
alumnos = {}

# pido al usuario ingresar los datos de los 3 alumnos
for i in range(3):
    # pido el nombre
    nombre = input("Por favor, ingrese el nombre del alumno: ")
    
    # pido las tres notas como números enteros
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Por favor, ingrese la nota {j} de {nombre}: "))
        notas.append(nota)
    
    # guardo las notas como tupla
    alumnos[nombre] = tuple(notas)

# saco el promedio de cada alumno y lo muestro por consola
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# -------------------------------------------------------------------------------------

print("\n")
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron 
# Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# creo los dos sets de números que representan estudiantes que aprobaron (uno para cada parcial)
aprobados_parcial_1 = {3, 4, 7, 11, 13, 16, 17}
aprobados_parcial_2 = {2, 3, 6, 7, 12, 14, 17}

# guardo en una variable los que aprobaron ambos parciales
ambos_parciales_aprobados = aprobados_parcial_1 & aprobados_parcial_2
# imprimo el resultado
print(f"Los estudiantes que aprobaron ambos parciales son: {ambos_parciales_aprobados}")

# guardo en una variable los que aprobaron solo uno de los parciales
solo_un_parcial_aprobado = aprobados_parcial_1 ^ aprobados_parcial_2
# imprimo el resultado
print(f"Los estudiantes que aprobaron solo uno de los parciales son: {solo_un_parcial_aprobado}")

# guardo en una variable los que aprobaron al menos un parcial, sin repetir estudiantes
total = aprobados_parcial_1 | aprobados_parcial_2
# lo muestro por consola
print(f"Los estudiantes que aprobaron al menos un parcial son: {total}")

# --------------------------------------------------------------------------------------------

print("\n")
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

# creo el diccionario con productos y su stock
listado_stock_productos = {"agenda": 378, "calendario": 523}

# permito al usuario consultar el stock de un producto ingresado
producto_consulta = input("Por favor, ingrese el producto que desea consultar: ").lower()

if producto_consulta in listado_stock_productos:
    print(f"Quedan {listado_stock_productos[producto_consulta]} unidades de {producto_consulta}.")
else:
    print(f"El producto '{producto_consulta}' no existe.")

# permito al usuario agregar stock
producto_stock = input("Por favor, ingrese el producto al que desea agregar stock: ").lower()
if producto_stock in listado_stock_productos:
    cantidad = int(input("¿Cuántas unidades desea agregar?: "))
    listado_stock_productos[producto_stock] += cantidad
    print(f"Stock actualizado: ahora hay {listado_stock_productos[producto_stock]} unidades de {producto_stock}.")
else:
    print(f"El producto '{producto_stock}' no existe.")

# permito al usuario agregar producto
producto_nuevo = input("Ingrese el nombre del producto: ")
cantidad= int(input("Ingrese la cantidad de stock inicial: "))
listado_stock_productos[producto_nuevo] = cantidad
print(f"Producto agregado: {producto_nuevo} con {cantidad} unidades.")

# mostrar el stock final actualizado
print("Stock final de productos:")
for producto, stock in listado_stock_productos.items():
    print(f"{producto}: {stock} unidades")

# --------------------------------------------------------------------------------------------------------

print("\n")
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora

# creo la agenda con los eventos
agenda = {
    ("lunes", "08:30"): "Entrega trabajo práctico",
    ("miercoles", "18:00"): "Clase Portugues",
    ("jueves", "16:00"): "Turno Dentista",
    ("viernes", "22:30"): "Cumpleaños Juana"
}

# pido al usuario por día y hora que desea consultar
dia = input("Por favor, ingrese el día que desea consultar en la agenda (ej: martes): ").lower()
hora = input("Por favor, ingrese la hora que desea consultar: (ej: 15:30): ")

# busco en la agenda si la tupla dada por el usuario exite y muestro por consola el mensaje que corresponda
if (dia, hora) in agenda:
    print(f"La actividad programada para el {dia} a las {hora} es: {agenda[(dia, hora)]}")
else:
    print("No hay actividades programadas para ese día y hora.")

# ---------------------------------------------------------------------------------------------------------

print("\n")
# 10)  Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

# creo el diccionario con clave: paises y valores: capitales
paises_capitales = {"Argentina": "Buenos Aires", "España": "Madrid", "Grecia": "Atenas", "Italia": "Roma", "Portugal": "Lisboa"}

# creo el nuevo diccionario para clave: capitales y valores: paises, lo inicio vacío
capitales_paises = {}

# intercambio los valores
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

# imprimo los dos diccionarios por consola para ver los cambios
print(paises_capitales)
print(capitales_paises)