import tkinter as tk
from tkinter import ttk
import pandas as pd

class ReportsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raporty")
        self.root.geometry("600x400")
        self.create_report_interface()

    def create_report_interface(self):
        # Przykładowe dane do raportu (możesz je zastąpić własnymi danymi)
        data = {
            "Zadanie": ["Zadanie 1", "Zadanie 2", "Zadanie 3", "Zadanie 4", "Zadanie 5"],
            "Status": ["Wykonane", "Wykonane", "W trakcie", "Oczekujące", "Wykonane"],
            "Czas Trwania": ["2h", "1h", "30m", "1h", "4h"]
        }

        # Tworzenie ramki danych Pandas z przykładowymi danymi
        self.df = pd.DataFrame(data)

        # Tworzenie widoku tabeli z użyciem ttk.Treeview
        self.tree = ttk.Treeview(self.root, show="headings")
        
        # Dodanie kolumn do treeview
        self.tree["columns"] = self.df.columns.tolist()

        # Dodanie nagłówków dla każdej kolumny
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="w")  # Możesz dodać szerokość i wyrównanie kolumny
        
        # Dodanie danych do tabeli
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=row.tolist())

        # Przycisk do generowania raportu
        generate_report_btn = ttk.Button(self.root, text="Generuj Raport", command=self.generate_report)
        generate_report_btn.pack(pady=5)

        # Przycisk do zamknięcia okna raportów
        close_btn = ttk.Button(self.root, text="Zamknij", command=self.hide_window)
        close_btn.pack(pady=10)

        # Wyświetlenie tabeli
        self.tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def generate_report(self):
        # Możesz tutaj dodać logikę generowania raportów (np. eksport do pliku CSV)
        report_file = "raport.csv"
        self.df.to_csv(report_file, index=False)
        self.show_message(f"Raport zapisany do {report_file}", "Sukces")

    def hide_window(self):
        # Ukrywa okno raportu
        self.root.withdraw()

    def show_message(self, message, title):
        # Wyświetla komunikaty, np. po zapisaniu raportu
        message_window = tk.Toplevel(self.root)
        message_window.title(title)
        label = ttk.Label(message_window, text=message, padding=10)
        label.pack(padx=10, pady=10)
        close_btn = ttk.Button(message_window, text="Zamknij", command=message_window.destroy)
        close_btn.pack(pady=5)
