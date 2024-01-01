from rich.console import Console
from rich.table import Table
from rich.theme import Theme

# dependencias:
# numpy
# rich
# keyboard

import time as sp
import numpy as np
import warnings
import keyboard

temas = Theme({
    "Error": "bold bright_red",
    "Info": "italic bright_blue ",
    "Error_except_secondary": "italic bright_red",
}) 

console = Console(theme=temas)

# Este código puede contener errores o partes ineficientes
# Esta versión utiliza Rich en vez de Colorama
# 1.1v

console.print("el Github del projecto", style="link https://github.com/lolelamo/calc")
console.print("STCalc - Calculadora de Trigonometria y logaritmos (en desarrollo d:)", style="Info")
console.print(
    "[italic]Codigo hecho por lole "
    "Algunos colores y demas cosas de rich no son compatibles con todo las terminales[/italic] \n"
)


################################## Tablas del modulo Rich ##################################
# 1ra tabla
tabla = Table(title="Operaciones matematicas")
tabla.add_column("ID: ")
tabla.add_column("Aritmetica")
tabla.add_column("ID: ")
tabla.add_column("Logaritmos")
tabla.add_column("ID: ")
tabla.add_column("Trigonometria")

tabla.add_row("1 | 2", "Suma | Resta", "6 | 7", "Log. en base 2 | Log. en base 10", "10 | 11", "Seno | Coseno")
tabla.add_row("3 | 4", "Multiplicacion | Division", "8 | 9", "Log. natural | Log. en cualquier base", "12 | 13", "Tangente | Cosecante")
tabla.add_row("5", "Raiz cuadrada", "", "", "14 | 15", "Secante | Cotangente")
tabla.add_row("", "", "", "", "16 | 17", "Arco de Seno | Arco de Coseno")
tabla.add_row("", "", "", "", "18", "Arco de Tangente")

# 2da tabla 
tabla_2 = Table()
tabla_2.add_column("ID:", justify="center")
tabla_2.add_column("")
tabla_2.add_row("19", "Salir")
tabla_2.add_row("20", "Configuracion")
# tabla_2.add_row("21", "Calculadora") otro dia hago una calculadora con todo junto, en vez de ir escogiendo una funcion

# 3ra tabla para la configuracion
tabla_config = Table(title="Config.")
tabla_config.add_column("ID")
tabla_config.add_column("Opciones")
tabla_config.add_column("Uso: ")
tabla_config.add_column("Por defecto:", style="Info")


tabla_config.add_row("1.", "Dividir cos()/sin() en vez de 1/tan(), para sacar el cotangente",  "Desactivar / Activar", "False")
tabla_config.add_row("2.", "Cambiar angulo a Radianes?",  "Desactivar / Activar", "False")
tabla_config.add_row("3.", "Redondear numero",  "Desactivar / Activar", "False")
tabla_config.add_row("4.", "Invertir la coma por un punto",  "Desactivar / Activar", "False")
tabla_config.add_row("5.", "Reestablecer configuración")
tabla_config.add_row("6.", "Historial", "Ver para ver la lista y borrar para eliminar toda el historial")
tabla_config.add_row("7.", "Volver al menu principal")


# Esto es para aumentar la precision de los decimales (necesito probarlo mas+)
np.set_printoptions(precision=64)


redondear = False
calc = False
div_to_cos = False
ang_to_rad = False
dot_to_coma = False
configbug = False
historial = []

# Una tabla que intenta simular las tablas de rich, ya que las tablas de rich no soportan 
# la eliminacion de columnas o filas
def tabla_falsa():
    global div_to_cos, ang_to_rad, redondear, dot_to_coma
    
    strings = [str(div_to_cos), str(ang_to_rad), str(redondear), str(dot_to_coma)]
    console.print("    Estado", style="italic red")
    print("┌─────────────┐")

    for i, s in enumerate(strings, start=1):
        print(f"│ [{i}] │ {s} {' ' * (5 - len(s))}│")

        if i < len(strings):
            print("├─────────────┤")

    print("└─────────────┘" + "\n")


sp.sleep(1.8)

# abriendo el archivo para guardar los calculos, sigo sin saber como va el jodidisimo open(), funciona como se le da la gana
# ya no se que hacer con ese open, crea el archivo historial_calculadora.txt donde se le da la putisima gana

archivo_ruta = "historial_calculadora.txt"
archivo = open(archivo_ruta, "a")

################################## Bucle principal ##################################

def menu():
    global redondear, div_to_cos, ang_to_rad, console
    calc = False
    resultado = 0

    console.print(tabla)
    console.print(tabla_2)
    
    opcion = input("Opcion: ")
    try:
        opcion = int(opcion)
    except ValueError:
        print("Solo numero entre 1-22, sin decimales") 
        sp.sleep(0.85)
        opcion = 0
        
    if opcion >= 1 and opcion <= 22:
        if opcion == 1:
            list_suma = []
            while True:
                console.print("utiliza salir o exit para regresar a la seleccion de operaciones" + "\n")
                opcion_lista = input("Ingresa un numero para sumar: ")
                try:
                    if opcion_lista.lower() in ["salir", "exit"]:
                        sp.sleep(0.2)
                        break 
                    opcion_lista = float(opcion_lista)
                    list_suma.append(opcion_lista)
                    
                    resultado = sum(list_suma)
                    print(f"Resultado: {resultado}" + "\n")
                    calc = True
  
                except Exception as ex:
                    if ex == ValueError:
                        console.print("Debes ingresar un numero...", style="Error")
                    else:
                        print("Error desconocido" + "\n")
                        print("Excepcion:\n")
                        print(str(ex))
                        sp.sleep(0.8)
                        break

        elif opcion == 2:
                operando1 = input("Primer numero: ")
                operando2 = input("Segundo numero: ")
                try:
                    operando1 = float(operando1)
                    operando2 = float(operando2)
                    resultado = operando1 - operando2
                    calc = True

                except Exception as e:
                    if e == ValueError:
                        console.print("Debes ingresar un numero...", style="Error")
                        sp.sleep(1.2)
                    else:
                        console.print("Error", style="Error_exception_secondary")
            
        elif opcion == 3:
            operando1 = input("Primer numero: ")
            operando2 = input("Segundo numero: ")
            print("\n")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                resultado = operando1 * operando2
                calc = True
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 4:

            operando1 = input("Primer numero: ")
            operando2 = input("Segundo numero: ")

            print("\n")

            try:
                operando1 = float(operando1)
                operando2 = float(operando2)
                resultado = operando1 / operando2
                calc = True
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")

                elif e == ZeroDivisionError:
                    console.print("No se puede Dividir por 0", style="Error_except_secondary")
                else:
                    console.print("Error", style="Error_except_secondary")

        elif opcion == 5:     
            operando1 = input("(Raiz cuadrada) Ingrese el primer numero: ")

            print("\n")
            try:
                operando1 = float(operando1)
                resultado = np.sqrt(operando1)
                calc = True 
                print("\n")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")


        elif opcion == 6:
            operando1 = input("(Logaritmo en base 2) Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                resultado = np.log2(operando1)
                calc = True
                print("\n")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

                sp.sleep(1.2)
        elif opcion == 7:
            operando1 = input("(Logaritmo en base 10) Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                resultado = np.log10(operando1)
                calc = True
                print("\n")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 8:
            operando1 = input("(Logaritmo natural) Ingrese un numero: ")
            try:
                operando1 = float(operando1)
                resultado = np.log(operando1)
                calc = True
                print("\n")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")
            
        elif opcion == 9:
            operando1 = input("Ingresa Logaritmo: ")
            operando2 = input("Ingresa el Valor de la base: ")
            try:
                operando1 = float(operando1)
                operando2 = float(operando2)

                resultado = np.log(operando1) / np.log(operando2)
                print(f"El logaritmo de {operando1} en base {operando2} es:")

                sp.sleep(0.9)
                calc = True
                

            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 10:
            operando1 = input("Ingresa un numero para calcular el Sin(): ")
            print("\n")
            try:
                operando1 = float(operando1)
                resultado = np.sin(operando1)
                calc = True
                print("\n")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 11:
            operando1 = input("Ingresa un numero para calcular el Cos(): ")
            print("\n")
            try:
                operando1 = float(operando1)
                resultado = np.cos(operando1)
                calc = True
                
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 12:
            operando1 = input("Ingresa un numero para calcular el Tan(): ")
            print("\n")
            try:
                operando1 = float(operando1)
                resultado = np.tan(operando1)
                calc = True
                
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")
        elif opcion == 13:
            operando1 = input("Ingresa un numero para calcular el Csc()")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = np.sin(operando2)
                resultado = 1 / operando1
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                elif e == ZeroDivisionError:
                    console.print("No se puede dividir por 0", style="Error_exception_secondary")
                    sp.sleep(0.6)
                else:
                    console.print("Error", style="Error_exception_secondary")
                    sp.sleep(0.3)


        elif opcion == 14:
            operando1 = input("Ingresa un numero para calcular el Sec()")
            print("\n")

            try:
                operando1 = float(operando1)
                calc = True
                
                operando1 = np.cos(operando2)
                resultado = 1 / operando1
            except:
                print("Debes ingresar un numero...", style="Error")

        elif opcion == 15:         
            print("\n")
            with warnings.catch_warnings():
                warnings.filterwarnings("error")  
                if div_to_cos == False:
                    operando1 = input("Ingresa Tan(): ")
                    
                    try:
                        operando1 = float(operando1)
                        operando1 = np.tan(operando1)
                        resultado = 1 / operando1
                        calc = True

                    except Exception as e:
                        if e == ValueError:
                            console.print("Debes ingresar un numero...", style="Error")
                        elif e == RuntimeWarning or ZeroDivisionError:
                            console.print("No se puede dividir por 0", style="Error")
                            sp.sleep(0.7)
                            
                        else:
                            console.print("Error \n", style="Error_except_secondary")
                            print(str(e))

                elif div_to_cos == True:
                    operando1 = input("Ingresa Cos(): ")
                    operando2 = input("ingresa Sin(): ")
                    try:
                        operando1 = float(operando1)
                        operando2 = float(operando2)

                        operando1 = np.cos(operando1)
                        operando2 = np.sin(operando2)

                        resultado = operando1 / operando2

                        print(f"Cos({operando2})) / Sin({operando1})")
                        sp.sleep(0.3)
                        calc = True
                    except Exception as e:
                        if e == RuntimeError or RuntimeWarning or ZeroDivisionError:
                            console.print("No se puede dividir por 0", style="Error")
                            sp.sleep(0.6)
                        elif e == ValueError:
                            console.print("Debes ingresar un codigo", style="Error")
                            sp.sleep(0.7)
                        else:
                            console.print("Error", style="Error_exception_secondary")

        elif opcion == 16:
            
            operando1 = input("Ingresa un numero:  \n")
            try:
                operando1 = float(operando1)
                if operando1 <= 1 and operando1 >= -1:
                    resultado = np.arcsin(operando1)
                    calc = True
                else:
                    print("Solo numeros entre -1 y 1")

            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 17:
            operando1 = input("Ingresa un numero del, Arcos (utiliza un numero como minimo -1 y como maximo 1) \n")
            try:
                operando1 = float(operando1)
                if operando1 <= 1 and operando1 >= -1:
                    resultado = np.arccos(operando1)
                    calc = True
                    
                else:
                    print("Solo numeros entre -1 y 1")
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 18:
            operando1 = input("Ingresa un numero") 
            try:
                operando1 = float(operando1)
                resultado = np.arctan(operando1)
                calc = True
                
            except Exception as e:
                if e == ValueError:
                    console.print("Debes ingresar un numero...", style="Error")
                    sp.sleep(1.2)
                else:
                    console.print("Error", style="Error_exception_secondary")

        elif opcion == 19:
            sp.sleep(1.2)
            exit()

        elif opcion == 20:
            config()
        
        if calc == True:
            if ang_to_rad == True:
                resultado = np.radians(resultado)
            if redondear == True:
                resultado = np.round(resultado)
                resultado = int(resultado)
            if dot_to_coma == True:
                resultado = str(resultado).replace(".", ",")
            
            print("El resultado es: \n" + str(resultado))

            console.print("Presiona enter para seguir", style="Info")
            keyboard.wait("enter")

            historial.append(resultado)


            print("\n")

            archivo = open(archivo_ruta, "a")
            archivo.write("Resultado = " + str(resultado) + "  [ el numero se redondeo? ] = " + str(redondear) + "\n")

################################## Configuracion ################################## 
            
def config():
    global redondear, calc, div_to_cos, ang_to_rad, dot_to_coma, configbug, tabla_config, historial
    tabla_falsa()
    console.print(tabla_config)                         
    opcionconfig = input("ingresa un numero (1-6): ")
    try:
        opcionconfig = int(opcionconfig)
        if opcionconfig >= 1 and opcionconfig <= 6:
            if opcionconfig == 1:
                if div_to_cos == True:
                    div_to_cos = False
                    configbug = True

                    print("[1]:  Cambiar 1/tan por cos / sin para cotangente = " + str(div_to_cos))
                    sp.sleep(1)
                    print(" ")
                
                        

                elif div_to_cos == False and configbug == False:
                    div_to_cos = True

                    print("[1]: Cambiar 1/tan por cos / sin para cotangente = " + str(div_to_cos))

                    sp.sleep(2.6)
                    print(" ")

            elif opcionconfig == 2:
                if ang_to_rad == True:

                    configbug = True
                    ang_to_rad = False  

                    print("[2]: Angulo a Radiales = " + str(ang_to_rad))
                    sp.sleep(1.8)

                elif ang_to_rad == False and configbug == False:
                    ang_to_rad = True
                    print("[2]: Angulo a Radiales =  " + str(ang_to_rad))
                    sp.sleep(1.8)

                    print(" ")

            elif opcionconfig == 3:
                if redondear == True:
                    redondear = False  
                    configbug = True

                    print("[3]: ¿Redondear numeros? =" + str(redondear))
                    sp.sleep(1.3)

                    print(" ")

                elif redondear == False and configbug == False:
                    redondear = True

                    print("[3]: ¿Redondear numeros? =" + str(redondear))
                    sp.sleep(1.3)
                    print(" ")

            elif opcionconfig == 4:
                if dot_to_coma == True:
                    dot_to_coma = False
                    configbug = True
                    print("[4]: ¿se invirtio el punto por una coma para los decimales? =" + str(dot_to_coma))
                    sp.sleep(2)
                    print(" ")

                elif dot_to_coma == False and configbug == False:
                    dot_to_coma = True

                    print("[4]: ¿se invirtio el punto por una coma para los decimales? =" + str(dot_to_coma))

                    sp.sleep(2)
                    print(" ")

            elif opcionconfig == 5:

                redondear = False
                calc = False
                div_to_cos = False
                ang_to_rad = False
                dot_to_coma = False

                console.print("Se reestablecieron las variables a False", style="bold dim")
                                                                                                                                                              
                sp.sleep(1.5)
            elif opcionconfig == 6:
                historial_input = input("\n ... : " + "\n")
                if historial_input.lower() in ["borrar", "delete"]:
                    historial = []
                    print(historial)

                elif historial_input.lower() == "ver":
                    for i, resultado_historial in enumerate(historial, start=1):
                        print(f"[{i}]  {resultado_historial}")
                    keyboard.wait("enter")
                else:
                    print("\n")
                    console.print("Error", style="Error_except_secondary")
            elif opcionconfig == 7:
                print("...")
                sp.sleep(0.15)
        else:
            print("Numero fuera del rango")
    except ValueError:
        print("Ingresa un numero")

while True:
    menu()
