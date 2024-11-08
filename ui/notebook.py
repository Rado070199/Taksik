import tkinter as tk
from tkinter import ttk, simpledialog

class NotebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notatnik")
        self.root.geometry("400x400")
        self.notes = []  # Lista przechowująca notatki
        self.create_notebook()

    def create_notebook(self):
        # Tworzenie widgetów do interfejsu
        self.text_area = tk.Text(self.root, wrap="word", height=15, width=50)
        self.text_area.pack(padx=10, pady=10)

        # Przycisk do zapisywania notatki
        save_btn = ttk.Button(self.root, text="Zapisz Notatkę", command=self.save_note)
        save_btn.pack(pady=5)

        # Przycisk do pokazania zapisanych notatek
        show_notes_btn = ttk.Button(self.root, text="Pokaż Zapisane Notatki", command=self.show_notes)
        show_notes_btn.pack(pady=5)

        # Przycisk do zamknięcia okna notatnika
        close_btn = ttk.Button(self.root, text="Zamknij", command=self.hide_window)
        close_btn.pack(pady=10)

    def save_note(self):
        # Zapisuje notatkę z pola tekstowego do listy
        note = self.text_area.get("1.0", tk.END).strip()
        if note:
            self.notes.append(note)
            self.text_area.delete("1.0", tk.END)  # Wyczyść pole tekstowe po zapisaniu
            self.show_message("Notatka zapisana!", "Sukces")
        else:
            self.show_message("Brak tekstu do zapisania!", "Błąd")

    def show_notes(self):
        # Pokazuje zapisane notatki w nowym oknie
        notes_window = tk.Toplevel(self.root)
        notes_window.title("Zapisane Notatki")

        # Wyświetlenie każdej notatki
        for note in self.notes:
            note_label = ttk.Label(notes_window, text=note, wraplength=350, anchor="w")
            note_label.pack(padx=10, pady=5)

        close_btn = ttk.Button(notes_window, text="Zamknij", command=notes_window.destroy)
        close_btn.pack(pady=10)

    def hide_window(self):
        # Ukrywa okno notatnika
        self.root.withdraw()

    def show_message(self, message, title):
        # Wyświetla komunikaty (np. po zapisaniu notatki)
        message_window = simpledialog.messagebox.showinfo(title, message)
