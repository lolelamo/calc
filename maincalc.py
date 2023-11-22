import numpy as np
import colorama
import time as sp

# abriendo el archivo para guardar los calculos
archivo = open("save.txt", "w")
import numpy as np
import colorama


# creando los DefS
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def raiz_cuadrada(a):
    return np.sqrt(a)
def seno(a):
    return np.sin(a)
def coseno(a):
    return np.cos(a)
def tangente(a):
    return np.tan(a)
print(colorama.Fore.RED + "Defs Creados" + colorama.Fore.RESET)
print("   ")
print("   ")


# abriendo el archivo para guardar los calculos
archivo = open("save.txt", "w")
#se crea un "menu" que dice al usuario que opciones hay, los colorama.Fore.<color> se utilizan para cambiar el color el print()
def menu():
    # imprimiendo el menu
    print(colorama.Fore.YELLOW + "Seleccione el tipo de calculo que desea realizar:" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "1. Suma" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "2. Resta" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "3. Multiplicacion" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "4. Division" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "5. Raiz cuadrada" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "6. Seno" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "7. Coseno" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "8. Tangente" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "9. Salir" + colorama.Fore.RESET)

    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    opcion = int(opcion)

    # se valida si el usuario puso una opcion correcta
    if opcion >= 1 and opcion <= 8:

        # pidiendo los operandos (variables) para los numeros, en caso de raiz cuadrada, sin(), cos(), tan() solo requiere 1 numero
        operando1 = input(colorama.Fore.YELLOW + "Ingrese el primer operando: " + colorama.Fore.RESET)
        operando1 = int(operando1)
        operando2 = input(colorama.Fore.YELLOW + "Ingrese el segundo operando: " + colorama.Fore.RESET)
        operando2 = int(operando2)

        # los ifs y elifs para escoger el tipo de calculo
        if opcion == 1:
            calculo = suma(operando1, operando2)
        elif opcion == 2:
            calculo = resta(operando1, operando2)
        elif opcion == 3:
            calculo = multiplicacion(operando1, operando2)
        elif opcion == 4:
            calculo = division(operando1, operando2)
        elif opcion == 5:
            calculo = raiz_cuadrada(operando1)
        elif opcion == 6:
            calculo = seno(operando1)
        elif opcion == 7:
            calculo = coseno(operando1)
        elif opcion == 8:
            calculo = tangente(operando1)
        #el codigo espera 2 segundos y termina (si el usuario pone el 9 para seleccionar)
        elif opcion == 9:
            sp.sleep(2)
            exit()

        # imprimiendo el resultado y se le cambia el color del print a verde
        print(colorama.Fore.GREEN + "El resultado es: " + str(calculo) + colorama.Fore.RESET)
        print("  ")
        print("  ")

        # guardando el calculo en el archivo save.txt, todos los inputs + Resultado
        archivo.write(str(opcion) + " " + str(operando1) + " " + str(operando2) + " " + str(calculo) + "\n")

    else:
        print(colorama.Fore.RED + "Opcion invalida" + colorama.Fore.RESET)

 # ejecutando el menu en la terminal
while True:
    menu()
# para reestablecer los colores de los print
deinit()
