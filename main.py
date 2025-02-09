from hotelManager import *
from registro import *

# Ejecutar el programa
if __name__ == "__main__":

    registro = input("Bienvenido a Roomio, ¿tienes cuenta ya creada?: ")
    registro.lower()

    if((registro == 'si')):
        manager = HotelManager()
        manager.show_menu()

    elif(registro == 'no'):
        create_hotel()

    else:
        print("\n♠ No seleccionaste ninguna opción válida, vuelve a intentar")
