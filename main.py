from hotelManager import *
from registro import *

# Ejecutar el programa
if __name__ == "__main__":

    while True:
        print("Bienvenido a Roomio.😎")
        registro = input("¿Ya creaste una cuenta? Ingresa 1 para Sí o 2 para No.\n(1: Sí, 2: No): ")

        if registro == '1':
            manager = HotelManager()
            manager.show_menu()
            break

        elif registro == '2':
            create_hotel()
            break

        else:
            print("\nOpción no válida.😕 Por favor, ingresa 1 para Sí o 2 para No.")
            print()