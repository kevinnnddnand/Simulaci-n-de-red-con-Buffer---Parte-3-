

import time
import random

class Nodo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []
        self.capacidad_buffer = 2

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")

        for nodo in self.conexiones:

            if random.random() < 0.2:
                print(f"¡Paquete perdido para {nodo.nombre}!")
                continue

            if len(nodo.buffer) >= nodo.capacidad_buffer:
                print(f"¡Buffer de {nodo.nombre} congestionado! Mensaje descartado")
                continue

            nodo.buffer.append(mensaje)
            print(f"{nodo.nombre}: mensaje agregado al buffer")

    def procesar_buffer(self):
        print(f"\nProcesando buffer de {self.nombre}...")

        while self.buffer:
            mensaje = self.buffer.pop(0)
            self.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibió: {mensaje}")


servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")


servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)


print("---- Comunicación inicial ----")
servidor.enviar_mensaje("Hola a todos!")

cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()


print("\n---- Desconexión del Cliente 2 ----")

servidor.eliminar_conexion(cliente2)
cliente2.eliminar_conexion(servidor)

print("Cliente 2 se ha desconectado")


time.sleep(3)

print("\nSimulando desconexión y reconexión dinámica...")


servidor.agregar_conexion(cliente2)
cliente2.agregar_conexion(servidor)

print("Cliente 2 se ha reconectado")


print("\n---- Simulación de congestión y pérdida de paquetes ----")

servidor.enviar_mensaje("Mensaje 1")
servidor.enviar_mensaje("Mensaje 2")
servidor.enviar_mensaje("Mensaje 3")


print("\n---- Procesamiento de buffers ----")

cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()


print("\n---- Fin de la simulación ----")
