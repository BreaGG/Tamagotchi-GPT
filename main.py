import time
import threading
import keyboard
import os

class Tamagotchi:
    def __init__(self):
        self.hambre = 0
        self.aburrimiento = 0
        self.sueño = 0
        self.higiene = 0
        self.animacion_actual = 0
        self.animaciones = [
            """
             .-^-.
            /_/_\\_\\
             |/o o\\|
             |\\_-_/|
            /|     |\\
           | |     | |
           |_/     \\_|
          (___)   (___)
            """,
            """
             .-^-.
            /_/_\\_\\
             |/o o\\|
             |\\_^_/|
            /|     |\\
           | |     | |
           |_/     \\_|
          (___)   (___)
            """,
            """
             .-^-.
            /_/_\\_\\
             |/o o\\|
             |\\_-_/|
            /|     |\\
           | |     | |
           |_/     \\_|
          (___)   (___)
            """,
            """
             .-^-.
            /_/_\\_\\
             |/o o\\|
             |\\_-_/|
            /|     |\\
           | |     | |
           |_/     \\_|
          (___)   (___)
            """
        ]

    def incrementar_stats(self):
        self.hambre += 1
        self.aburrimiento += 0.5
        self.sueño += 0.25
        self.higiene += 0.1

    def mostrar_barras(self):
        print("Hambre:", self.mostrar_barra(self.hambre))
        print("Aburrimiento:", self.mostrar_barra(self.aburrimiento))
        print("Sueño:", self.mostrar_barra(self.sueño))
        print("Higiene:", self.mostrar_barra(self.higiene))

    def mostrar_barra(self, valor):
        barra = "[" + "#" * int(valor) + " " * (10 - int(valor)) + "]"
        return barra

    def verificar_estados(self):
        if self.hambre >= 10:
            print("¡Estoy hambriento! ¡Aliméntame!")
        if self.aburrimiento >= 10:
            print("¡Estoy aburrido! ¡Juguemos!")
        if self.sueño >= 10:
            print("¡Estoy cansado! ¡Necesito dormir!")
        if self.higiene >= 10:
            print("¡Necesito bañarme!")

    def mostrar_animacion(self):
        while True:
            limpiar_pantalla()
            print(self.animaciones[self.animacion_actual])
            self.mostrar_barras()
            self.verificar_estados()
            self.incrementar_stats()
            time.sleep(0.5)

    def atender_hambre(self):
        while self.hambre > 0:
            self.hambre -= 1
            self.animacion_actual = 2  # Animación de comer
            time.sleep(0.5)
        self.animacion_actual = 0

    def atender_aburrimiento(self):
        while self.aburrimiento > 0:
            self.aburrimiento -= 1
            self.animacion_actual = 1  # Animación de jugar
            time.sleep(0.5)
        self.animacion_actual = 0

    def atender_sueño(self):
        while self.sueño > 0:
            self.sueño -= 1
            self.animacion_actual = 3  # Animación de dormir
            time.sleep(0.5)
        self.animacion_actual = 0

    def atender_higiene(self):
        while self.higiene > 0:
            self.higiene -= 1
            time.sleep(0.5)

def limpiar_pantalla ():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    tamagotchi = Tamagotchi()

    threading.Thread(target=tamagotchi.mostrar_animacion, daemon=True).start()

    while True:
        if keyboard.is_pressed('h'):
            threading.Thread(target=tamagotchi.atender_hambre).start()
        elif keyboard.is_pressed('a'):
            threading.Thread(target=tamagotchi.atender_aburrimiento).start()
        elif keyboard.is_pressed('s'):
            threading.Thread(target=tamagotchi.atender_sueño).start()
        elif keyboard.is_pressed('g'):
            threading.Thread(target=tamagotchi.atender_higiene).start()

if __name__ == "__main__":
    main()
