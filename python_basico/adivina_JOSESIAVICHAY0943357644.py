 
import random

numero_secreto = random.randint(1, 100)
intentos = 0
encontrado = False

while not encontrado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else:
        print(f"¡Correcto en {intentos} intentos!")
        encontrado = True
