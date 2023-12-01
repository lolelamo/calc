import numpy as np
import colorama
import time as sp
#no se que hace esto
colorama.init()

variablesinit = {
    "var": False,
    "rad": False,
    "dein": False,
    "redondear": False,
    "debug": False,
    "calc": False,

}

# abriendo el archivo para guardar los calculos
archivo = open("save.txt")

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




def menu():
    # abriendo el archivo para guardar los calculos
    archivo = open("save.txt", "a")
    var = variablesinit["var"]
    debug = variablesinit["debug"]
    calc = variablesinit["calc"]
    dein = variablesinit["dein"]
    redondear = variablesinit["redondear"]
    rad = variablesinit["rad"]
    calculo = 0.0

    # imprimiendo el menu
    print(''' [STCalc]
          Code by lole, free to use :D, codigo hecho por un novato se espera errores en el codigo o algunas partes no se entiendan ''')
    print(" Lista de todas las operaciones matematicas disponibles:" + "\n")
    
    print('''          {Operatoria basica y la Raiz cuadrada}: ''' + colorama.Fore.LIGHTGREEN_EX + '''
          [1- Suma] [2- Resta] [3- Multiplicacion] [4- Division] ''' + colorama.Fore.RESET + colorama.Fore.GREEN + '''
          [5- Raiz cuadrada] ''' +  colorama.Fore.RESET  + colorama.Fore.LIGHTCYAN_EX + ''' 
          {Trigonometria}: ''' + colorama.Fore.RESET + colorama.Fore.CYAN + '''
          [6- Seno] [7- Coseno] [8- Tangente]
          [9- Arco de (Seno numeros del -1 al 1)] [10- Arco de Coseno (numeros del -1 al 1)] [11- Arco de Tangente (solo numeros reales)]''' + colorama.Fore.RESET + '''
          [12- Salir del programa] [13- Configuracion]''' )



    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    opcion = int(opcion)

    # validando la opcion del usuario
    if opcion >= 1 and opcion <= 13:

        # pidiendo los operandos (variables) para los numeros

        # los ifs y elifs para escoger el tipo de calculo
        if opcion == 1:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)

            print("\n")

            calculo = suma(operando1, operando2)

        elif opcion == 2:
            calc = True
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando1 = float(operando1)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            operando2 = float(operando2)
            print("\n")

            calculo = resta(operando1, operando2)
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
            operando1 = input("Arcsin (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            try:
                calculo = arcsin(operando1)
                calc = True
            except ValueError or RuntimeWarning:
                print(colorama.Fore.LIGHTRED_EX + "Error, numeros menores que -1 O mayores que 1 no se permiten para arcsin" + colorama.Fore.Reset)
         
        elif opcion == 10:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            operando1 = float(operando1)
            try:
                calculo = arccos(operando1)
                calc = True
            except ValueError or RuntimeWarning:
                print(colorama.Fore.LIGHTRED_EX + "Error, numeros menores que -1 O mayores que 1 no se permiten para arccos" + colorama.Fore.Reset)

        elif opcion == 11:
            operando1 = input(" Arctan (utiliza un numero Real) \n")
            operando1 = float(operando1)

            try:
                calculo = arctan(operando1)
                calc = True
            except ValueError or RuntimeWarning:
                print(colorama.Fore.LIGHTRED_EX + "Error, SOLO numeros Reales" + colorama.Fore.Reset)

        #el codigo espera 2 segundos y termina (si el usuario pone el 9 para seleccionar)
        elif opcion == 12:
            if dein == True:
                colorama.deinit()
            sp.sleep(2)
            exit()


        elif opcion == 13:
            print(" ")
            print(" ")
            print("Config")
            print('''
            1. cambiar rad por deg (Desactivar / Activar, Funcion no testeada)
            2. debug (Funcion sin uso por el momento, Desactivar / Activar)
            3. deinit() (Desactivar / Activar)
            4. Redondear numero (Desactivar / Activar)''')

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
            if rad == True:
                calculo = np.radian(calculo)
            if debug == True:
                print("rad?/round? = " + rad + "/" + redondear)
            if redondear == True:
                calculo = np.round(calculo)

        print(colorama.Fore.GREEN + "El resultado es: " + str(calculo) + colorama.Fore.RESET)
        sp.sleep(5)
        print("  ")
        print("  ")
        archivo.write("Resultado = " + str(calculo) + " [esta como puesto como radiales?] = " + str(rad) +" [el numero se redondeo?] = " + str(redondear) + "\n" + "\a")
    else:
        print(colorama.Fore.RED + "Opcion invalida" + colorama.Fore.RESET)
        sp.sleep(1)




# ejecutando el menu en la terminal
while True:
    menu()

