import json
from hotel import Hotel
import threading

class HotelManager:

    def __init__(self):
        self.hotel = None

    def load_hotels(self):
        hotels = []
        
        def load():
            nonlocal hotels
            try:
                with open("hoteles.json", "r") as file:
                    hotels = json.load(file)
            except FileNotFoundError:
                print("⚠ No se encontró el archivo hoteles.json.")
                hotels = []
        
        hilo = threading.Thread(target=load)
        hilo.start()
        hilo.join()  # Esperamos a que termine antes de continuar

        return hotels


    def authenticate_hotel(self, name, password):
        hotels = self.load_hotels()
        for hotel in hotels:
            if hotel["nombre"] == name and str(hotel["password"]) == password:
                self.hotel = Hotel(
                    hotel["nombre"],
                    len(hotel["habitaciones"]),
                    hotel["direccion"],
                    hotel["telefono"],
                    hotel["precio"],
                    hotel["password"]
                )
                self.hotel.rooms = hotel["habitaciones"]
                return True
        return False

    def save_hotels(self):
        def save():
            hotels = self.load_hotels()
            for hotel in hotels:
                if hotel["nombre"] == self.hotel.hotel_name:
                    hotel["habitaciones"] = self.hotel.rooms

            with open("hoteles.json", "w") as file:
                json.dump(hotels, file, indent=4)

        hilo = threading.Thread(target=save)
        hilo.start()  # El hilo se ejecuta sin bloquear el programa

    def show_menu(self):
        user = input("Ingresa el nombre del hotel: ")
        password = input("Ingresa la contraseña del hotel: ")

        if not self.authenticate_hotel(user, password):
            print("⚠ Nombre de hotel o contraseña incorrectos.")
            return

        while True:
            print("\n1. Ver estado de habitaciones\n2. Modificar estado de habitación\n3. Calcular precio\n4. Checkout\n5. Salir")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.hotel.show_hotel_status()
            elif choice == "2":
                self.modify_room_status()
            elif choice == "3":
                self.calculate_price()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida. Intente nuevamente.")

    def modify_room_status(self):
        try:
            room_number = input("Ingrese el número de habitación: ")
            status = input("Ingrese el nuevo estado (D para Disponible / O para Ocupada): ").upper()

            self.hotel.modify_room_status(room_number, status)
            self.save_hotels()  # Guardar cambios en JSON después de modificar estado

        except ValueError:
            print("\n⚠ Entrada inválida. Ingrese un número de habitación válido.")

    def calculate_price(self):
        try:
            days = int(input("Ingrese la cantidad de noches a hospedar: "))
            total_price = self.hotel.price_calculate(days)
            print(f"💵 El precio total por {days} noches es: ${total_price:.2f}")
        except ValueError:
            print("\n⚠ Entrada inválida. Ingrese un número válido.")

    def checkout(self):
        try:
            room_number = int(input("🏠 Ingrese el número de habitación para hacer checkout: "))

            if self.hotel.rooms.get(room_number) == "Ocupada":
                days = int(input("📅 Ingrese la cantidad de noches hospedadas: "))
                total_price = self.hotel.price_calculate(days)

                self.hotel.modify_room_status(room_number, 'D')  # Marcar habitación como disponible
                self.save_hotels()  # Guardar cambios en JSON

                print(f"\n✅ Checkout realizado con éxito.")
                print(f"💵 Total a pagar por {days} noches: ${total_price:.2f}")
            else:
                print("⚠ La habitación ya está disponible o no existe.")
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")