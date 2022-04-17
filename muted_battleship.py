import numpy as np
import random
import time


# Contadores de disparos acertados y fallidos
strike_player = 0
strike_machine = 0
failed_player = 0
failed_machine = 0

# Contadores de turnos
turn_player = 1
turn_machine = 1


def creacion_tableros():

    '''
    en esta funcion inicializamos los tableros de cada jugador, uno con los barcos y otro en blanco donde se veran
    los disparos realizados al oponente. 

    '''

    tablero_jugador = np.full((10,10), " ")
    tablero_blanco = np.full((10,10), " ")


    barcos_list= [["#"],["#"],["#"],["#"],
                ["#","#"],["#","#"],["#","#"],
                ["#","#","#"],["#","#","#"],
                ["#","#","#","#"]]

    for barco in barcos_list:
        #las orientaciones serán : Norte = 0, Sur = 1, Este = 2, Oeste = 3
        orientacion = random.randrange(4) 
        
        while True: 

            cord_x = random.randrange(10)
            # print("coordenada x ",cord_x)
            cord_y = random.randrange(10)
            # print("coordenada y ",cord_y)
            # print("Punto en el mapa",tablero_juego[cord_x,cord_y])
            # print("\n")
            '''
            para la colocacion de los barcos comprobamos que el barco quepa dentro de los limites del tablero,
            y comprobamos que dentro del "slice" de la matriz donde ira el barco todo el agua, si es asi se sustituiran
            los espacios por # que representa un punto del barco
            '''

            if orientacion == 0:
                situacion_barco = np.all(tablero_jugador[cord_x:cord_x+len(barco),cord_y:cord_y+1] == " ")
                if situacion_barco & (cord_x + len(barco)-1 <= 9):
                    tablero_jugador[cord_x:cord_x+len(barco),cord_y:cord_y+1] = "#"
                    # print("norte",situacion_barco)
                else:
                    continue
            elif orientacion == 1:
                situacion_barco = np.all(tablero_jugador[cord_x-len(barco)+1:cord_x+1,cord_y:cord_y+1] == " ")
                if situacion_barco & (cord_x - len(barco)-1 >= 0):
                    tablero_jugador[cord_x-len(barco)+1:cord_x+1,cord_y:cord_y+1] = "#"
                    # print("sur",situacion_barco)
                else:
                    continue
            elif orientacion == 2:
                situacion_barco = np.all(tablero_jugador[cord_x:cord_x+1,cord_y:cord_y+len(barco)] == " ")
                if situacion_barco & (cord_y + len(barco)-1 <= 9):
                    tablero_jugador[cord_x:cord_x+1,cord_y:cord_y+len(barco)] = "#"
                    # print("este",situacion_barco)
                else:
                    continue
            elif orientacion == 3:
                situacion_barco = np.all(tablero_jugador[cord_x:cord_x+1,cord_y-len(barco)+1:cord_y+1] == " ")
                if situacion_barco & (cord_y - len(barco)-1 >= 0):
                    tablero_jugador[cord_x:cord_x+1,cord_y-len(barco)+1:cord_y+1] = "#"
                    # print("oeste",situacion_barco)
                else:
                    continue
            
            break

    return tablero_jugador, tablero_blanco


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
    good_strike = (ocean1[x, y] == '#') or (ocean1[x, y] == '#') or (ocean1[x, y] == '#') or (ocean1[x, y] == '#')
    
    # Condición de disparo NO acertado en el tablero de Player
    fail_strike = (ocean1[x, y] == ' ') or (ocean1[x, y] == 'Ξ')

    # Condición de disparo repetido en el tablero de Player
    re_strike = (ocean1[x, y] == 'Ø')
    
    # Si se cumple la condición de disparo acertado...
    if good_strike:
        turn_machine += 1
        strike_machine += 1
        ocean1[x, y] = 'Ø'
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
    good_strike = (ocean2[x, y] == '#') or (ocean2[x, y] == '#') or (ocean2[x, y] == '#') or (ocean2[x, y] == '#')
    
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
ocean1, ocean3 = creacion_tableros()
# Tablero para los barcos de la máquina            
ocean2, ocean4 = creacion_tableros()


# Mostrando tableros iniciales del jugador y la máquina
print_oceans()

# Iniciando el primer turno de la batalla solicitando coordenadas al jugador
disparo_player()
