import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Adivina el número secreto entre 1 y 100!")

while True:
    adivinanza = int(input("Ingresa tu número: "))
    intentos += 1

    if adivinanza < numero_secreto:
        print("Muy bajo")
    elif adivinanza > numero_secreto:
        print("Muy alto")
    else:
        print(f"¡Correcto en {intentos} intentos!")
        break
    print("Por favor, ingresa un número válido.")
