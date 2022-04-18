
import random
import numpy as np
import time
import funciones_barcos as fb

# los barcos colocados en el tablero se identificaran con: "#"
# los disparos al agua se identificaran con: "0"
# los disparos tocados se identificaran con: "!"

# Primero damos la bienvenida al jugador y preguntamos su nombre

jugador = input("Bienvenido a Hundir la Flota Jugador. Escribe tu nombre: \n")
print("\n")
print("Aqui comienza tu aventura", jugador, "\n")

#con estas dos funciones inicializamos los tableros
tablero_jugador, tablero_maquina_blanco = fb.creacion_tableros()
tablero_maquina, tablero_jugador_blanco = fb.creacion_tableros()

#como su nombre indica esta funicon nos imprime el tablero del jugador por pantalla
fb.pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)

#inicializamos los contadores de tocados del jugador y de la maquina
tocado_jugador = 0
tocado_maquina = 0

#este bucle es el core el juego mientras que ninguno de los jugadores haya tocado 20 veces el juego seguira en marcha,
#una vez uno de ellos llegue a 20, el numero de tocados maximo segun los barcos que tenemos, el juego parara
while tocado_maquina<20 and tocado_jugador<20:
    
    
    tocado_jugador = fb.disparo_jugador(jugador, tablero_jugador, tablero_maquina, tablero_maquina_blanco, tocado_jugador)
    
    tocado_maquina = fb.disparo_maquina(jugador, tablero_jugador, tablero_jugador_blanco, tablero_maquina_blanco, tocado_maquina)
    
    
    
# una vez el juego pare segun quien sea el ganador tendremos un mensaje 
if tocado_maquina == 20:
    print("¡Has perdido!", jugador)

elif tocado_jugador == 20:
    print(f"¡Has ganado, enhorabuena {jugador} !")

print("GAME OVER!!")