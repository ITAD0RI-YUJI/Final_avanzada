class Hotel:
    def __init__(self, hotel_name, rooms, hotel_address, hotel_telephone, hotel_price , password):
        self.hotel_name = hotel_name
        self.rooms = {i + 1: 'Disponible' for i in range(rooms)}
        self.address = hotel_address
        self.hotel_telephone = hotel_telephone
        self.hotel_price = hotel_price
        self.password = password

    def modify_room_status(self, room_number, status):
        if room_number in self.rooms and status in ['D', 'O']:
            self.rooms[room_number] = 'Disponible' if status == 'D' else 'Ocupada'
            print(f"✔ Habitación {room_number} ahora está {self.rooms[room_number]}.")
        else:
            print("✖ Número de habitación o estado inválido.")

    def show_hotel_status(self):
        print("\nEstado del hotel:")
        for room, status in self.rooms.items():
            print(f" - Habitación {room}: {status}")

    def price_calculate(self, cant_dias):
        return self.hotel_price * cant_dias
