#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
# print("hello world")

import random

def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    puntaje = {'jugador': 0, 'oponente': 0}

    while True:
        print("\nOpciones: piedra, papel, tijeras")
        eleccion_jugador = input("Elige tu opción: ").lower()

        if eleccion_jugador not in opciones:
            print("Opción no válida. Por favor, elige entre piedra, papel o tijeras.")
            continue

        eleccion_oponente = random.choice(opciones)
        print(f"\nTu elección: {eleccion_jugador}")
        print(f"Elección del oponente: {eleccion_oponente}")

        resultado = determinar_ganador(eleccion_jugador, eleccion_oponente)

        if resultado == 'empate':
            print("¡Empate!")
        elif resultado == 'ganador':
            print("¡Ganaste esta ronda!")
            puntaje['jugador'] += 1
        else:
            print("¡Perdiste esta ronda!")
            puntaje['oponente'] += 1

        print(f"Puntaje actual - Jugador: {puntaje['jugador']}, Oponente: {puntaje['oponente']}")
        
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print("¡Gracias por jugar!")

def determinar_ganador(eleccion_jugador, eleccion_oponente):
    reglas = {'piedra': 'tijeras', 'tijeras': 'papel', 'papel': 'piedra'}

    if eleccion_jugador == eleccion_oponente:
        return 'empate'
    elif reglas[eleccion_jugador] == eleccion_oponente:
        return 'ganador'
    else:
        return 'perdedor'

# Iniciar el juego
jugar()
