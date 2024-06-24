class Cinema:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [[False] * seats_per_row for _ in range(rows)]  # False indica que el asiento está disponible

    def reserve_seat(self, row, seat_number):
        """ Reserva un asiento específico """
        if row < 1 or row > self.rows or seat_number < 1 or seat_number > self.seats_per_row:
            print("Número de fila o asiento inválido.")
            return False

        if self.seats[row - 1][seat_number - 1]:
            print("Lo siento, este asiento ya está reservado.")
            return False

        self.seats[row - 1][seat_number - 1] = True
        print(f"Asiento en la fila {row}, asiento {seat_number} reservado con éxito.")
        return True

    def cancel_reservation(self, row, seat_number):
        """ Cancela la reserva de un asiento """
        if row < 1 or row > self.rows or seat_number < 1 or seat_number > self.seats_per_row:
            print("Número de fila o asiento inválido.")
            return False

        if not self.seats[row - 1][seat_number - 1]:
            print("Este asiento no está reservado.")
            return False

        self.seats[row - 1][seat_number - 1] = False
        print(f"Reserva del asiento en la fila {row}, asiento {seat_number} cancelada.")
        return True

    def show_seating(self):
        """ Muestra el estado actual de la sala """
        print("Estado actual de la sala:")
        for i in range(self.rows):
            for j in range(self.seats_per_row):
                status = "Ocupado" if self.seats[i][j] else "Disponible"
                print(f"Fila {i + 1}, Asiento {j + 1}: {status}")
            print()


# Ejemplo de uso del sistema de reservas
if __name__ == "__main__":
    # Crear una sala de cine con 5 filas y 10 asientos por fila
    cine = Cinema(rows=5, seats_per_row=10)

    # Mostrar el estado inicial de la sala
    cine.show_seating()

    # Reservar algunos asientos
    cine.reserve_seat(1, 3)
    cine.reserve_seat(3, 5)
    cine.reserve_seat(5, 10)

    # Mostrar el estado de la sala después de reservar
    cine.show_seating()

    # Cancelar una reserva
    cine.cancel_reservation(3, 5)

    # Mostrar el estado de la sala después de cancelar la reserva
    cine.show_seating()
