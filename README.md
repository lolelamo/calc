### Introducción

Este proyecto fue creado en vscode esto era una tarea de la escuela, debiamos pedirle a una IA que nos genere un codigo con
8 defs, sobre operaciones matematicas, sin especificar nada

este proyecto no es para nada serio,  es solo para aprender y asi no me olvido xD

* * *

### Codigo por la IA

Para ahorrar tiempo, utilice la base del código hecho por la IA
estos 8 defs son de la IA (Bard):

``` python
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
```

### Explicacion del codigo

utilicé una cadena de `elif` para las opciones del 0 al 14, donde el 1 al 12 corresponden a las operaciones matemáticas y el 13
sirve para salir del código.

al principio pide un input y se valida, si es un str dara una excepcion
cuando de esa excepcion el `except` se utilizara y se activara la variable `exc` y `opcion` se pondra como = 0
como `exc` estara True dara un print diferente y asi seguira el bucle :D

PYTHON:

```
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
ETC...

```

* * *

### Dependencias

* ```Numpy```
* ```Python```  
* ```Colorama```  

* * *

### Cosas que pienso añadir

En el futuro, me gustaría hacer lo siguiente: (en orden)

* Arreglar errores.
* Añadir más operaciones matemáticas, faltan logaritmos, trigonometria y mas cosas.
* Cambiar de Colorama a Rich, no necesariamente quitar colorama.
* Añadir tablas, barras de carga y mas.
* Hacer que el código sea más entedible

* * *

### Cambios realizados  

* 0.5: También hice algunas mejoras al código, como agregar variables ```global```
* 0.6: cambié por completo el print del inicio para hacerlos mas bonito y ordenado. También añadí las funciones ```arcsin()```, ```arccos()```, y ```arctan()```. Además, quité las variables globales, elimine el ```deinit()``` fuera del bucle. Ahora el ```archivo.write()``` funciona correctamente.
* 0.6.1: Quite el ```deinit()``` porque no lo habia eliminado, para ```sin() cos() tan()``` y sus ```arc``` en vez de "Trigonometria" le habia puesto "Logaritmos"
* 0.7: Arregle por completo la configuracion, elimine las variables `var` `debug` y añadi `div_to_cos` `ang_to_cos` si div_to_cos es False para sacar el Cotangente se usara 1/tan y si es True cos/sin
ahora todos los inputs arrojaran un texto de error si se pone un texto o un numero fuera del rango de los inputs para seleccionar una funcion, Añadi una funcion para Reestablecer las variables y otra para       eliminar el save.txt, estas dos funciones estan en la configuracion

* * *
Errores que conozco:

* ~~Si escribes un STRING en cualquier input va a dar error~~  
* algunas funciones de Trigonometria si les pones un numero que no corresponde te lanzara un error pero no una excepcion  
  por lo que sigue funcionando el codigo  
* ~~todas las funciones de la config estan o rotas o no funcionan del todo bien~~  
* ~~Los nombres de las variables son algo confusas o no tienen funcion~~  
  
* * *
