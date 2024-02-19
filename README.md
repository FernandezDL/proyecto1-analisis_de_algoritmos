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
### Convenciones utilizadas
#### Archivo Yaml
* q_list indica el listado de posibles estados en la máquina.

* q_initial indica el estado inicial

* q_final indica los estados finales

* accept indica los estados de aceptacion

* alphabet indica el alfabeto

* tape_alphabet indica el alfabeto de la cinta

* blank indica el caracter utilizado para representar los blanks.

* delta indica el inicio del set de transiciones.

* params son los parámetros de la configuración para la cuál se aplicaría la transición en cuestión, de manera que está compuesto por el estado inicial y un array de la configuración en cada una de las cintas.

* output, indica el output o el retorno de la función de transición, está compuesto por: final_state que es el estado final al que llega, el output de las cintas que es un array que indica cómo queda la configuración de las cintas luego de aplicar el estado de transición y el tape_displacement que que es un array indica cómo es que se movería cada cabeza en dicha función de transición; R es derecha, L es izquierda y S es stay que significaría que se mantiene en el mismo punto en la cinta.

* Simulation_strings son los valores que ingresarían en cada una de las cintas, de manera que cada cinta tiene su propia cadena de entrada. Se debe de denotar que para esta máquina de turing de la simulación de Fibonacci, la sucesión de unos en la primera cinta significa el valor n a evaluar en la sucesión de Fibonacci.
 
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
