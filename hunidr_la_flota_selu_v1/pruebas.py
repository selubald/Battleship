from winreg import SetValue
import funciones_barcos as fb


# import numpy as np
# import random
# import time

jugador = input("Bienvenido a Hundir la Flota Jugador. Escribe tu nombre: \n")
print("\n")
print("Aqui comienza tu aventura", jugador, "\n")

tablero_jugador, tablero_maquina_blanco = fb.creacion_tableros()


fb.pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)








































# tablero_jugador_list = np.arange(100)
# tablero_jugador = tablero_jugador_list.reshape((10,10))

# print(tablero_jugador)
# print("\n")

# barco = ["14","24","34","44"]

    
# cord_x = 5
# print("coordenada x" ,cord_x)
# cord_y = 5
# print("coordenada y" ,cord_y)
# print("Punto en el mapa",tablero_jugador[cord_x,cord_y])
# print("\n")

# #barco norte
# print(tablero_jugador[cord_x-1:cord_x+len(barco)+2,cord_y-1:cord_y+2])


# # para barco hacia el sur, situacion barco:
# print(tablero_jugador[cord_x-len(barco)+1:cord_x+1,cord_y:cord_y+1])
# print(tablero_jugador[cord_x-len(barco):cord_x+2,cord_y-1:cord_y+2])

# # #para un barco hacia el este
# print(tablero_jugador[cord_x:cord_x+1,cord_y:cord_y+len(barco)])
# print(tablero_jugador[cord_x-1:cord_x+2,cord_y-1:cord_y+len(barco)+2])

# # #para un barco hacia el oeste
# print(tablero_jugador[cord_x:cord_x+1,cord_y-len(barco)+1:cord_y+1])
# print(tablero_jugador[cord_x-1:cord_x+2,cord_y-len(barco):cord_y+2])


