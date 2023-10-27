import random
from mysql import connector 
import time

conexion1 = connector.connect(
host = 'localhost', 
user='root',
password='',
database='juego'
)

'''Timer'''
'''def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = "{:02d}:{:02d}".format(m, s)
        print(min_sec_format, end="\n")
        time.sleep(1)
        num_of_secs -= 1

    print("Countdown finished.")


inp = int(input("Input number of seconds to countdown: "))
countdown(inp)'''

def jugadores():
    J1 = input("Ingrese nombre del Jugador 1: ")
    J2 = input("Ingrese nombre del Jugador 2: ")
    miCursor = conexion1.cursor()
    introducción = miCursor.execute(f"INSERT INTO jugadores")


def pregunta():
    preguntas = {"¿Que año fue la ultima vez que argentina no clasifico a un mundial?": "1970"}
    for x in range(5):
        pregunta = random.choice(preguntas)
        print(pregunta)
        resp = input("")
        for x in preguntas:
            if pregunta == x:
                if resp == preguntas[x]
                    print("respuesta correcta")
