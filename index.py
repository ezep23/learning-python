print("Hola, Mundo")

year = 2024

print ("Estamos en el año: ", year)

""" Algoritmo basico para actividad:

    1. Ir hacia la heladera 
    2. Abrir la puerta de la heladera
    3. estirar el brazo y agarrar la jarra de jugo
    4. sacar el brazo de la heladera y cerrar su puerta
    5. colocar la jarra en la mesa
    6. buscar un vaso de vidrio que este limpio sobre la mesada
    7. agarrar el vaso, ponelo a 5 centimetros de la jarra.
    8. agarrar la jarra, posicionarlo a 30 centimetros de altura sobre el vaso e inclinarlo a 45 grados
    9. levantar de vuelta a 90 grados cuando este por la mitad de capacidad nuestro vaso.

""" 

rol = amigo
nombre =  gervacio 

print("Buen día, me gustaria invitarte mi buen, ", rol, " a mi cumpleaños el día 8 de abril, te espero ", nombre)
 
hw = ¡Hola, Mundo!
print(hw)

# Enteros: 
# Suma, resta, división, multiplicación

numero = 5 
snumero = 10
print("Mi numero es ", numero)

resultado_suma = snumero + numero
print(resultado)

resultado_resta = snumero - numero
print(resultado_resta)

resultado_multiplicacion = snumero * numero
print(resultado_multiplicacion)

resultado_division = snumero / numero
print(resultado_division)

# Tipo de datos

x = 10
x2 = 12.4
x3 = 'hola'

print(type(x)) #int 
print(type(x2)) #float
print(type(x3)) #string

#concatenando strings
nombre = "pensamiento"
apellido = "computacional"
nombre_materia = nombre + ' ' + apellido
print(nombre_materia)


#metodo para saber el largo 
largo_nombre = len(nombre) #len -> length
print(largo_nombre)

#aplicando metodo para cortar un string
[::] # -> substring

# nombre_corto = nombre[desde_donde:hasta_donde:cada_cuantas_letras]
# [start:stop:step] 

nombre_corto = nombre[:5:]

#funciones - mala práctica hacerlas individuales para cada persona
def saludarUnico():
    print("Hola! Espero que estés muy bien :)")
saludar()

#Estandarizar una función
#Buena practicar comentar sobre las funciones y comentar para que sirve
def saludar(nombre):
    print("Hola! " + nombre + " Espero que estés muy bien :)")

saludar("Manuel")
saludar("Juan")
saludar("Ernesto")

# Función que suma 2 números que le otorguemos.
def suma(numero1, numero2)
    print("El resultado es: " + numero1 + numero2)

suma(5,4)
suma(25,25)#Scope de funciones -> El codigo en toda la hoja index.py es global, mientras# que el codigo de una función es local.

# Recibe 2 números y devuelve la suma de ellos
def suma(sumando_1, sumando_2):
    resultado = sumando_1 + sumando_2
    return resultado #return -> devuelve un valor

resultado_suma = suma(5,9)
print(resultado_suma)

#Una función que devuelve más de 2 resultados
def resultados(numero_1, numero_2):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    return suma, resta #-> para que nos devuelva la suma por un lado y la resta por otro.
suma, resta = resultados(10, 5)

print("La suma es ", suma)
print("La resta es ", resta)

#Ingreso de datos por el usuario
valor = input(6) 

print(valor)
print(type(valor))

#Otra forma
#valor = input()
numerox = int(input("Ingrese un numero: "))
otro_numerox = int(input("Ingrese otro numero: "))

adicion = numerox + otro_numerox
print(adicion)