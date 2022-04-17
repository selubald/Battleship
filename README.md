
# Juego Hundir la Flota (Battleship) 10x10
![Logo](https://www.myfxdata.io/img/markdown/battleship.png)

## Introducción
En este ejercicio vas a crear tu propio juego de **Hundir la flota** en Python. Para el desarrollo del programa necesitarás conocimientos de la librería `numpy`, módulos, bucles, funciones y colecciones de Python. Se recomienda desarrollar el programa en un IDE como Pycharm, Visual Studio Code o Spyder. **Por lo que la entrega deberá constar de uno o varios scripts de Python (archivos .py), los que necesite el alumno**.

## ¿Cómo funciona el juego?
Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: tu y la maquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tu, como la maquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tu.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la maquina.
7. En los turnos de la maquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
9. Por norma del juego no puede haber espacios entre barcos. Ignora esta norma

## Authors

- **Ouissam** [ouissam@outlook.com](mailto:ouissam@outlook.com)
- **Selu** [jotoan93@gmail.com](mailto:jotoan93@gmail.com)
- **Lola** [eauturquesa@hotmail.com](mailto:eauturquesa@hotmail.com)


## Features

Esta entrega del juego viene en 2 versiones:
- **muted_battleship:** Version sin sonido en la que todos los barcos del jugador se representan sobre el tablero con el mismo signo **#**
- **sonor_battleship:** Version con sonido usando el módulo *Pygame* para crear 2 funciones que permiten reproducir un archivo .WAV después de disparar según si es acertado o fallido (a barco o al agua)
## Tech Stack

- Visual Code 1.66.2 for Windows
- Python 3.7.4
- Biblioteca NumPy
- Módulo Pygame 2.1.2 *(pip install pygame)*
- Notepad++ 




## Screenshots

![muted_b](https://www.myfxdata.io/img/markdown/muted_b.png)

![sonor_b](https://www.myfxdata.io/img/markdown/sonor_b.png)

![sonor_c](https://www.myfxdata.io/img/markdown/sonor_c.png)
