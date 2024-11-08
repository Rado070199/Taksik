import tkinter as tk
from tkinter import ttk

class ChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checklist")
        self.root.geometry("400x400")
        self.create_checklist()

    def create_checklist(self):
        # Lista zadań (możesz dodać lub zmieniać zadania)
        self.tasks = [
            "Zadanie 1",
            "Zadanie 2",
            "Zadanie 3",
            "Zadanie 4",
            "Zadanie 5"
        ]

        # Lista przechowująca zmienne związane z checkboxami
        self.check_vars = []

        # Tworzenie checkboxów dla każdej taski
        for task in self.tasks:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.root, text=task, variable=var)
            checkbox.pack(anchor='w', padx=10, pady=5)
            self.check_vars.append(var)

        # Przycisk do zamykania okna checklisty
        close_btn = ttk.Button(self.root, text="Zamknij", command=self.hide_window)
        close_btn.pack(pady=10)

        # Przycisk do wyświetlania statusu (sprawdzanie, które zadania zostały wykonane)
        status_btn = ttk.Button(self.root, text="Sprawdź Status", command=self.show_status)
        status_btn.pack(pady=5)

    def show_status(self):
        # Wyświetlanie statusu wykonania zadań
        completed_tasks = []
        for i, var in enumerate(self.check_vars):
            if var.get():
                completed_tasks.append(self.tasks[i])

        # Pokazanie zakończonych zadań
        if completed_tasks:
            status_message = "Zakończone zadania:\n" + "\n".join(completed_tasks)
        else:
            status_message = "Brak zakończonych zadań."
        
        # Okno do wyświetlania statusu
        status_window = tk.Toplevel(self.root)
        status_window.title("Status Zadań")
        status_label = ttk.Label(status_window, text=status_message, padding=10)
        status_label.pack()
        
        # Przycisk do zamknięcia okna statusu
        close_status_btn = ttk.Button(status_window, text="Zamknij", command=status_window.destroy)
        close_status_btn.pack(pady=10)

    def hide_window(self):
        # Funkcja do ukrywania okna checklisty (np. po kliknięciu w tray)
        self.root.withdraw()

