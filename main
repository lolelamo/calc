import numpy as np
import colorama
import time as sp
#no se que hace esto
colorama.init()

global var
global rad
global dein
global redondear
global calculo


# abriendo el archivo para guardar los calculos
archivo = open("save.txt", "w")

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
def arcsin(a):
    return np.arcsin(a)
def arccos(a):
    return np.arccos(a)
def arctan(a):
    return np.arctan(a)


# abriendo el archivo para guardar los calculos
archivo = open("save.txt", "w")

def menu():
    calculo = 0.0
    calc = False
    var = False
    rad = False
    dein = False
    redondear = False
    debug = False
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
    print("10. config")

    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    opcion = int(opcion)

    # validando la opcion del usuario
    if opcion >= 1 and opcion <= 14:

        # pidiendo los operandos (variables) para los numeros

        # los ifs y elifs para escoger el tipo dfe calculo
        if opcion == 1:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print(" ")
            print(" ")

            calculo = suma(operando1, operando2)

        elif opcion == 2:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print(" ")
            print(" ")

            calculo = resta(operando1, operando2)
        elif opcion == 3:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print(" ")
            print(" ")
            calculo = multiplicacion(operando1, operando2)
        elif opcion == 4:
            calc = True

            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print(" ")
            print(" ")

            calculo = division(operando1, operando2)
        elif opcion == 5:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print(" ")
            print(" ")

            calculo = raiz_cuadrada(operando1)
        elif opcion == 6:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print(" ")
            print(" ")

            calculo = seno(operando1)
        elif opcion == 7:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print(" ")
            print(" ")

            calculo = coseno(operando1)
        elif opcion == 8:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "ingrese un numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print(" ")
            print(" ")

            calculo = tangente(operando1)

        elif opcion == 10:
            operando1 = input("Arcsin (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            try:
                calculo = arcsin(operando1)
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Error, numeros menores que -1 O mayores que 1 no se permiten para arcsin" + colorama.Fore.Reset)
         
        elif opcion == 11:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            try:
                calculo = arccos(operando1)
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Error, numeros menores que -1 O mayores que 1 no se permiten para arccos" + colorama.Fore.Reset)

        elif opcion == 12:
            operando1 = input(" Arctan (utiliza un numero Real) \n")
            operando1 = float(operando1)

            try:
                calculo = arctan(operando1)
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Error, SOLO numeros Reales" + colorama.Fore.Reset)

        #el codigo espera 2 segundos y termina (si el usuario pone el 9 para seleccionar)
        elif opcion == 13:
            if dein == True:
                colorama.deinit()
            sp.sleep(2)
            exit()


        elif opcion == 14:
            print(" ")
            print(" ")
            print("Config")
            print('''
            1. cambiar rad por deg (desactivar / activar, Funcion no testeada)
            2. debug
            3. deinit()
            4. Redondear numero ''')

            opcion1 = input("ingresa un numero (1-4)")
            opcion1 = int(opcion1)

            if opcion1 == 1:
                
                if rad == True:
                    rad = False
                    print("Esta como rad?: " , rad)
                    sp.sleep(1)
                    print(" ")
                if rad == False:
                    rad = True
                    print("Esta como rad?: " , rad)
                    sp.sleep(1)
                    print(" ")

            if opcion1 == 2:
                if debug == True:
                    debug = False  
                    print("modo debug?" + debug)
                    sp.sleep(1)
                    print(" ")

                if debug == False:
                    debug == True
                    print("modo debug?" + debug)
                    sp.sleep(1)
                    print(" ")

            if opcion1 == 3:
                if dein == True:
                    dein = False  
                    print("modo dein?" + dein)
                    sp.sleep(1)
                    print(" ")

                if dein == False:
                    dein == True
                    print("modo dein?" + dein)
                    sp.sleep(1)
                    print(" ")
            if opcion1 == 3:
                if redondear == True:
                    redondear = False  
                    print("modo dein?" + redondear)
                    sp.sleep(1)
                    print(" ")

                if redondear == False:
                    redondear == True
                    print("modo dein?" + redondear)
                    sp.sleep(1)
                    print(" ")
        if calc == True:
            if rad == True:
                calculo = np.radian(calculo)
            if debug == True:
                print("rad?/round? = " + rad + "/" + redondear)
            if redondear == True:
                calculo = np.round(calculo)

        print(colorama.Fore.GREEN + "El resultado es: " + str(calculo) + colorama.Fore.RESET)
        print("  ")
        print("  ")
    else:
        print(colorama.Fore.RED + "Opcion invalida" + colorama.Fore.RESET)
        sp.sleep(1)

    archivo.write(str(calculo) + str(rad) + str(debug) + str(dein) + "w" "\n")


# ejecutando el menu en la terminal
while True:
    menu()
#no se que hace esto 2.0
if dein == True:
    colorama.deinit()
