class Pasajero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Vuelo:
    def __init__(self, numero, origen, destino, fecha, hora):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.asientos_disponibles = 100
        self.lista_pasajeros = []

    def reservar_asiento(self, pasajero):
        if self.asientos_disponibles > 0:
            self.lista_pasajeros.append(pasajero)
            self.asientos_disponibles -= 1
            print(f"Reserva exitosa. Asiento reservado para {pasajero.nombre}.")
        else:
            print("Lo siento, no quedan asientos disponibles en este vuelo.")

    def mostrar_pasajeros(self):
        print("Lista de pasajeros:")
        for pasajero in self.lista_pasajeros:
            print(pasajero.nombre)

# Crear objetos y realizar interacciones
pasajero1 = Pasajero("Juan", 30)
pasajero2 = Pasajero("María", 25)

vuelo1 = Vuelo("V001", "Ciudad A", "Ciudad B", "2024-06-25", "10:00")
vuelo2 = Vuelo("V002", "Ciudad B", "Ciudad C", "2024-06-26", "14:00")

vuelo1.reservar_asiento(pasajero1)
vuelo1.reservar_asiento(pasajero2)

vuelo2.reservar_asiento(pasajero1)

vuelo1.mostrar_pasajeros()
vuelo2.mostrar_pasajeros()
