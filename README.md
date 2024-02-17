# Simulación de una máquina de Turing que represente la sucesion de fibonacci.

## Contenido
- [Descripción](https://github.com/Wachuuu15/Simulacion-MT/tree/main#descripci%C3%B3n)
- [Objetivos](https://github.com/Wachuuu15/Simulacion-MT/tree/main#objetivos)
  - [General](https://github.com/Wachuuu15/Simulacion-MT/tree/main#general)
  - [Específicos](https://github.com/Wachuuu15/Simulacion-MT/tree/main#espec%C3%ADficos)
- [Temas vistos](https://github.com/Wachuuu15/Simulacion-MT/tree/main#temas-vistos)
- [Video](https://github.com/Wachuuu15/Simulacion-MT/tree/main#video)
- [Integrantes](https://github.com/Wachuuu15/Simulacion-MT/tree/main#integrantes)

## Descripción 
Teniendo como finalidad el desarrollar un simulador de la sucesion de Fibonacci mediante una Máquina de Turing, se debió realizar una máquina de turing multicinta de manera que se generalizo una máquina de turing de una cinta y se le pueden meter n cantidad de cintas. 
Así mismo, para realizar este proyecto se debe de desarrollar un archivo yaml en el cuál se introduzca la descripción formal de dicha máquina y este pueda simular una entrada que se le proporcione para saber si es una cadena aceptada o no.
En el caso de la máquina de turing de fibonacci el aproach que se dió fue que la primera entrada sería una sucesión de unos, indicando el n de la máquina, por ejemplo si se quiere conocer F7 entonces se ingresa 1111111, las demás entradas realmente es una sucesión de blanks para que no se quede en 0 las otras 2 cintas.
Sin embargo, la particularidad de esta máquina es que es generalizada por lo que puede aceptar cualquier máquina de turing multicinta, siempre y cuando se le provea de un archivo yaml con las descripciones instantáneas bien estructuradas.

## Objetivos
### General
Evaluar la comprensión del estudiante sobre la notación O en el tiempo de 
ejecución de un algoritmo. 

### Específicos
  -Implementación de un parsing sobre la configuración de la MT

 -Implementación de un parsing sobre la entrada en las cintas

 -Diseño e implementación de la arquitectura a utilizar para las estructuras de datos que  alojarán las configuraciones de su MT y permitirán una simulación utilizando las funciones de transición descritas

 -Implementación de la visualización de descripciones instantáneas en cada paso de la simulación

 -Implementación de la lógica para aceptar inputs en las cintas

## Temas vistos
- Máquinas de Turing
- Transiciones de una máquina de Turing
- Descripciones instantáneas
- Proceso reconocedor
- Proceso alterador

## Video 
[Link](https://youtu.be/McAQcS89Ocs)

## Integrantes
-Diana Lucía Fernández Villatoro - 21747

-Diego Andres Alonzo Medinilla  - 20172
