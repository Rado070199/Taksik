import tkinter as tk
from tkinter import ttk
from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw
import threading

class ChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checklist App")
        self.root.geometry("300x250")
        self.create_checklist()
    
    def create_checklist(self):
        self.tasks = [
            "Task 1",
            "Task 2",
            "Task 3",
            "Task 4"
        ]
        
        self.check_vars = []
        
        # Tworzenie checkboxów dla każdej taski
        for task in self.tasks:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.root, text=task, variable=var)
            checkbox.pack(anchor='w', padx=10, pady=5)
            self.check_vars.append(var)
        
        close_btn = ttk.Button(self.root, text="Close", command=self.hide_window)
        close_btn.pack(pady=10)
    
    def hide_window(self):
        self.root.withdraw()  # Ukrywa okno

def create_image():
    # Tworzenie ikony do tray'a
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill="blue")
    draw.text((10, 20), "C", fill="white")  # Na ikonie rysujemy literę "C" (od Checklist)
    return image

def show_window(app):
    app.root.deiconify()  # Pokazuje okno

def quit_app(icon, item, root):
    icon.stop()
    root.quit()

def setup_tray(app):
    icon_image = create_image()
    menu = Menu(
        item('Show Checklist', lambda: show_window(app)),
        item('Quit', lambda: quit_app(icon, item, app.root))
    )
    
    icon = Icon("ChecklistApp", icon_image, menu=menu)
    
    # Uruchomienie ikony tray w osobnym wątku
    tray_thread = threading.Thread(target=icon.run, daemon=True)
    tray_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChecklistApp(root)
    
    # Ukrycie okna na starcie
    root.withdraw()

    # Uruchomienie tray'a
    setup_tray(app)
    
    # Główna pętla aplikacji Tkinter
    root.mainloop()
