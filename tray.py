from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw
import threading
#from app import App

from PIL import Image, ImageDraw

def create_image():
    # Tworzymy obrazek 200x200 px z przezroczystym tłem
    img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))  # (R, G, B, A) gdzie A = 0 (pełna przezroczystość)
    draw = ImageDraw.Draw(img)

    # Kolor litery "T" (czarny)
    color = (0, 0, 0)  # Czarny

    # Rysowanie poziomej części litery "T"
    draw.line((50, 50, 150, 50), fill=color, width=20)  # Linia pozioma

    # Rysowanie pionowej części litery "T"
    draw.line((100, 50, 100, 150), fill=color, width=20)  # Linia pionowa

    # Zmiana rozmiaru obrazu do 64x64 px
    img = img.resize((64, 64))

    return img



def setup_tray(app_instances, quit_callback):
    # Tworzenie menu dla tray'a
    menu = Menu(
        item('\u2705 Checklist', lambda: show_window(app_instances, 'checklist')),
        item('\U0001F4DD Notebook', lambda: show_window(app_instances, 'notebook')),
        item('\U0001F4CA Raports', lambda: show_window(app_instances, 'reports')),
        item('\U0001F511 Passwords', lambda: show_window(app_instances, 'passwords')),
        item('\U0001F504 File converter', lambda: show_window(app_instances, 'passwords')),
        item('\U0001F6AA Quit', quit_callback)
    )
    
    # Tworzenie ikony tray
    icon = Icon("Organizer", create_image(), menu=menu)
    
    # Uruchomienie ikony tray w osobnym wątku
    tray_thread = threading.Thread(target=icon.run, daemon=True)
    tray_thread.start()

def show_window(app_instances, app_name):
    # Funkcja do pokazywania odpowiedniego okna na podstawie wybranego modułu
    app = app_instances.get(app_name)
    if app:
        app.root.deiconify()  # Pokazuje okno aplikacji
