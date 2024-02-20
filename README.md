# Simulación de una máquina de Turing que represente la sucesion de fibonacci.

## Contenido
- [Descripción](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#descripci%C3%B3n)
- [Objetivos](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#objetivos)
  - [General](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#general)
  - [Específicos](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#espec%C3%ADficos)
- [Convenciones utilizadas](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#convenciones-utilizadas)
  - [Archivo Yaml](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#archivo-yaml)
- [Temas vistos](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#temas-vistos)
- [Documento](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#documento)
- [Integrantes](https://github.com/FernandezDL/proyecto1-analisis_de_algoritmos?tab=readme-ov-file#integrantes)

## Descripción 
La [sucesión de Fibonacci](https://www.educ.ar/recursos/132013/la-matematica-incrustada-en-la-inmensa-variedad-de-formas-de-vida#:~:text=En%20matem%C3%A1tica%2C%20la%20sucesi%C3%B3n%20de,%2C%20610%2C%20987%2C%201597%E2%80%A6) se trata de una serie infinita de números naturales la cual continúa añadiendo números que son la suma de los dos anteriores. La realización de este proyecto tiene la finalidad de desarrollar un simulador de dicha sucesión mediante una [máquina de Turing](https://es.wikipedia.org/wiki/M%C3%A1quina_de_Turing), la cual en este caso es una máquina de tres cintas.

Dicha máquina obtendrá su _input_ mediante un archivo [yaml](https://www.redhat.com/es/topics/automation/what-is-yaml) el cual proporciona la descripción formal de la máquina y la cadena de entrada a simular, la cual se debe saber, al finalizar la ejecución de la máquina, si es aceptada o rechazada.

Esta máquina acepta una cadena formada por una sucesión de 1's, por lo que si se desea evaluar F7 la cadena a introducir en el archivo yaml es 1111111, donde la cantidad de 1's que se escriben corresponden al número de la sucesión que se desea comprobar. Por su parte, la entrada de las otras dos cintas son una sucesión de _blanks_ que se usan para que estas cintas no se queden completamente en 0.

Esta máquina tiene la particularidad de que siempre que se le provea un archivo yaml con sus descripciones instantáneas bien estructuradas puede aceptar cualquier máquina de Turing multicina debido a su generalización.
 
## Objetivos
### General
Comprender, de mejor manera, la notación O en el tiempo de ejecución de un algoritmo. 

### Específicos
 -Implementar de un parsing sobre la configuración de la máquina de Turing

 -Implementar de un parsing sobre la entrada en las cintas

 -Diseñar e implementar de la arquitectura a utilizar para las estructuras de datos que  alojarán las configuraciones de la máquina y permitirán una simulación utilizando las funciones de transición descritas

 -Implementar de la visualización de descripciones instantáneas en cada paso de la simulación

 -Implementar de la lógica para aceptar inputs en las cintas

 -Implementar el código para la captura del tiempo de ejecución de la máquina

## Convenciones utilizadas
### Archivo Yaml
* q_list: indica el listado de posibles estados en la máquina

* q_initial: indica el estado inicial de la máquina

* q_final: indica los estados finales de la máquina

* accept: indica los estados de aceptación de la máquina

* alphabet: indica el alfabeto que acepta la máquina

* tape_alphabet: indica el alfabeto de la cinta

* blank: indica el caracter utilizado para representar los blanks

* delta: indica el inicio del set de transiciones.

* params: parámetros de la configuración para la cuál se aplicaría la transición en cuestión, de manera que está compuesto por el estado inicial y un array de la configuración en cada una de las cintas.

* output: indica el output o el retorno de la función de transición, está compuesto por:
  * final_state: estado final al que llega
  * output: array que indica cómo queda la configuración de las cintas luego de aplicar el estado de transición
  * tape_displacement: array  que indica cómo es que se movería cada cabeza en dicha función de transición, donde "R" es derecha, "L" es izquierda y "S" es _stay_, lo que significa que se mantiene en el mismo punto en la cinta

* Simulation_strings: valores que ingresarían en cada una de las cintas, de manera que cada cinta tiene su propia cadena de entrada. Se debe de denotar que para esta máquina, la sucesión de 1's en la primera cinta significa el valor _n_ a evaluar en la sucesión de Fibonacci.
  
## Temas vistos
- Máquinas de Turing
- Transiciones de una máquina de Turing
- Notación asintótica O
- Sucesión de Fibonacci

## Documento
Dentro del [documento](https://docs.google.com/document/d/1W6obe05NTC72kWp2WSZXfGYj9MBrQgc-08Cyx9WeQVo/edit?usp=sharing) se encuentra desarrollado el _punto 5: análisis empírico_ del proyecto

## Integrantes
-Diana Lucía Fernández Villatoro - 21747

-Diego Andres Alonzo Medinilla  - 20172
