import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importujemy ttk, żeby używać ComboBoxa
from cryptography.fernet import Fernet
import pyperclip
import random
import string
import threading

# Funkcja generująca klucz szyfrujący
def generate_key():
    return Fernet.generate_key()

# Funkcja szyfrująca hasło
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Funkcja deszyfrująca hasło
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# Funkcja do kopiowania hasła do schowka
def copy_to_clipboard(password, time_label):
    pyperclip.copy(password)
    update_timer(30, time_label)

# Funkcja do aktualizacji timera
def update_timer(time_left, time_label):
    if time_left > 0:
        time_label.config(text=f"Czas: {time_left}s")
        time_label.after(1000, update_timer, time_left-1, time_label)
    else:
        pyperclip.copy("")  # Usuwamy hasło z schowka po 30 sekundach
        time_label.config(text="Czas: 0s")

# Funkcja pokazująca szczegóły hasła
def show_details(details):
    messagebox.showinfo("Szczegóły", details)

# Funkcja dodaje nową grupę
def add_group():
    def submit_password():
        group = name_entry.get()

        if not group:
            messagebox.showwarning("Błąd", "Nazwa grupy jest wymagana !")
            return

        places.append(group)
        add_group_window.destroy()

     # Tworzymy okno formularza do dodawania hasła
    add_group_window = tk.Toplevel(root)
    add_group_window.title("Dodaj grupę")
    
    tk.Label(add_group_window, text="Tytuł:").pack(pady=5)
    name_entry = tk.Entry(add_group_window, width=30)
    name_entry.pack(pady=5, padx=5)
    
    submit_button = tk.Button(add_group_window, text="Dodaj grupę", command=submit_password)
    submit_button.pack(pady=10)

# Funkcja dodająca nowe hasło
def add_password():
    def submit_password():
        title = title_entry.get()
        login = login_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        description = description_entry.get()
        link = link_entry.get()
        place = place_combobox.get()  # Zmieniamy na ComboBoxa

        if not title or not login or not password:
            messagebox.showwarning("Błąd", "Tytuł, login i hasło są wymagane!")
            return

        if password != confirm_password:
            messagebox.showwarning("Błąd", "Hasła nie pasują do siebie!")
            return

        encrypted_password = encrypt_password(password, key)
        passwords.append({
            'title': title,
            'login': login,
            'password': encrypted_password,
            'description': description,
            'link': link,
            'place': place
        })
        
        update_places(place)  # Aktualizujemy listę miejsc
        show_passwords()
        add_password_window.destroy()

    # Tworzymy okno formularza do dodawania hasła
    add_password_window = tk.Toplevel(root)
    add_password_window.title("Dodaj hasło")
    
    tk.Label(add_password_window, text="Tytuł:").pack(pady=5)
    title_entry = tk.Entry(add_password_window, width=30)
    title_entry.pack(pady=5, padx=5)
    
    tk.Label(add_password_window, text="Login:").pack(pady=5)
    login_entry = tk.Entry(add_password_window, width=30)
    login_entry.pack(pady=5)
    
    tk.Label(add_password_window, text="Hasło:").pack(pady=5)
    password_entry = tk.Entry(add_password_window, width=30, show="*")  # Hasło ukryte
    password_entry.pack(pady=5)

    # Przycisk "Pokaż hasło"
    show_password_button = tk.Button(add_password_window, text="👁️", command=lambda: toggle_password(password_entry, show_password_button))
    show_password_button.pack(pady=5)

    tk.Label(add_password_window, text="Powtórz hasło:").pack(pady=5)
    confirm_password_entry = tk.Entry(add_password_window, width=30, show="*")  # Hasło ukryte
    confirm_password_entry.pack(pady=5)
    
    tk.Label(add_password_window, text="Opis:").pack(pady=5)
    description_entry = tk.Entry(add_password_window, width=30)
    description_entry.pack(pady=5)
    
    tk.Label(add_password_window, text="Link:").pack(pady=5)
    link_entry = tk.Entry(add_password_window, width=30)
    link_entry.pack(pady=5)

    # Zamiast Entry dla Miejsca, używamy ComboBoxa
    tk.Label(add_password_window, text="Miejsce:").pack(pady=5)
    place_combobox = ttk.Combobox(add_password_window, values=places, state="readonly", width=30)  # ComboBox z listą miejsc
    place_combobox.pack(pady=5)
    place_combobox.set("Wybierz miejsce")  # Domyślny wybór
    
    # Przycisk generowania hasła
    generate_button = tk.Button(add_password_window, text="Generuj hasło", command=lambda: password_entry.insert(0, generate_strong_password()))
    generate_button.pack(pady=5)

    submit_button = tk.Button(add_password_window, text="Dodaj hasło", command=submit_password)
    submit_button.pack(pady=10)

# Funkcja do przełączania widoczności hasła
def toggle_password(password_entry, button):
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        button.config(text="🔒")
    else:
        password_entry.config(show="*")
        button.config(text="👁️")

# Funkcja generująca silne hasło
def generate_strong_password(length=12):
    """Generuje silne hasło składające się z małych liter, dużych liter, cyfr i znaków specjalnych."""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(all_characters) for i in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

# Funkcja do edytowania hasła
def edit_password(password_data):
    def submit_edit():
        new_title = title_entry.get()
        new_login = login_entry.get()
        new_password = password_entry.get()
        new_confirm_password = confirm_password_entry.get()
        new_description = description_entry.get()
        new_link = link_entry.get()
        new_place = place_combobox.get()

        if not new_title or not new_login or not new_password:
            messagebox.showwarning("Błąd", "Tytuł, login i hasło są wymagane!")
            return

        if new_password != new_confirm_password:
            messagebox.showwarning("Błąd", "Hasła nie pasują do siebie!")
            return

        encrypted_password = encrypt_password(new_password, key)

        # Aktualizowanie danych hasła
        password_data.update({
            'title': new_title,
            'login': new_login,
            'password': encrypted_password,
            'description': new_description,
            'link': new_link,
            'place': new_place
        })
        
        update_places(new_place)  # Aktualizujemy listę miejsc, jeśli trzeba
        show_passwords()  # Odświeżamy listę haseł
        edit_password_window.destroy()

    # Tworzymy okno formularza do edytowania hasła
    edit_password_window = tk.Toplevel(root)
    edit_password_window.title("Edytuj hasło")
    
    tk.Label(edit_password_window, text="Tytuł:").pack(pady=5)
    title_entry = tk.Entry(edit_password_window, width=30)
    title_entry.insert(0, password_data['title'])  # Ustawiamy obecny tytuł
    title_entry.pack(pady=5, padx=5)
    
    tk.Label(edit_password_window, text="Login:").pack(pady=5)
    login_entry = tk.Entry(edit_password_window, width=30)
    login_entry.insert(0, password_data['login'])  # Ustawiamy obecny login
    login_entry.pack(pady=5)
    
    tk.Label(edit_password_window, text="Hasło:").pack(pady=5)
    password_entry = tk.Entry(edit_password_window, width=30, show="*")
    password_entry.insert(0, decrypt_password(password_data['password'], key))  # Ustawiamy obecne hasło (deszyfrowane)
    password_entry.pack(pady=5)

    # Przycisk "Pokaż hasło"
    show_password_button = tk.Button(edit_password_window, text="👁️", command=lambda: toggle_password(password_entry, show_password_button))
    show_password_button.pack(pady=5)

    tk.Label(edit_password_window, text="Powtórz hasło:").pack(pady=5)
    confirm_password_entry = tk.Entry(edit_password_window, width=30, show="*")
    confirm_password_entry.insert(0, decrypt_password(password_data['password'], key))  # Powtórzenie obecnego hasła
    confirm_password_entry.pack(pady=5)
    
    tk.Label(edit_password_window, text="Opis:").pack(pady=5)
    description_entry = tk.Entry(edit_password_window, width=30)
    description_entry.insert(0, password_data['description'])  # Ustawiamy obecny opis
    description_entry.pack(pady=5)
    
    tk.Label(edit_password_window, text="Link:").pack(pady=5)
    link_entry = tk.Entry(edit_password_window, width=30)
    link_entry.insert(0, password_data['link'])  # Ustawiamy obecny link
    link_entry.pack(pady=5)

    # Zamiast Entry dla Miejsca, używamy ComboBoxa
    tk.Label(edit_password_window, text="Miejsce:").pack(pady=5)
    place_combobox = ttk.Combobox(edit_password_window, values=places, state="readonly", width=30)  # ComboBox z listą miejsc
    place_combobox.set(password_data['place'])  # Ustawiamy obecne miejsce
    place_combobox.pack(pady=5)
    
    # Przycisk generowania hasła
    generate_button = tk.Button(edit_password_window, text="Generuj hasło", command=lambda: password_entry.insert(0, generate_strong_password()))
    generate_button.pack(pady=5)

    submit_button = tk.Button(edit_password_window, text="Zapisz zmiany", command=submit_edit)
    submit_button.pack(pady=10)

# Funkcja renderująca listę haseł z przyciskiem "Edytuj"
def show_passwords():
    # Usuwamy wszystkie obecne widgety (hasła) w oknie
    for widget in scrollable_frame.winfo_children():
        widget.grid_forget()

    # Tworzymy nagłówki tabeli
    headers = ["Tytuł", "Login", "Kopiuj", "Szczegóły", "Edytuj"]
    for col, header in enumerate(headers):
        header_label = tk.Label(scrollable_frame, text=header, font=("Helvetica", 10, "bold"))
        header_label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

    # Sprawdzamy, które miejsce jest wybrane w comboboxie
    selected_place = place_combobox.get()
    filtered_passwords = passwords if selected_place == "Wszystkie" else [p for p in passwords if p['place'] == selected_place]

    # Wyświetlamy listę haseł z odpowiednimi danymi
    for index, password_data in enumerate(filtered_passwords, start=1):  # Rozpoczynamy od wiersza 1 (po nagłówkach)
        # Tytuł oraz login
        password_label = tk.Label(scrollable_frame, text=f"{password_data['title']}", anchor="w")
        password_label.grid(row=index, column=0, sticky="w", padx=10)

        login_label = tk.Label(scrollable_frame, text=f"{password_data['login']}", anchor="w")
        login_label.grid(row=index, column=1, sticky="w", padx=10)

        # Przycisk "Kopiuj"
        copy_button = tk.Button(scrollable_frame, text="Kopiuj hasło", command=lambda p=password_data: copy_to_clipboard(decrypt_password(p['password'], key), time_label))
        copy_button.grid(row=index, column=2, padx=5, pady=5)

        # Przycisk "Szczegóły"
        details_button = tk.Button(scrollable_frame, text="Szczegóły", command=lambda p=password_data: show_details(p['description']))
        details_button.grid(row=index, column=3, padx=5, pady=5)

        # Przycisk "Edytuj"
        edit_button = tk.Button(scrollable_frame, text="Edytuj", command=lambda p=password_data: edit_password(p))
        edit_button.grid(row=index, column=4, padx=5, pady=5)

    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


# Funkcja do aktualizacji miejsc w comboboxie
def update_places(new_place):
    if new_place not in places:
        places.append(new_place)
        place_combobox['values'] = places  # Aktualizujemy ComboBox
        place_combobox.set("Wszystkie")  # Opcjonalnie ustawiamy domyślną wartość

# Funkcja zamknięcia aplikacji
def on_closing():
    if messagebox.askokcancel("Zamknij", "Czy na pewno chcesz zamknąć aplikację?"):
        root.destroy()

# Główna aplikacja
root = tk.Tk()
root.title("Menedżer Haseł")
root.geometry("600x500")

# Ramka na przewijanie
canvas = tk.Canvas(root)
canvas.pack(side="top", fill="both", expand=True)

# Dodajemy pasek przewijania
scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Przypisujemy frame do canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Tworzymy okno w canvasie
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Umieszczamy pasek przewijania
scrollbar.pack(side="right", fill="y")

# Lista haseł
passwords = []

# Generujemy klucz szyfrujący
key = generate_key()

# Lista miejsc - statyczna
places = ["Wszystkie", "Miejsce1", "Miejsce2", "Miejsce3"]  # Możesz dostosować listę miejsc

# Ramka na dolne przyciski
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x", pady=10)

# Funkcja do odświeżania wartości w ComboBoxie
def refresh_place_combobox(event=None):
    place_combobox['values'] = places  # Aktualizuje zawartość ComboBoxa

# ComboBox dla miejsc
place_combobox = ttk.Combobox(bottom_frame, values=places, state="readonly", width=20)
place_combobox.pack(side="left", padx=10)

# Ustawienie zdarzenia dla ComboBoxa
place_combobox.bind("<Button-1>", refresh_place_combobox)  # Odświeża listę przy kliknięciu na ComboBox

# Zdarzenie zmiany w comboboxie (odświeżanie haseł)
place_combobox.bind("<<ComboboxSelected>>", lambda event: show_passwords())

# Przycisk Dodaj grupę
add_button = tk.Button(bottom_frame, text="+ Dodaj grupę", command=add_group)
add_button.pack(side="left", padx=10)

# Przycisk Dodaj hasło
add_button = tk.Button(bottom_frame, text="+ Dodaj hasło", command=add_password)
add_button.pack(side="right", padx=10)

# Czas
time_label = tk.Label(bottom_frame, text="", anchor="w")
time_label.pack(side="right", padx=10)

# Pokazujemy hasła
show_passwords()

# Uruchamiamy aplikację
root.mainloop()
