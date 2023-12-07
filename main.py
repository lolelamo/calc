import numpy as np
import colorama
import time as sp
import os


#init() de colorama ya no funciona, en cambio se debe utilizar colorama.init()
colorama.init()

#Se crean las variables
dein = True
redondear = False
calc = False
div_to_cos = False
ang_to_rad = False


# creando las definiciones para la mayoria de los calculos
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

print('''Se creara un archivo en la carpeta que esta este archivo
      https://github.com/lolelamo/calc <<< El github en el que esta este proyecto''')

# abriendo el archivo para guardar los calculos
archivo_ruta = "save.txt"
archivo = open(archivo_ruta, "a")

# el def principal que estara en un bucle infinito hasta que el usuario cierre la ventana o use
#el numero "13" 
def menu():
    #Las variables se haen globales y creo variables que estaran 
    #Volviendo a su valor por cada bucle

    global redondear
    global dein
    global div_to_cos
    global ang_to_rad
    calc = False
    calculo = 0.0
    exc = False

    # imprimiendo el menu
    print(colorama.Fore.GREEN + ''' [STCalc]
          Codigo por lole codigo hecho por un novato se espera errores en el codigo o algunas partes no se entiendan ''')
    print(" Lista de todas las operaciones matematicas disponibles:" + colorama.Fore.RESET + "\n")
    print(colorama.Fore.LIGHTGREEN_EX)
    print("{Operaciones basicas}: ")
    print("[1. Suma] [2. Resta] [3. Multiplicacion] [4. Division]")
    print("{Logaritmos}:")
    print("{Trigonometria}: ")
    print("[6. Seno] [7. Coseno] [8. Tangente] ")
    print("[9. Cosecante] [11. Secante] [12. Cotangente]")
    print("[12. Arco de Seno] [13. Arco de Coseno] [14. Arco de Tangente]")
    print("{Otros}: ")
    print("[15. Salir] [16. Opciones (No esta terminado)]")
    print(colorama.Fore.RESET)

    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    try:
        opcion = int(opcion)
    except ValueError:
        print(colorama.Fore.LIGHTRED_EX + "Err:4:" + colorama.Fore.RESET) 
        exc = True
        
    # validando la opcion del usuario
    if opcion >= 0 and opcion <= 16:

        # este If es para evitar errores
        if opcion == 0: 
            if exc == False:
                print("No has escogido nada...")
                sp.sleep(1)
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
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

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
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)
            
        elif opcion == 3:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                calculo = multiplicacion(operando1, operando2)
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 4:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            operando2 = input(colorama.Fore.GREEN + "Ingrese el segundo numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                calculo = division(operando1, operando2)
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 5:     
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)

            print("\n")
            try:
                operando1 = float(operando1)
                calculo = raiz_cuadrada(operando1)
                calc = True
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 6:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = seno(operando1)
                calc = True
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 7:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = coseno(operando1)
                calc = True
                
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 8:
            operando1 = input(colorama.Fore.GREEN + "ingrese un numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = tangente(operando1)
                calc = True
                
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 9:
            operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa Sin()")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = seno(operando2)
                calculo = 1 / operando1
            except:
                print("ERR:1: Ingresa un numero")


        elif opcion == 10:
            operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa Cos()")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = coseno(operando2)
                calculo = 1 / operando1
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 11:         
            print("\n")
            try:
                
                
                if div_to_cos == False:
                    operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa el Tangente" + colorama.Fore.RESET)
                    operando1 = float(operando1)
                    operando1 = tangente(operando1)
                    calculo = 1 / operando1
                    calc = True

                elif div_to_cos == True:
                    operando1 = input("Ingresa el Seno")
                    operando2 = input("ingresa el Coseno")
                    try:
                        operando1 = float(operando1)
                        operando2 = float(operando2)

                        operando1 = seno(operando1)
                        operando2 = coseno(operando2)

                        calculo = operando2 / operando1
                        calc = True
                    except ValueError:
                        print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)


            except:
                print("ERR:1: Ingresa un numero")

        elif opcion == 12:
            
            operando1 = input("Arcsin (utiliza un numero como minimo -1 y como maximo 1) \n")
            try:
                operando1 = float(operando1)
                if operando1 <= 1 and operando1 >= -1:
                    calculo = arcsin(operando1)
                    calc = True
                    
                else:
                    print(colorama.Fore.LIGHTRED_EX + "Err:2:, Solo numeros entre -1 y 1" + colorama.Fore.Reset)

            except ValueError:
                    print(colorama.Fore.LIGHTRED_EX + "ERR:1: Ingresa un numero" + colorama.Fore.RESET)
        elif opcion == 13:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            try:
                if operando1 <= 1 and operando1 >= -1:
                    calculo = arccos(operando1)
                    calc = True
                    
                else:
                    print(colorama.Fore.LIGHTRED_EX + "Err:2:, Solo numeros entre -1 y 1" + colorama.Fore.RESET)
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 14:
            operando1 = input("Ingresa un numero") 
            try:
                operando1 = float(operando1)
                calculo = arctan(operando1)
                calc = True
                

            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Error, SOLO numeros Reales" + colorama.Fore.RESET)

        #el codigo espera 2 segundos y termina (si el usuario pone el 9 para seleccionar)
        elif opcion == 15:
            if dein == True:
                colorama.deinit()
            sp.sleep(2)
            exit()

        elif opcion == 16:
            print(" ")
            print(" ")
            print("Config")
            print('''
            1. Dividir 1/tan() en vez de cos() / sin(), para sacar el cotangente || Desactivar / Activar, False por defecto 
            2. Cambiar de angulo a Radianes? || Desactivar / Activar, False por defecto
            3. deinit() || Desactivar / Activar,  True por defecto
            4. Redondear numero || Desactivar / Activar, False por Defecto
            5. Utilizar Coseno en vez de dividir por 1 para sacar el cotangente || Desactivar / Activar, False por defecto
            5. Reestablecer config
            6. Borrar save.txt''')

            opcion1 = input("ingresa un numero (1-6): ")
            try:
                opcion1 = int(opcion1)
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "ERR:1: Ingresa un numero" + colorama.Fore.RESET)
            if opcion1 >= 1 and opcion <= 6:
                if opcion1 == 1:
                
                    if div_to_cos == True:
                        div_to_cos = False
                        print("De angulo a radianes?: " , div_to_cos)
                        sp.sleep(1)
                        print(" ")
                    elif div_to_cos == False:
                        div_to_cos = True
                        print("De angulo a radianes?: " , div_to_cos)
                        sp.sleep(1)
                        print(" ")

                elif opcion1 == 2:
                    if ang_to_rad == True:
                        ang_to_rad = False  
                        print("" + ang_to_rad)
                        sp.sleep(1)
                        print("Angulo a Radiales? ")

                    elif ang_to_rad == False:
                        ang_to_rad == True
                        print("Angulo a Radiales?" + ang_to_rad)
                        sp.sleep(1)
                        print(" ")

                elif opcion1 == 3:
                    if dein == True:
                        dein = False  
                        print("usar el colorama.deinit()? " + dein)
                        sp.sleep(1)
                        print(" ")
                    elif dein == False:
                        dein == True
                        print("usar el colorama.deinit? " + str(dein))
                        sp.sleep(1)
                        print(" ")
                elif opcion1 == 4:
                    if redondear == True:
                        redondear = False  
                        print("Redondear?" + redondear)
                        sp.sleep(1)
                        print(" ")

                    elif redondear == False:
                        redondear == True
                        print("Redondear?" + redondear)
                        sp.sleep(1)
                        print(" ")
                elif opcion1 == 5:
                    Reestablecer()
                elif opcion1 == 6:
                    os.remove("save.txt")
                    archivo = open("save.txt")
            else:
                print(colorama.Fore.LIGHTRED_EX + "ERR:4: Valor fuera del rango, utiliza numeros del 1 al 6" + colorama.Fore.RESET)


        if calc == True:
            if ang_to_rad == True:
                calculo = np.radians(calculo)
            elif redondear == True:
                calculo = np.round(calculo)
            
            print(colorama.Fore.GREEN + "El resultado es: " + str(calculo) + colorama.Fore.RESET)
            sp.sleep(5)
            print("  ")
            print("  ")
            archivo = open(archivo_ruta, "a")
            archivo.write("Resultado = " + str(calculo) + "[el numero se redondeo?] = " + str(redondear) + "\n")
    else:
        print(colorama.Fore.RED + "Opcion invalida" + colorama.Fore.RESET)
        sp.sleep(1)

def Reestablecer():
    global dein
    global redondear
    global calc
    global div_to_cos
    global ang_to_rad
    
    dein = True
    redondear = False
    calc = False
    div_to_cos = False
    ang_to_rad = False
# ejecutando el menu en la terminal
while True:
    menu()
