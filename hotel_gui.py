import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from hotelManager import HotelManager
from hotel import Hotel
from registro import guardar_hotel_json

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roomio - Gestión de Hoteles")
        self.root.geometry("400x500")
        self.hotel = None
        self.manager = HotelManager()
        self.create_login_screen()
    
    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Bienvenido a Roomio", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Nombre del Hotel").pack()
        self.hotel_name_entry = tk.Entry(self.root)
        self.hotel_name_entry.pack()
        
        tk.Label(self.root, text="Contraseña").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Iniciar Sesión", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Registrar Nuevo Hotel", command=self.create_register_screen).pack()
    
    def login(self):
        name = self.hotel_name_entry.get()
        password = self.password_entry.get()
        
        if self.manager.authenticate_hotel(name, password):
            self.hotel = self.manager.hotel
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Nombre o contraseña incorrectos")
    
    def create_register_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Registro de Nuevo Hotel", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Nombre del Hotel").pack()
        self.reg_name = tk.Entry(self.root)
        self.reg_name.pack()
        
        tk.Label(self.root, text="Teléfono").pack()
        self.reg_phone = tk.Entry(self.root)
        self.reg_phone.pack()
        
        tk.Label(self.root, text="Dirección").pack()
        self.reg_address = tk.Entry(self.root)
        self.reg_address.pack()
        
        tk.Label(self.root, text="Precio por noche").pack()
        self.reg_price = tk.Entry(self.root)
        self.reg_price.pack()
        
        tk.Label(self.root, text="Cantidad de Habitaciones").pack()
        self.reg_rooms = tk.Entry(self.root)
        self.reg_rooms.pack()
        
        tk.Button(self.root, text="Registrar", command=self.register_hotel).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.create_login_screen).pack()
    
    def register_hotel(self):
        name = self.reg_name.get()
        phone = self.reg_phone.get()
        address = self.reg_address.get()
        price = float(self.reg_price.get())
        rooms = int(self.reg_rooms.get())
        password = random.randint(1000, 5000)
        
        new_hotel = Hotel(name, rooms, address, phone, price, password)
        self.manager.hotel = new_hotel
        guardar_hotel_json(new_hotel)
        
        messagebox.showinfo("Registro Exitoso", f"Hotel registrado. Contraseña: {password}")
        self.create_login_screen()
    
    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text=f"Hotel: {self.hotel.hotel_name}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Ver Estado de Habitaciones", command=self.show_hotel_status).pack()
        tk.Button(self.root, text="Modificar Estado de Habitación", command=self.modify_room_status).pack()
        tk.Button(self.root, text="Calcular Precio", command=self.calculate_price).pack()
        tk.Button(self.root, text="Checkout", command=self.checkout).pack()
        tk.Button(self.root, text="Cerrar Sesión", command=self.create_login_screen).pack(pady=10)
    
    def show_hotel_status(self):
        status = "\n".join([f"Habitación {k}: {v}" for k, v in self.hotel.rooms.items()])
        messagebox.showinfo("Estado de Habitaciones", status)
    
    def modify_room_status(self):
        room_number = (simpledialog.askstring("Modificar Habitación", "Ingrese número de habitación:"))
        status = simpledialog.askstring("Modificar Estado", "Ingrese 'D' para Disponible o 'O' para Ocupada:").upper()
        self.hotel.modify_room_status(room_number, status)
        self.manager.save_hotels()
        
    
    def calculate_price(self):
        days = int(simpledialog.askstring("Calcular Precio", "Ingrese la cantidad de noches a hospedar:"))
        total_price = self.hotel.price_calculate(days)
        messagebox.showinfo("Precio Total", f"Total a pagar por {days} noches: ${total_price:.2f}")
    
    def checkout(self):
        room_number = (simpledialog.askstring("Checkout", "Ingrese el número de habitación:"))
        if self.hotel.rooms.get(room_number) == "Ocupada":
            days = int(simpledialog.askstring("Checkout", "Ingrese la cantidad de noches hospedadas:"))
            total_price = self.hotel.price_calculate(days)
            self.hotel.modify_room_status(room_number, 'D')
            self.manager.save_hotels()
            messagebox.showinfo("Checkout Exitoso", f"Total a pagar por {days} noches: ${total_price:.2f}")
        else:
            messagebox.showerror("Error", "La habitación ya está disponible o no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()