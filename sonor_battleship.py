import numpy as np
import random
import time
import os
# Esconder el prompt informativo que muestra pygame al ejecutar el programa
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "HIDE"

# Módulo pygame necesario para reproducir sonidos .wav durante el juego
# Se instala ejecutando el comando: pip install pygame
import pygame


pygame.init()
pygame.mixer.init()

# Sonidos de disparos acertados y fallidos
good_strike_sound = pygame.mixer.Sound("good_strike.wav")
fail_strike_sound = pygame.mixer.Sound("fail_strike.wav")

# Contadores de disparos acertados y fallidos
strike_player = 0
strike_machine = 0
failed_player = 0
failed_machine = 0

# Contadores de turnos
turn_player = 1
turn_machine = 1


# Función para reproducir sonido de disparo acertado
def play_good_strike():
    pygame.mixer.Sound.play(good_strike_sound)

# Función para reproducir sonido de disparo fallido
def play_fail_strike():
    pygame.mixer.Sound.play(fail_strike_sound)


# Función para posicionar los barcos en el tablero del jugador
def barcos_player(letra,eslora):

    while True:

        # Generando posición inicial de cada barco
        init_pos = np.random.randint(10, size = 2)
        x = init_pos[0]
        y = init_pos[1]

        # Generando orientación aleatoria: Norte, Sur, Este, Oeste
        orient = random.choice(['N', 'S', 'E', 'O'])

        # Reservando posiciones según eslora y orientación
        if orient == 'N':
            posiciones = ocean1[x:x - eslora:-1, y]
        elif orient == 'S':
            posiciones = ocean1[x:x + eslora, y]
        elif orient == 'E':
            posiciones = ocean1[x, y:y + eslora]
        elif orient == 'O':
            posiciones = ocean1[x, y:y - eslora:-1]
        
        # Condición de posición libre en el tablero
        free_pos = ('A' not in posiciones) and ('B' not in posiciones) and ('C' not in posiciones) and ('D' not in posiciones)
    
        # Comprobando si las posiciones están libres y no se salen del tablero
        
        # Orient. == Norte
        if orient == 'N' and 0 <= x - eslora < 10 and free_pos:
            ocean1[x:x - eslora:-1, y] = letra
            break

        # Orient. == Sur
        elif orient == 'S' and 0 <= x + eslora < 10 and free_pos:
            ocean1[x:x + eslora, y] = letra
            break

        # Orient. == Este
        elif orient == 'E' and 0 <= y + eslora < 10 and free_pos:
            ocean1[x, y:y + eslora] = letra
            break

        # Orient. == Oeste
        elif orient == 'O' and 0 <= y - eslora < 10 and free_pos:
            ocean1[x, y:y - eslora:-1] = letra
            break

        # Probando de nuevo si el barco se sale del tablero o alguna de sus posiciones está ocupada
        else:
            continue


# Función para posicionar los barcos en el tablero de la máquina
def barcos_machine(letra,eslora):

    while True:

        # Generando posición inicial de cada barco
        init_pos = np.random.randint(10, size = 2)
        x = init_pos[0]
        y = init_pos[1]

        # Generando orientación aleatoria: Norte, Sur, Este, Oeste
        orient = random.choice(['N', 'S', 'E', 'O'])

        # Reservando posiciones según eslora y orientación
        if orient == 'N':
            posiciones = ocean2[x:x - eslora:-1, y]
        elif orient == 'S':
            posiciones = ocean2[x:x + eslora, y]
        elif orient == 'E':
            posiciones = ocean2[x, y:y + eslora]
        elif orient == 'O':
            posiciones = ocean2[x, y:y - eslora:-1]
        
        # Condición de posición libre en el tablero
        free_pos = ('A' not in posiciones) and ('B' not in posiciones) and ('C' not in posiciones) and ('D' not in posiciones)
    
        # Comprobando si las posiciones están libres y no se salen del tablero
        
        # Orient. == Norte
        if orient == 'N' and 0 <= x - eslora < 10 and free_pos:
            ocean2[x:x - eslora:-1, y] = letra
            break

        # Orient. == Sur
        elif orient == 'S' and 0 <= x + eslora < 10 and free_pos:
            ocean2[x:x + eslora, y] = letra
            break

        # Orient. == Este
        elif orient == 'E' and 0 <= y + eslora < 10 and free_pos:
            ocean2[x, y:y + eslora] = letra
            break

        # Orient. == Oeste
        elif orient == 'O' and 0 <= y - eslora < 10 and free_pos:
            ocean2[x, y:y - eslora:-1] = letra
            break

        # Probando de nuevo si el barco se sale del tablero o alguna de sus posiciones está ocupada
        else:
            continue


# Función para imprimir por pantalla los tableros del jugador y la máquina
def print_oceans():
    print(f"\n{player} Ocean:")
    print("-------------------------------------------")
    print(ocean1)

    print(f"\n{machine} Ocean:")
    print("-------------------------------------------")
    print(ocean3)

# Función para comprobar que la fila tecleada por el jugador está dentro del rango del tablero
def x_en_rango(x):
    return 1 <= x <= 10

# Función para comprobar que la columna tecleada por el jugador está dentro del rango del tablero
def y_en_rango(y):
    return 1 <= y <= 10


# Función para buscar el disparo de la máquina en el tablero del jugador
def buscar_player(x, y):
    global strike_machine
    global failed_machine
    global turn_machine

    # Condición de disparo acertado en el tablero de Player
    good_strike = (ocean1[x, y] == 'A') or (ocean1[x, y] == 'B') or (ocean1[x, y] == 'C') or (ocean1[x, y] == 'D')
    
    # Condición de disparo NO acertado en el tablero de Player
    fail_strike = (ocean1[x, y] == ' ') or (ocean1[x, y] == 'Ξ')

    # Condición de disparo repetido en el tablero de Player
    re_strike = (ocean1[x, y] == 'Ø')
    
    # Si se cumple la condición de disparo acertado...
    if good_strike:
        turn_machine += 1
        strike_machine += 1
        ocean1[x, y] = 'Ø'
        play_good_strike()
        time.sleep(1)
        print(f"\n¡BOOM! {machine} ha alcanzado un barco de {player}.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_machine}\nDisparos fallidos (al agua): {failed_machine}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_machine()

    # Si se cumple la condición de disparo NO acertado...
    elif fail_strike:
        turn_machine += 1    
        failed_machine += 1
        ocean1[x, y] = 'Ξ'
        play_fail_strike()
        time.sleep(1)
        print(f"\n¡FAIL! {machine} ha disparado al agua.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_machine}\nDisparos fallidos (al agua): {failed_machine}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_player()  

    # Si se cumple la condición de disparo repetido...
    elif re_strike:
        turn_machine += 1 
        time.sleep(1)
        print(f"\n¡ALERT! {machine} ha vuelto a disparar a una posición acertada anteriormente.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_machine}\nDisparos fallidos (al agua): {failed_machine}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_player()          
    
    
# Función para buscar el disparo del jugador en el tablero de la máquina
def buscar_machine(x, y):
    global strike_player
    global failed_player
    global turn_player

    # Condición de disparo acertado en el tablero de Machine
    good_strike = (ocean2[x, y] == 'A') or (ocean2[x, y] == 'B') or (ocean2[x, y] == 'C') or (ocean2[x, y] == 'D')
    
    # Condición de disparo NO acertado en el tablero de Machine
    fail_strike = (ocean2[x, y] == ' ') or (ocean2[x, y] == 'Ξ')

    # Condición de disparo repetido en el tablero de Machine
    re_strike = (ocean2[x, y] == 'Ø')
    
    # Si se cumple la condición de disparo acertado...
    if good_strike:
        turn_player += 1
        strike_player += 1
        ocean2[x, y] = 'Ø'
        ocean3[x, y] = 'Ø'
        time.sleep(1)
        play_good_strike()
        time.sleep(1)
        print(f"\n¡BOOM! {player} ha alcanzado un barco de {machine}.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_player}\nDisparos fallidos (al agua): {failed_player}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_player()

    # Si se cumple la condición de disparo NO acertado...
    elif fail_strike:
        turn_player += 1
        failed_player += 1
        ocean2[x, y] = 'Ξ'
        ocean3[x, y] = 'Ξ'
        time.sleep(1)
        play_fail_strike()
        time.sleep(1)
        print(f"\n¡FAIL! {player} ha disparado al agua.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_player}\nDisparos fallidos (al agua): {failed_player}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_machine()    

    # Si se cumple la condición de disparo repetido...
    elif re_strike:
        turn_player += 1
        time.sleep(1)
        print(f"\n¡ALERT! {player} ha vuelto a disparar a una posición acertada anteriormente.")
        time.sleep(1)
        print(f"Disparos acertados (a barcos): {strike_player}\nDisparos fallidos (al agua): {failed_player}\n")
        time.sleep(1)
        print_oceans()
        time.sleep(2)
        disparo_machine()      


# Función para solicitar el disparo del jugador        
def disparo_player():
    global strike_player
    global turn_player
    
    if strike_player < 20:
        time.sleep(2)    
        print(f"\nTurno #{turn_player} de {player}: Solicitando coordenadas de disparo...")

        x = None
        y = None

        # Solicitando y comprobando la fila
        while True:
            try:
                x = int(input("Ingresa el número de la fila: "))
                if x_en_rango(x):
                    x = x-1  # El índice de la posición (fila) deseada equivale al valor tecleado -1
                    break
                else:
                    print("Fila NO válida!! Ingresa un número entre 1 y 10")
            except:
                print("Ingresa un número de fila entre 1 y 10")

        # Solicitando y comprobando la columna
        while True:
            try:
                y = int(input("Ingresa el número de la columna: "))
                if y_en_rango(y):
                    y = y-1  # El índice de la posición (columna) deseada equivale al valor tecleado -1
                    break
                else:
                    print("Columna NO válida!! Ingresa un número entre 1 y 10")
            except:
                print("Ingresa un número de columna entre 1 y 10")    

        buscar_machine(x, y)
    
    else:
        print(f"\n{player} ha hundido toda la flota de {machine}.\n\n")
        for letra in 'MISSION COMPLETE!!':
            time.sleep(1)
            print(letra)
        time.sleep(3)


# Función para generar el disparo de la máquina    
def disparo_machine():
    global strike_machine
    global turn_machine

    if strike_machine < 20:
        time.sleep(2)        
        print(f"\nTurno #{turn_machine} de {machine}: Generando coordenadas de disparo...")

        # disparo = np.random.randint(10, size = 2)
        # x = disparo[0]
        # y = disparo[1]
    
        x = random.randint(0,9)
        y = random.randint(0,9)

        buscar_player(x, y)
        
    else:
        print(f"\n{machine} ha hundido toda la flota de {player}.\n\n")
        for letra in 'GAME OVER!!':
            time.sleep(1)
            print(letra)
        time.sleep(3)


print(",--.  ,--.                      ,--. ,--.             ,--.              ,------. ,--.           ,--.                 ,--.   ,--.               ,--.   ,--.    ")
print("|  '--'  | ,--.,--. ,--,--,   ,-|  | `--' ,--.--.     |  |  ,--,--.     |  .---' |  |  ,---.  ,-'  '-.  ,--,--.     /   |  /    \  ,--.  ,--. /   |  /    \   ")
print("|  .--.  | |  ||  | |      \ ' .-. | ,--. |  .--'     |  | ' ,-.  |     |  `--,  |  | | .-. | '-.  .-' ' ,-.  |     `|  | |  ()  |  \  `'  /  `|  | |  ()  |  ")
print("|  |  |  | '  ''  ' |  ||  | \ `-' | |  | |  |        |  | \ '-'  |     |  |`    |  | ' '-' '   |  |   \ '-'  |      |  |  \    /   /  /.  \   |  |  \    /   ")
print("`--'  `--'  `----'  `--''--'  `---'  `--' `--'        `--'  `--`--'     `--'     `--'  `---'    `--'    `--`--'      `--'   `--'   '--'  '--'  `--'   `--'    ")
print(" ____  ____  _________  ____  ____  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  _________  ____  _________  ____  ____  ____  ____ ")
print("||b ||||y ||||       ||||L ||||O ||||L ||||A ||||, ||||       ||||O ||||U ||||I ||||S ||||S ||||A ||||M ||||       ||||& ||||       ||||S ||||E ||||L ||||U ||")
print("||__||||__||||_______||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||_______||||__||||_______||||__||||__||||__||||__||")
print("|/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/_______\||/__\||/__\||/__\||/__\|")

# Los barcos de eslora = 1 se representan con: 'A'
# Los barcos de eslora = 2 se representan con: 'B'
# Los barcos de eslora = 3 se representan con: 'C'
# Los barcos de eslora = 4 se representan con: 'D'
# Los disparos acertados (a barcos) se representan con: 'Ø'
# Los disparos NO acertados (al agua) se representan con: 'Ξ'


print("\n\nBienvenido a Hundir la Flota 10x10")
time.sleep(0.5) 
nombre = input("Escribe tu nombre: ")
player = nombre.upper()
machine = "OMEN"
time.sleep(0.5) 
print("\nHola", player)
time.sleep(1.5) 
print("Aquí comienza tu batalla...")
time.sleep(1.5) 
print("Consiste en hundir todos los barcos de tu oponente a base de disparos a coordenadas solicitadas por teclado.")
time.sleep(1.5) 
print("\nTu oponente se llama", machine)
time.sleep(1.5) 
print("Juegas contra la máquina que intentará ganarte la batalla a base de disparos a coordenadas generadas aleatoriamente.")
time.sleep(1.5) 
print("\nStarting the Battle...")
time.sleep(3) 


# Creando los tableros del jugador y la máquina
# Tablero para los barcos del jugador            
ocean1 = np.full(fill_value = ' ', shape = (10, 10))
# Tablero para los barcos de la máquina            
ocean2 = np.full(fill_value = ' ', shape = (10, 10))
# Tablero para los disparos del jugador en los barcos (ocultos) de la máquina            
ocean3 = np.full(fill_value = ' ', shape = (10, 10))


# Posicionando barcos sobre los tableros del jugador y la máquina
# Los barcos de eslora = 1 se representan con la letra A
for i in range(4):
    barcos_player('A',1)
    barcos_machine('A',1)

# Los barcos de eslora = 2 se representan con la letra B
for j in range(3):
    barcos_player('B',2)
    barcos_machine('B',2)

# Los barcos de eslora = 3 se representan con la letra C
for k in range(2):
    barcos_player('C',3)
    barcos_machine('C',3)

# Los barcos de eslora = 4 se representan con la letra D
barcos_player('D',4)
barcos_machine('D',4)


# Mostrando tableros iniciales del jugador y la máquina
print_oceans()

# Iniciando el primer turno de la batalla solicitando coordenadas al jugador
disparo_player()
