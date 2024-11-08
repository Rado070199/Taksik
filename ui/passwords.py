import tkinter as tk
from tkinter import ttk, simpledialog

class PasswordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menedżer Haseł")
        self.root.geometry("400x400")
        self.passwords = {}  # Przechowywanie haseł w słowniku (nazwa -> hasło)
        self.create_password_manager()

    def create_password_manager(self):
        # Tworzenie widgetów do interfejsu
        self.username_entry = ttk.Entry(self.root, width=40)
        self.username_entry.pack(pady=5, padx=10)
        self.username_entry.insert(0, "Nazwa użytkownika")

        self.password_entry = ttk.Entry(self.root, width=40, show="*")
        self.password_entry.pack(pady=5, padx=10)
        self.password_entry.insert(0, "Hasło")

        save_btn = ttk.Button(self.root, text="Zapisz Hasło", command=self.save_password)
        save_btn.pack(pady=5)

        show_btn = ttk.Button(self.root, text="Pokaż Zapisane Hasła", command=self.show_passwords)
        show_btn.pack(pady=5)

        close_btn = ttk.Button(self.root, text="Zamknij", command=self.hide_window)
        close_btn.pack(pady=10)

    def save_password(self):
        # Zapisuje hasło użytkownika
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            self.passwords[username] = password
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.show_message("Hasło zapisane!", "Sukces")
        else:
            self.show_message("Proszę podać zarówno nazwę użytkownika, jak i hasło!", "Błąd")

    def show_passwords(self):
        # Pokazuje zapisane hasła w nowym oknie
        passwords_window = tk.Toplevel(self.root)
        passwords_window.title("Zapisane Hasła")

        for username, password in self.passwords.items():
            password_label = ttk.Label(passwords_window, text=f"{username}: {password}", wraplength=350, anchor="w")
            password_label.pack(padx=10, pady=5)

        close_btn = ttk.Button(passwords_window, text="Zamknij", command=passwords_window.destroy)
        close_btn.pack(pady=10)

    def hide_window(self):
        # Ukrywa okno menedżera haseł
        self.root.withdraw()

    def show_message(self, message, title):
        # Wyświetla komunikaty (np. po zapisaniu hasła)
        message_window = simpledialog.messagebox.showinfo(title, message)
