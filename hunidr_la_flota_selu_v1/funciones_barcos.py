#en este script los barcos se colocan aleatoriamente
#se quedan pegados unos a otros se puede implementar para que alrededor del barco sea agua y no esten mas de un barco junto 



import numpy as np
import random
import time

def creacion_tableros():

    '''
    en esta funcion inicializamos los tableros de cada jugador, uno con los barcos y otro en blanco donde se veran
    los disparos realizados al oponente. 

    '''

    tablero_jugador = np.full((10,10), " ")
    tablero_blanco = np.full((10,10), " ")


    barcos_list= [["11"],["11"],["11"],["11"],
                ["12","22"],["12","22"],["12","22"],
                ["13","23","33"],["13","23","33"],
                ["14","24","34","44"]]

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



def pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco):
    '''
    esta funcion nos muestra por pantalla el tablero del jugador y el tablero de la maquina en blanco con los disparos 
    realizados por el jugador
    '''

    print("Tablero de", jugador)
    print(tablero_jugador)
    print("\n")
    time.sleep(1)
    print("Tablero Maquina")
    print(tablero_maquina_blanco)
    time.sleep(1)
    
    return 



def disparo_jugador(jugador, tablero_jugador, tablero_maquina, tablero_maquina_blanco, tocado_jugador):
    '''
    esta funcion nos pide introducir las coordenadas de disparo, primero comprobamos si los valores introducidos son 
    enteros y si estan entre 0 y 9 si es asi pasamos a comprobar si el disparo ha dado en agua o ha sido tocado, si
    los valores introducidos no son correctos nos pedira que los introduzcamos de nuevo
    '''

    while tocado_jugador<20:

        print("\n")
        print(f"Es tu turno {jugador} \n")
        cord_x_jugador = input("Introduce tu coordenada x, \n (numero de fila de 0 a 9): \n")
        cord_y_jugador = input("Introduce tu coordenada y, \n (numero de columna de 0 a 9): \n")
        
        while True:
                    
            while True:
                try:
                    cord_x_jugador = int(cord_x_jugador)
                    cord_y_jugador = int(cord_y_jugador)
                    break
                        
                                
                except:
                    cord_x_jugador = input("Coordenada incorrecta,\nIntroduce tu coordenada x, \n (numero de fila de 0 a 9): \n")
                    cord_y_jugador = input("Coordenada incorrecta,\nIntroduce tu coordenada y, \n (numero de columna de 0 a 9): \n")
                    continue


            if 0 <= cord_x_jugador <=9 and 0 <= cord_y_jugador <=9:
                print("esta entre 0 y 9 ")
                break
            else:
                cord_x_jugador = input("Coordenada fuera del rango de 0 a 9,\nIntroduce tu coordenada x, \n (numero de fila de 0 a 9): \n")
                cord_y_jugador = input("Coordenada fuera del rango de 0 a 9,\nIntroduce tu coordenada y, \n (numero de columna de 0 a 9): \n")
                continue

        if tablero_maquina[cord_x_jugador,cord_y_jugador] == "#":
            print("¡Tocado!, Te toca otra vez")
            tablero_maquina[cord_x_jugador,cord_y_jugador] = "!"
            tablero_maquina_blanco[cord_x_jugador,cord_y_jugador] = "!"
            tocado_jugador = tocado_jugador + 1
            print("numero de tocados jugador",tocado_jugador)
            pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)
            continue
        
        elif tablero_maquina[cord_x_jugador,cord_y_jugador] == "!":
            print("¡Disparo repetido, tira de nuevo!")
            continue

        else:
            print("¡Agua!")
            tablero_maquina[cord_x_jugador,cord_y_jugador] = "0" 
            tablero_maquina_blanco[cord_x_jugador,cord_y_jugador] = "0"
            pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)
        break

    return tocado_jugador




    

def disparo_maquina(jugador, tablero_jugador, tablero_jugador_blanco, tablero_maquina_blanco, tocado_maquina):

    '''
    en el disparo de la maquina, genermos de forma aleatoria las coordenadas y como en la funcion anterior, 
    comprobamos si el disparo ha dado en agua o ha sido tocado
    '''


    while tocado_maquina<20:

        print(f"Es el turno de la Maquina \n")
        cord_x_maquina = random.randrange(10)
        print("Coordenada x de la Maquina: ",cord_x_maquina)
        cord_y_maquina = random.randrange(10)
        print("Coordenada y de la Maquina: ",cord_y_maquina)
        cord_x_maquina = int(cord_x_maquina)
        cord_y_maquina = int(cord_y_maquina)

        if tablero_jugador[cord_x_maquina,cord_y_maquina] == "#":
            print("¡Tocado!, Le toca otra vez a la Maquina")
            tablero_jugador[cord_x_maquina,cord_y_maquina] = "!"
            tablero_jugador_blanco[cord_x_maquina,cord_y_maquina] = "!"
            tocado_maquina = tocado_maquina + 1
            print("numero de tocados Maquina",tocado_maquina)
            pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)
            continue
        
        elif tablero_jugador[cord_x_maquina,cord_y_maquina] == "!" :
            print("¡Disparo repetido, La Maquina tira de nuevo!")
            continue

        else:
            print("¡Agua!")
            tablero_jugador[cord_x_maquina,cord_y_maquina] = "0"
            tablero_jugador_blanco[cord_x_maquina,cord_y_maquina] = "0"
            pantalla_jugador(jugador, tablero_jugador, tablero_maquina_blanco)
            break

    return tocado_maquina