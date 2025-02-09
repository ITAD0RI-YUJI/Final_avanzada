from hotel import Hotel

class HotelManager:
    
    def show_menu(self):
        while True:
            print("\n1. Ver estado de habitaciones\n2. Modificar estado de habitación\n3. Calcular precio\n4. Salir")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.hotel.show_hotel_status()
            elif choice == "2":
                self.modify_room_status()
            elif choice == "3":
                self.calculate_price()
            elif choice == "4":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("⚠ Opción inválida. Intente nuevamente.")

    def modify_room_status(self):
        try:
            room_number = int(input("Ingrese el número de habitación: "))
            status = input("Ingrese el nuevo estado (D para Disponible / O para Ocupada): ").upper()
            self.hotel.modify_room_status(room_number, status)
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número de habitación válido.")

    def calculate_price(self):
        try:
            days = int(input("Ingrese la cantidad de noches a hospedar: "))
            total_price = self.hotel.price_calculate(days)
            print(f"💵 El precio total por {days} noches es: ${total_price:.2f}")
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")
