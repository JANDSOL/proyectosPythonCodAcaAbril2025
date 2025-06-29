"""Adivina un número secreto entre 1 y 100"""
import random
# Generar un número secreto entre 1 y 100
numero_secreto = random.randint(1, 100)
# Contador de intentos
num_intentos = 0

# Bucle para adivinar
while True:
    try:
        adivinanza = int(input("Adivina el número (entre 1 y 100): "))
        num_intentos += 1

        if adivinanza < numero_secreto:
            print("Muy bajo.")
        elif adivinanza > numero_secreto:
            print("Muy alto.")
        else:
            print(f"¡Correcto en {num_intentos} intentos!")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")
