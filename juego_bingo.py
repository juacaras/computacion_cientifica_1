from bombo import Bombo
from jugador import Jugador
import time 
import tkinter 

class JuegoBingo:
    def __init__(self, nombres_jugadores):
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.bombo = Bombo()
        self.ganador = None

    def iniciar_juego(self):
        print("¡Bienvenido al juego de Bingo!\n")

        # Mostrar cartones antes de comenzar el sorteo
        print("🎴 Estos son los cartones de los jugadores:\n")
        self.mostrar_estado()
        print("Espere 2 segundos para el siguiente turno")
        time.sleep(2)
        
        

        while not self.ganador:
            numero = self.bombo.sortear_numero()
            if numero is None:
                print("No quedan más números. Fin del juego.")
                break

            print(f"\n🎱 Número sorteado: {numero}")
            for jugador in self.jugadores:
                jugador.marcar_numero(numero)
                if jugador.ha_ganado():
                    self.ganador = jugador
                
                    break

            self.mostrar_estado()

            if not self.ganador:
                print("Espere 2 segundos para el siguiente turno")
                time.sleep(2)

        print(f"\n🎉 ¡{self.ganador.nombre} ha ganado el juego!")


    def mostrar_estado(self):
        for jugador in self.jugadores:
            print(f"\nCartón de {jugador.nombre}:")
            jugador.carton.mostrar()
            
        
        
