import json
import random
from hotel import Hotel

# Función para guardar en JSON
def guardar_hotel_json(hotel):
    data = []

    # Intentar leer el archivo JSON si ya existe
    try:
        with open("hoteles.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        pass  # Si no existe, se creará uno nuevo

    # Agregar el nuevo hotel
    data.append({
        "nombre": hotel.hotel_name,
        "telefono": hotel.hotel_telephone,
        "direccion": hotel.address,
        "precio": hotel.hotel_price,
        "habitaciones": hotel.rooms,
        "password": hotel.password
    })

    # Escribir los datos en JSON
    with open("hoteles.json", "w") as file:
        json.dump(data, file, indent=4)

def create_password():
    return random.randint(1000, 5000)

def bring_password():
    password = create_password()
    print(f"🤐 La contraseña para tu hotel es: {password} Bienvenido a ROOMIO")
    return password

# Función para crear un hotel
def create_hotel():
    hotel_name = input("\n🏨 Ingrese el nombre del hotel: ")
    hotel_telephone = input("📞 Ingrese el teléfono del hotel: ")
    hotel_address = input("📍 Ingrese la dirección del hotel: ")
    hotel_price = float(input("💰 Ingrese el precio por noche: "))
    rooms = int(input("🏠 Ingrese la cantidad de habitaciones: "))
    password = bring_password()

    hotel = Hotel(hotel_name, rooms, hotel_address, hotel_telephone, hotel_price, password)

    # Guardar en JSON
    guardar_hotel_json(hotel)

    print("\n✅ Hotel registrado exitosamente en hoteles.json")
