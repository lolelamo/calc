### Introducción

Este proyecto fue creado en vscode esto era una tarea de la escuela, debiamos pedirle a una IA que nos genere un codigo con
8 defs, sobre operaciones matematicas, sin especificar nada

este proyecto no es para nada serio,  es solo para aprender

* * *

### Explicación del código

Para ahorrar tiempo, utilice la base del código hecho por la IA 

```
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


También utilicé una cadena de `elif` para las opciones del 1 al 9, donde el 1 al 8 corresponden a las operaciones matemáticas y el 9 sirve para salir del código.
```
python
opcion = int(input("¿Qué operación quieres realizar? (1-8)"))
if opcion == 1:
    # codigo de Suma
elif opcion == 2:
    # codigo de Resta
etc...
```

* * *

### Dependencias
* ```Numpy```:   
* ```Python```:  
* ```Colorama```:  

* * *

### Cosas que pienso añadir:

En el futuro, me gustaría hacer lo siguiente:

* Arreglar errores.
* Añadir más operaciones matemáticas.
* Cambiar de Colorama a Rich, no necesariamente quitar colorama.
* Añadir tablas, barras de carga y mas.
* Hacer que el código sea más entedible

* * *

### Cambios realizados

* En la versión 0.5 También hice algunas mejoras al código, como agregar variables ```global```
* En la versión 0.6, cambié por completo el print del inicio para hacerlos mas bonito y ordenado. También añadí las funciones ```arcsin()```, ```arccos()```, y ```arctan()```. Además, quité las variables globales, elimine el ```deinit()``` fuera del bucle. Ahora el ```archivo.write()``` funciona correctamente.

* * *
Errores que conozco:

* Si escribes un STRING en cualquier input va a dar error
* algunas funciones de Trigonometria si les pones un numero que no corresponde te lanzara un error pero no una excepcion
  por lo que sigue funcionando el codigo
* todas las funciones de la config estan o rotas o no funcionan del todo bien
* Los nombres de las variables son algo confusas
  

* * *
