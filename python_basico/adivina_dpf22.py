import random
num_aleatorio=(random.randint(1,100))
intentos=0
while True:
    print(num_aleatorio)
    intentos=intentos+1
    aleatorio=int(input("Adivina el numero: "))
    if aleatorio > num_aleatorio:
        print("Muy alto")
    elif num_aleatorio > aleatorio :
        print("Muy bajo") 
    elif num_aleatorio == aleatorio :
        print("ganaste")
        print(f"fue en total {intentos} intentos")
        break
