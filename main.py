# #esto es un comentario y no se ejecuta
# print("Hola mundo")

# #Start: sintaxis
# #shift+alt+f
# #end: sintaxis

# #comentario de una sola linea
# # if True:
# #     print("Verdadero")
# # else:
# #     print("Falso")  

# #start: variables, constantes y tipos de datos

# x=10 #Guarda el numero entero 10 en la variable x.
# print(x)
# tasa_interes=3.14
# usuario_actual="ana"
# usuario_activo = True
# print(x, tasa_interes, usuario_actual, usuario_activo)

# #Constantes
# MAX_INTENTOS_JUGADOR = 3
# #Usualmento cuando esta escrito en maysuucula es una constante
# print(MAX_INTENTOS_JUGADOR)


# #Print(stdout)
# nombre="Ana"
# print(f"Mi nombre es {nombre}") #Imprime: Mi nombre es Ana

# #Tipos de entrada basicos
# #int: numeros enteros(-2,0,5)
# #float: numeros decimales(3.14)
# #bool: verdadero o falso(True o False)
# #str: cadenas de texto("Hola mundo",'hola mundo')
# # print(type(x))
# # print(type(tasa_interes))
# # print(type(usuario_activo))
# # print(type(usuario_actual))
# #end: variables, constantes y tipos de datos
# # start: operadores aritmeticos
# x=10
# y=3
# print(x+y) #suma
# print(x-y)  #resta
# print(x*y) #multiplicacion
# print(x/y) #division
# print(x%y) #modulo= resto de la division
# print(x**y) #potencia

# #operadores de comparacion
# print(x==y) #igual
# print(x!=y) #distinto
# print(x>y) #mayor que
# print(x<y) #menor que
# print(x>=y) #mayor o igual que
# print(x<=y) #menor o igual que

# #operadores logicos
# print(x and y) #and
# print(x or y) #or
# print(not x) #not

# edad=20
# es_estudiante=True
# print((edad>18) and es_estudiante) #True ambas condiciones son ciertas
# print((edad<18) or es_estudiante) #True al menos una de las condiciones es cierta   
# print(not es_estudiante) #False

# #operadores de asignacion
# x+=y #x=x+y
# x-=y #x=x-y
# x*=y #x=x*y
# x/=y #x=x/y
# x=10 #asigancion simple

# #asigancion multiple
# a, b, c = 1, 2, 3 #a=1, b=2, c=3
# print(a, b, c)
# p = q= r = 1 #p=1, q=1, r=1 asigancion de valor a mulltiple variables

# ## start: intercamiio directo
# x,y=10,20
# print(x, y)
# x,y=y,x
# print(x, y)
# ## end: intercamiio directo


# #start: input (stdin)
# #FIXME: asd
# #TODO: hjhkjhkj


# nombre=input("Introduce tu nombre: ")
# print(f"Mi nombre es {nombre}")

# dato_1=input("Introduce el primer dato: ")
# dato_2=input("Introduce el segundo dato: ")
# print(f"La suma de {dato_1} y {dato_2} es {int(dato_1)+int(dato_2)}")
# print(f"la suma de los dos numeros es: {(dato_1 + dato_2)} ") #manera inocrrecta de hacerlo
# #end: input (stdin)


# # Start conversion de tipos de datos basicos

# ### conversion implicita
# a = 5 #entero
# b = 2.0 #float
# c= a + b #float
# print(type(c))

# #Conversion explicita
# # conversion a entero
# num_str = "10"
# print(type(num_str))
# num_int = int(num_str)
# print(type(num_int))

# #conversion a float
# num = 10
# print(type(num))
# num_float = float(num)
# print(type(num_float))





# #end: operadores aritmeticos

# #Start > condicionales
# num_input=float(input("Pon un numero: "))
# if num_input < 0:
# #bloque de codigo que se ejecuta
#     print("negativo")
# elif num_input==0:
#     #
#     print("0")
# else:
#     #
#     print("positivo")

# ##################### ejercicios
# '''
#  Implementa un programa que solicite la edad y que este determine si la persona es menor de edad, mayor o tiene edad de jubilación.
# 2. Implementa un programa que solicite una contraseña y verifica si es correcta o incorrecta. “Tú defines cuál es la contraseña correcta”.
# 3. Implementa un programa que solicite dos números, determina cuál es el mayor, o si 
 
 
#  '''

# #1
# num_input=int(input("edad: "))
# if num_input < 18:
# #bloque de codigo que se ejecuta
#     print("menor de edad")
# else:
#     print("mayor de edad")

# #1
# password=(input("contraseña: "))
# if password == "azulejo":
# #bloque de codigo que se ejecuta
#     print("contraseña correcta")
# else:
#     print("inocrrecto")

# #3
# #1
# num1=float(input("Digita un numero: "))
# num2=float(input("Digita otro numero: "))

# if num1 == num2:
# #bloque de codigo que se ejecuta
#     print("son iguales")
# elif num1 > num2:p
#     print("Num1 es mayor")
# else:
#     print("num 2 es  mayor")
#condicional while:

# num=int(input("escribe un numero: "))
# while num > 0:
#     for i  in range(num):
#         i += 1
#         print(i)
# password="toper"
# while True:
#     passs = input("digite: ")
#     if password == passs:
#         print("correcto")
#         break
#     else:
#         print("repite")

# num = int(input("Escribe un número: "))
# for i in range(1, num + 1):
#     print(i)

# for i in range(5): #imprime numeros dell 0 al 4
#     print(i)

# for i in range(10,0,-2): #crra una secuencia del 10 al 0, saltando -2

#     print(i)
'''
 Escribe un programa que pida un número y haga una cuenta regresiva hasta 0 usando while.
2. Escribe un programa para mostrar los números pares  desde 0 hasta 20.
3. Crea una lista de números y úsala para calcular la suma total.
4. Crea un programa que pida una contraseña hasta que sea correcta. “Tú defines cuál es la contraseña correcta”.
 
'''
# #1
# num=int(input("Number?: "))
# while num > 0:
#     for i in range(num,-1,-1):
#         print(i)
#         num-=1

# #2

# for i in range(0,21,2):
#     print(i)

# #3
# num=[14,15,17,18]
# for i in range(num):
#     total +=1
#     print(total)
# #4

# while True:
#     contraseña=input("ingrese un password: ")
#     if contraseña != "definida":
#         print("vuelve a repetir")

#     else:
#         print("correcto")
#         break
# #end condicionales
#empezar librerias
import random
while True:
    aleatorio=int(input("Adivina el numero: "))
    pnum=(random.randint(1,10))
    # print(random.randint(1,10))
    if pnum == aleatorio:
        print("ganaste")
        break
    else:
        print("vuelve a intenarlo")

#end librerias