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
def logaritmo10(a):
    return np.log10(a)
def logaritmo2(a):
    return np.log2(a)
def lognatural(a):
    return np.log(a)


print('''Se creara un archivo en la carpeta que esta este archivo
      https://github.com/lolelamo/calc <<< El github en el que esta este proyecto''')
print(colorama.Fore.GREEN + ''' [STCalc]
    Codigo por lole codigo hecho por un novato se espera errores en el codigo o algunas partes no se entiendan ''')
print(" Lista de todas las operaciones matematicas disponibles:" + colorama.Fore.RESET + "\n")

# abriendo el archivo para guardar los calculos
archivo_ruta = "save.txt"
archivo = open(archivo_ruta, "a+")

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

    print(colorama.Fore.LIGHTGREEN_EX)
    print("{Operaciones basicas}: ")
    print("[1. Suma] [2. Resta] [3. Multiplicacion] [4. Division]")
    
    print("{Raiz cuadrada}: [5. Raiz cuadrada]")
    
    print("{Logaritmos}:")
    print("[6. Logaritmo en base 2] [7. Logaritmo en base 10] [8. Logaritmo natural]")
    print("[9. Logaritmo en cualquier base]")

    print("{Trigonometria}: ")
    print("[10. Seno] [11. Coseno] [12. Tangente] ")
    print("[13. Cosecante] [14. Secante] [15. Cotangente]")
    print("[16. Arco de Seno] [17. Arco de Coseno] [18. Arco de Tangente]")

    print("{Otros}: ")
    print("[19. Salir] [20. Opciones (No esta terminado)]")
    print(colorama.Fore.RESET)

    # pidiendo la opcion del usuario
    opcion = input(colorama.Fore.YELLOW + "Opcion: " + colorama.Fore.RESET)
    try:
        opcion = int(opcion)
    except ValueError:
        print(colorama.Fore.LIGHTRED_EX + "Err:4:" + colorama.Fore.RESET) 
        exc = True
        
    # validando la opcion del usuario
    if opcion >= 0 and opcion <= 20:

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
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)

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
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
            
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
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)

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
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 5:     
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)

            print("\n")
            try:
                operando1 = float(operando1)
                calculo = raiz_cuadrada(operando1)
                calc = True 
                print("\n")
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 6:
            operando1 = input("Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                calculo = logaritmo2(operando1)
                calc = True
                print("\n")
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 7:
            operando1 = input("Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                calculo = logaritmo10(operando1)
                calc = True
                print("\n")
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 8:
            operando1 = input("Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                calculo = lognatural(operando1)
                calc = True
                print("\n")
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
            
        elif opcion == 9:
            operando1 = input("Ingrese el Valor: ")
            operando2 = input("ingrese el Valor de la base: ")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)

                calculo = lognatural(operando1) / lognatural(operando2)
                print("\n")
                calc = True
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 10:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = seno(operando1)
                calc = True
                print("\n")
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 11:
            operando1 = input(colorama.Fore.GREEN + "Ingrese el primer numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = coseno(operando1)
                calc = True
                
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 12:
            operando1 = input(colorama.Fore.GREEN + "Ingrese un numero: " + colorama.Fore.RESET)
            print("\n")
            try:
                operando1 = float(operando1)
                calculo = tangente(operando1)
                calc = True
                
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)
        elif opcion == 13:
            operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa Sin()")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = seno(operando2)
                calculo = 1 / operando1
            except:
                print("ERR:1: Ingresa un numero")


        elif opcion == 14:
            operando1 = input(colorama.Fore.LIGHTGREEN_EX + "Ingresa Coseno")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = coseno(operando2)
                calculo = 1 / operando1
            except:
                print(colorama.Fore.LIGHTRED_EX + "Err:1: Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 15:         
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

        elif opcion == 16:
            
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
        elif opcion == 17:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            try:
                if operando1 <= 1 and operando1 >= -1:
                    calculo = arccos(operando1)
                    calc = True
                    
                else:
                    print(colorama.Fore.LIGHTRED_EX + "Err:2:, Solo numeros entre -1 y 1" + colorama.Fore.RESET)
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Err:1:, Ingresa un numero" + colorama.Fore.Reset)

        elif opcion == 18:
            operando1 = input("Ingresa un numero") 
            try:
                operando1 = float(operando1)
                calculo = arctan(operando1)
                calc = True
                

            except ValueError:
                print(colorama.Fore.LIGHTRED_EX + "Error, SOLO numeros Reales" + colorama.Fore.RESET)

        #el codigo espera 2 segundos y termina (si el usuario pone el 9 para seleccionar)
        elif opcion == 19:
            if dein == True:
                colorama.deinit()
            sp.sleep(2)
            exit()

        elif opcion == 20:
            config()


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
        print(colorama.Fore.RED + "ERR:4: Opcion invalida " + colorama.Fore.RESET)
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

def config():
    global dein
    global redondear
    global calc
    global div_to_cos
    global ang_to_rad

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

    opcionconfig = input("ingresa un numero (1-6): ")
    try:
        opcionconfig = int(opcionconfig)
        if opcionconfig >= 0 and opcionconfig <= 6:

            if opcionconfig == 1:
                if div_to_cos == True:
                    div_to_cos = False
                    print("De angulo a radianes?: " + str(div_to_cos))
                    sp.sleep(1)
                    print(" ")
                if div_to_cos == False:
                    div_to_cos = True
                    print("De angulo a radianes?: " + str(div_to_cos))
                    sp.sleep(1)
                    print(" ")

            if opcionconfig == 2:
                if ang_to_rad == True:
                    ang_to_rad = False  
                    print("Angulo a Radiales? " + str(ang_to_rad))
                    sp.sleep(1)
                    print("Angulo a Radiales? " + str(ang_to_rad))

                if ang_to_rad == False:
                    ang_to_rad == True
                    print("Angulo a Radiales?" + str(ang_to_rad))
                    sp.sleep(1)
                    print(" ")

            if opcionconfig == 3:
                if dein == True:
                    dein = False  
                    print("usar el colorama.deinit()? " + str(dein))
                    sp.sleep(1)
                    print(" ")
                if dein == False:
                    dein == True
                    print("usar el colorama.deinit? " + str(dein))
                    sp.sleep(1)
                    print(" ")
            if opcionconfig == 4:
                if redondear == True:
                    redondear = False  
                    print("Redondear?" + str(redondear))
                    sp.sleep(1)
                    print(" ")

                if redondear == False:
                    redondear == True
                    print("Redondear?" + str(redondear))
                    sp.sleep(1)
                    print(" ")
            if opcionconfig == 5:
                Reestablecer()
            if opcionconfig == 6:
                os.remove("save.txt")
                archivo = open("save.txt")

    except ValueError:
        print(colorama.Fore.LIGHTRED_EX + "ERR:1: Ingresa un numero" + colorama.Fore.RESET)
            
            #else:
                #print(colorama.Fore.LIGHTRED_EX + "ERR:4: Opcion invalida " + colorama.Fore.RESET)
                #sp.sleep(2)

# ejecutando el menu en la terminal
while True:
    menu()
