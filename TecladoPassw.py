from machine import Pin
from time import sleep


TECLA_ARRIBA  = const(0)
TECLA_ABAJO = const(1)

teclas = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

# Pines del GPIO  
filas = [2,3,4,5]
columnas = [6,7,8,9]

# define los pines de filas como salidas
fila_pines = [Pin(nombre_pin, mode=Pin.OUT) for nombre_pin in filas]

# define los pines de columnas como entradas
columna_pines = [Pin(nombre_pin, mode=Pin.IN, pull=Pin.PULL_DOWN) for nombre_pin in columnas]

def init():
    for fila in range(0,4):
        for columna in range(0,4):
            fila_pines[fila].low()

def scan(fila, columna):
    """ escanea todo el teclado """

    # define la columna actual en alto -high-
    fila_pines[fila].high()
    tecla = None

    # verifica por teclas si hay teclas presionadas
    if columna_pines[columna].value() == TECLA_ABAJO:
        tecla = TECLA_ABAJO
    if columna_pines[columna].value() == TECLA_ARRIBA:
        tecla = TECLA_ARRIBA
    fila_pines[fila].low()

    # devuelve el estado de la tecla
    return tecla
password = "123456"
entrada = ""
print("Ingrese password")

# define todas las columnas bajo -low-
init()

while True:
    for fila in range(4):
        for columna in range(4):
            tecla = scan(fila, columna)
            if tecla == TECLA_ABAJO:
                print("Tecla presionada", teclas[fila][columna])
                sleep(0.5)
                ultima_tecla_presionada = teclas[fila][columna]
                entrada = entrada + ultima_tecla_presionada
                if len(entrada) == 6:
                    if entrada == password:
                        print("Password correcto")
                        entrada = ""
                    else:
                        print("Password incorrecto")
                        entrada = ""
