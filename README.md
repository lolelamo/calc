 mi primer proyecto en vscode
 No es un proyecto serio, es mas para aprender por mi cuenta

#### --ES--
en que lo hice y porque lo hice:
Un proyecto, hecho en jupyter en el IDE VSCode, este proyecto fue para una tarea de la escuela
Se tenia que pedir a la IA un codigo con 8 defs, no se especifica que tipos de operaciones matematicas

 Explicacion basica del codigo (sin orden)
para ahorrar tiempo utilize la base del codigo proporcionado por la ia y hice la calculadora, agregue una forma de guardar los calculos 
con archivo = open("save.txt" + "w"), utilize una cadena de Elifs para las opciones del 1-9, 1-8 para las operaciones y el 9 para salir del codigo

 "print(colorama.Fore.RED + "funciona" + colorama.Fore.RESET)" es simplemente para saber si todo funciona bien, por si se quedo pegado o otra cosa
print("  ") es la forma mas basica de hacer saltos de linea, seguramente hay mejores formas de saltar lineas pero lo dejare asi por ahora

Para usar la calculadora se necesita y el porque se utilizan:

numpy (se utilizan raices cuadradas, ```sin()```, ```cos()```, ```tan()```, ```arcsin()```, ```arccos()```. ```arctan```() )  
python  
colorama (colores y para que sea vea mas bonito)  

### Cosas que quiero hacer:
1- arreglar errores y mejorar el codigo

2- agregas mas operaciones matematicas

3- cambiar de colorama A rich, no necesariamente quitar colorama

4- hacer tablas, poner barras de carga

5- finalmente, hacer mas bonito las tablas, y mas

#Cambios

t0.5: añadi sin, cos y tan y algunas mejoras para el codigo, como algunos "global" y configuracion (no esta completo y tiene errores
 
t0.6: cambie por completo el print del inicio para hacerlo algo mas ordenado, añadi arcsin, arccos y arctan, cambie varias cosas
quite por completo los "global", arregle algunos errores como el de si salias desde la terminal no se aplicaba el deinit() de colorama
elimine el deinit() afuera del bucle (ya que nunca se ejecutaria), cambie algunas cosas de la config (sigue estando incompleta)
ahora finalmente funciona el ```archivo.write```

