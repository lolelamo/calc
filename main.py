import numpy as np
import colorama
import time as sp




#init() de colorama ya no funciona, en cambio se debe utilizar colorama.init()
colorama.init()

#Se crean las variables
var = False
rad = False
dein = False
redondear = False
debug = False
calc = False


# abriendo el archivo para guardar los calculos
archivo = open("save.txt")

# creando las definiiones para la mayoria de los calculos
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

archivo_path = "save.txt"
archivo = open(archivo_path, "a")

# el def principal que estara en un bucle infinito hasta que el usuario cierre la ventana o use
#el numero "13" 
def menu():
    # abriendo el archivo para guardar los calculos
    global rad
    global redondear
    global debug
    global var
    global dein
    calc = False
    calculo = 0.0
    exc = False
    trigonometria = False

    # imprimiendo el menu
    print(''' [STCalc]
          Code by lole, free to use :D, codigo hecho por un novato se espera errores en el codigo o algunas partes no se entiendan ''')
    print(" Lista de todas las operaciones matematicas disponibles:" + "\n")
    
    print("{Operaciones basicas}: ")
    print("[1 +Suma] [2 Resta] [3 *Multiplicacion] [4 Division]")
    print("{Logaritmos}:")
    print("{Trigonometria}: ")
    print("[6 Seno] [7 Coseno] [8 Tangente] ")
    print("[9 Arco de Seno] [11 Arco de Coseno] [12 Arco de Tangente]")
    print("{Otros}: ")
    print("[13- Salir] [14- Opciones (No esta terminado)]")


    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    try:
        opcion = int(opcion)
    except ValueError:
        print(colorama.Fore.LIGHTRED_EX + "Error" + colorama.Fore.RESET) 
        opcion = 0
        exc = True
        
    # validando la opcion del usuario
    if opcion >= 0 and opcion <= 14:

        # If para evitar errores
        if opcion == 0: 
            if exc == False:
                print("No has escogido nada")
            if exc == True:
                print("" + "\n")
            sp.sleep(3)
        #elifs para comprobar la opcion del usuario

        elif opcion == 1:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)  
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            
            print(" ")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                calculo = suma(operando1, operando2)
                calc = True
            except ValueError:
                print("ERR:1: Ingresa un numero")
                opcion = 1

        elif opcion == 2:
            
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print("\n") 
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                calculo = resta(operando1, operando2)
                calc = True
            except ValueError:
                print("ERR:1: Ingresa un numero")
            
        elif opcion == 3:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print("\n")

            calculo = multiplicacion(operando1, operando2)
        elif opcion == 4:
            calc = True

            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print("\n")

            calculo = division(operando1, operando2)
        elif opcion == 5:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print("\n")

            calculo = raiz_cuadrada(operando1)
        elif opcion == 6:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print("\n")

            calculo = seno(operando1)
        elif opcion == 7:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print("\n")

            calculo = coseno(operando1)
        elif opcion == 8:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "ingrese un numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            print("\n")

            calculo = tangente(operando1)
        elif opcion == 9:
            calc = True
            trigonometria = True
            operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa Cos()")
            operando1 = float(operando1)
            print("\n")

            operando1 = tangente(operando2)
            operando1 = 1 / operando1

            calculo = operando1 / operando2

        elif opcion == 10:
            
            operando1 = input("Arcsin (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            if operando1 <= 1 and operando1 >= -1:
                calculo = arcsin(operando1)
                calc = True
            else:
                print(colorama.Fore.LIGHTRED_EX + "Err:2:, numeros menores que -1 O mayores que 1 no se permiten para arcsin" + colorama.Fore.Reset)
         
        elif opcion == 11:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            if operando1 <= 1 and operando1 >= -1:
                calculo = arccos(operando1)
                calc = True
            else:
                print(colorama.Fore.LIGHTRED_EX + "Error, numeros menores que -1 O mayores que 1 no se pueden usar" + colorama.Fore.RESET)


        elif opcion == 12:
            operando1 = input("Ingresa un numero") 
            operando1 = float(operando1)

            try:
                calculo = arctan(operando1)
                calc = True
            except ValueError or RuntimeWarning:
                print(colorama.Fore.LIGHTRED_EX + "Error, SOLO numeros Reales" + colorama.Fore.RESET)

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
            1. cambiar de angulo a radianes (Funvion sin uso por el momento, Desactivar / Activar, False por defecto) 
            2. debug (Funcion sin uso por el momento, Desactivar / Activar,  False por defecto)
            3. deinit() (Desactivar / Activar,  True por defecto)
            4. Redondear numero (Desactivar / Activar, False por Defecto)
            5. Reestablecer config
            6. Borrar save.txt''')

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
                    print("modo dein?" + str(dein))
                    sp.sleep(1)
                    print(" ")
            if opcion1 == 4:
                if redondear == True:
                    redondear = False  
                    print("Redondear?" + redondear)
                    sp.sleep(1)
                    print(" ")

                if redondear == False:
                    redondear == True
                    print("Redondear?" + redondear)
                    sp.sleep(1)
                    print(" ")
        if calc == True:
            if trigonometria == True:
                calculo = np.radians(calculo)
            if redondear == True:
                calculo = np.round(calculo)
        if calc == True:
            print(colorama.Fore.GREEN + "El resultado es: " + str(calculo) + colorama.Fore.RESET)
            sp.sleep(5)
            print("  ")
            print("  ")
            archivo = open(archivo_path, "a")
            archivo.write("Resultado = " + str(calculo) + "[el numero se redondeo?] = " + str(redondear) + "\n")
    else:
        print(colorama.Fore.RED + "Opcion invalida" + colorama.Fore.RESET)
        sp.sleep(1)




# ejecutando el menu en la terminal
while True:
    menu()
