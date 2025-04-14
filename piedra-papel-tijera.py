"""
NOMBRE: Edwin Andrés Reyes Cóndor
Titulo del Proyecto: Juego Piedra, Papel o Tijera
Descripción: Este es un juego de piedra, papel o tijera que permite jugar contra la computadora. 
El jugador elige una opción y la computadora elige aleatoriamente entre piedra, papel o tijera. 
El resultado se determina según las reglas del juego.
El juego se repite hasta que el jugador decida salir. El programa también lleva un registro de las victorias, 
derrotas y empates del jugador.
"""

# ramdon.choice() es una función que elige un elemento aleatorio de una secuencia no vacía.
import random

# descripcion del juego
print("\t\t\t=====================================")
print("\t\t\t=== JUEGO: Piedra, papel o tijera ===")
print("\t\t\t=====================================")

print("\n-> OBJETIVO: El objetivo del juego es vencer a tu oponente en una serie de rondas. Cada ronda se decide \n" \
"mediante la selección simultánea de una de tres formas: piedra, papel o tijera.")
print("\n-> DESCRIPCION: es un juego clásico de manos jugado tradicionalmente entre dos personas.\n" \
"Cada jugador elige simultáneamente una de tres formas: piedra, papel o tijera. \n" \
"Se puede jugar a una sola ronda, pero mayormente se juega a 3 rondas.")
print("\n¡AVISO!\n" \
"En esta implementación particular, el usuario jugará contra la computadora, que realizará sus elecciones de forma aleatoria.")

# Inicio del juego
# Pedimos datos al usuario
print("\n*** BIENVENIDO AL JUEGO: Piedra, papel o tijera ***")
nombre_apellido = input("¿Cual es su nombre y apellido? ")
nick = input("Ingrese un nick: ")

# funcion para determinar una victoria, derrota o empate en cada ronda de juego
def play():
    # hacemos que la computadora elija una opcion al azar, usando la funcion random.choice()
    lista_opciones = ["piedra", "papel", "tijera"]
    play_computadora = random.choice(lista_opciones)

    # ahora el usuario debe elegir tambien una opcion
    play_usuario = input("\tpiedra, papel o tijera: ")

    # mostramos las elecciones 
    print(f"\n\t{nick}: {play_usuario}")
    print(f"\tComputadora: {play_computadora}")

    # comparamos ambas elecciones
    """
    REGLAS: 
    1. Piedra vence a Tijera (la aplasta o rompe) -> piedra > tijera 
    2. Papel vence a Piedra (la envuelve o cubre) -> papel > piedra  
    3. Tijera vence a Papel (la corta).")         -> tijera > papel 
    """
    # todos los casos donde el usuario pueda ganar
    if((f"{play_usuario} > {play_computadora}" == "piedra > tijera") or (f"{play_usuario} > {play_computadora}" == "papel > piedra") or (f"{play_usuario} > {play_computadora}" == "tijera > papel")):
        print(f"\t♥ Resultado: {nick} usted Gana! ♥")
        return "gana"
    # todos los casos donde el usuario pueda perder
    elif((f"{play_computadora} > {play_usuario}" == "piedra > tijera") or (f"{play_computadora} > {play_usuario}" == "papel > piedra") or (f"{play_computadora} > {play_usuario}" == "tijera > papel")):
        print(f"\t♣ Resultado: {nick} usted Pierde! ♣")
        return "pierde"
    # otro casos, seria un empate
    else:
        print("\t☻ Resultado: Empate! ☻")
        return "empate"

# defino una funcion menu de opciones para el usuario
def menu_opciones():
    print("\n ===============================================================================")
    print(f"|\t\t\tMENU DE OPCIONES DEL JUEGO\t\t\t\t|")
    print("|\t1. Comenzar juego\t\t\t\t\t\t\t|")
    print("|\t2. Visualizar registro de victorias, derrotas y/o empates del usuario   |")
    print("|\t3. Reglas del juego\t\t\t\t\t\t\t|")
    print("|\t4. Salir del juego\t\t\t\t\t\t\t|")
    print(" ===============================================================================\n")

# pedimos al usuario que elija una opcion del menu
print()     # salto de linea
menu_opciones() # mostrando el menu
op = int(input(nick + " elija una opcion: "))
print()

# variables para contabilizar el registro de victorias, derrotas y empates por cada juego.
victorias_user = 0
derrotas_user = 0
empates_user =  0

# variable para determinar cuantos juegos se van realizando actualmente
jugadas = 0

# como nose cuantas veces se va repetir las iteraciones, usaremos un bucle while
while(op):
    # lo haremos a 3 rondas en cada juego
    if(op == 1):
        # debemos reinicializar el registro cada vez que el usuario decida jugar, para evitar posibles errores 
        # en las condicionales
        victorias_user = 0
        derrotas_user = 0
        empates_user = 0

        # registramos el numero de veces que va jugando el usuario
        jugadas += 1

        # empezamos el juego, llamando a nuestra funcion play()
        print(f"\n\t\t\t*** PLAY {jugadas}° ***")
        # como sabemos que por cada juego, será 3 rondas, usaremos un bucle for
        for ronda in range(1, 4):  
            print(f"\t-> Ronda N° {ronda}")
            res_user = play()

            # luego de que la funcion play() hace su trabajo, usamos condicionales para ir actualizando nuestro registro
            if(res_user == "gana"):
                victorias_user += 1
            elif(res_user == "pierde"):
                derrotas_user += 1
            else:
                empates_user += 1
            print() # salto de linea
        
        # usamos condicionales para determinar el resultado final en cada juego
        if(victorias_user >= 2 or (victorias_user == 1 and empates_user == 2)):
            print(f"\t=> Resultado Final del Juego N°{jugadas}: {nick} gana")
        elif(derrotas_user >= 2 or (derrotas_user == 1 and empates_user == 2)):
            print(f"\t=> Resultado Final del Juego N°{jugadas}: La computadora gana")
        else:
            print(f"\t=> Resultado Final del Juego N°{jugadas}: EMPATE!")

        # despues de cada juego, volvemos a mostrarle al usuario el menu, para que él decida si desea seguir jugando o salir del juego.
        menu_opciones()
        op = int(input(nick + " elija una opcion: "))

    elif(op == 2):
        # Aqui solo mostramos el registro de victorias, derrotas y empates por cada juego.
        print(f"\nRegistro de cada Juego del Usuario {nick}")
        print(f"*** Registro en el Juego N°: {jugadas} ***")
        print(f"-> N° de Victorias Totales: {victorias_user}")
        print(f"-> N° de Derrotas Totales: {derrotas_user}")
        print(f"-> N° de Empates Totales: {empates_user}")
        
        # igualmente aqui, le mostramos el menu al usuario, para que determine lo que desea hacer
        menu_opciones()
        op = int(input(nick + " elija una opcion: "))

    elif(op == 3):
        # aqui solo mostramos las reglas del juego, por si el usuario desconoce de ellas.
        print("\t\t***** Reglas del Juego *****\t\t\n" \
        "\t-> 1. Piedra vence a Tijera (la aplasta o rompe).\n" \
        "\t-> 2. Papel vence a Piedra (la envuelve o cubre).\n" \
        "\t-> 3. Tijera vence a Papel (la corta).")

        # mostramos nuevamente el menu al usuario
        menu_opciones()
        op = int(input(nick + " elija una opcion: "))

    elif(op == 4):
        # opcion que nos permitirá salir del juego.
        print("Saliendo del juego...")
        break   # usamos un break para salir del bucle