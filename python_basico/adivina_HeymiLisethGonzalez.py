import random

num_secreto = random.randint(1,100)
intentos = 1
while True:
    numero = int(input("Ingresa un numero: "))
    if numero < num_secreto:
        print("Muy bajo")
        intentos +=1
    elif numero > num_secreto:
        print("Muy alto")
        intentos +=1
    else:
        print(f"CORRECTO EN {intentos} INTENTOS")
        print(f"El numero ingresado es: {numero} y el numero alteatorio es: {num_secreto}")
        break
