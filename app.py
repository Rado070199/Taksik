import tkinter as tk
from ui.checklist import ChecklistApp
from ui.notebook import NotebookApp
from ui.reports import ReportsApp
from ui.passwords import PasswordsApp
from tray import setup_tray

class App:
    def __init__(self):
        self.root_home = tk.Tk()
        self.root_home.withdraw()  # Ukrycie głównego okna na starcie
        
        self.home_app = ChecklistApp(self.root_home)
        self.checklist_app = ChecklistApp(self.create_window())
        self.notebook_app = NotebookApp(self.create_window())
        self.reports_app = ReportsApp(self.create_window())
        self.passwords_app = PasswordsApp(self.create_window())

        # Przechowujemy instancje aplikacji w słowniku, aby łatwo zarządzać dostępem do nich
        self.app_instances = {
            "checklist": self.checklist_app,
            "notebook": self.notebook_app,
            "reports": self.reports_app,
            "passwords": self.passwords_app
        }

        # Uruchomienie tray'a z menu
        setup_tray(self.app_instances, self.quit_app)

    def create_window(self):
        # Tworzenie nowego okna dla każdego modułu (notatnik, raporty, hasła)
        window = tk.Tk()
        window.withdraw()  # Ukrycie okna na początku
        return window

    def run(self):
        # Główna pętla aplikacji Tkinter
        self.root_home.mainloop()   

    def quit_app(self):
        # Zamknięcie wszystkich okien Tkintera i zakończenie aplikacji
        for app in self.app_instances.values():
            app.root.destroy()  # Zamknięcie każdego okna modułu
        self.root_home.destroy()  # Zamknięcie głównego okna          


if __name__ == "__main__":
    app = App()
    app.run()

