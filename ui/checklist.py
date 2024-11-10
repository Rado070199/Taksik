import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

def show_details(task):
    # Funkcja wyświetlająca szczegóły zadania
    messagebox.showinfo("Szczegóły zadania", f"Szczegóły zadania: {task['details']}")

def toggle_history():
    # Funkcja przełączająca widok między wszystkimi zadaniami a tylko zadaniami z status False
    if show_all.get():  # Jeśli widzimy wszystkie zadania, zmieniamy na tylko zadania False
        show_all.set(False)
        history_button.config(text="All")  # Zmieniamy tekst przycisku na "All"
        show_active_tasks()  # Pokazujemy zadania False
    else:  # Jeśli widzimy tylko zadania False, zmieniamy na wszystkie zadania
        show_all.set(True)
        history_button.config(text="To Do")  # Zmieniamy tekst przycisku na "To Do"
        show_history()  # Pokazujemy wszystkie zadania

def show_history():
    # Funkcja wyświetlająca historię (wszystkie zadania)
    render_tasks(include_all=True)

def show_active_tasks():
    # Funkcja wyświetlająca tylko aktywne zadania (status False)
    render_tasks(include_all=False)

def on_closing():
    # Funkcja do zamknięcia aplikacji
    if messagebox.askokcancel("Zamknij", "Czy na pewno chcesz zamknąć aplikację?"):
        root.destroy()

def add_task():
    # Otwiera formularz do wprowadzenia nowego zadania
    def submit_task():
        task_title = title_entry.get()  # Tytuł zadania
        task_details = details_text.get("1.0", "end-1c")  # Szczegóły zadania z pola Text
        task_priority = priority_var.get()  # Priorytet zadania
        task_due_date = due_date_entry.get()  # Data do kiedy

        # Walidacja daty
        try:
            task_due_date = datetime.strptime(task_due_date, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Błąd", "Proszę podać poprawny format daty (YYYY-MM-DD).")
            return

        if not task_title or not task_details:
            messagebox.showwarning("Błąd", "Tytuł i szczegóły są wymagane!")
        else:
            tasks.append({"title": task_title, "details": task_details, "completed": False, 
                          "priority": task_priority, "due_date": task_due_date})
            show_active_tasks()  # Po dodaniu zadania pokazujemy aktywne zadania
            add_task_window.destroy()

    # Tworzymy okno formularza do dodawania zadania
    add_task_window = tk.Toplevel(root)
    add_task_window.title("Dodaj zadanie")
    
    # Etykiety i pola do wprowadzenia tytułu i szczegółów zadania
    tk.Label(add_task_window, text="Tytuł zadania:").pack(pady=5)
    title_entry = tk.Entry(add_task_window, width=30)
    title_entry.pack(pady=5)
    
    tk.Label(add_task_window, text="Szczegóły zadania:").pack(pady=5)
    details_text = tk.Text(add_task_window, width=30, height=6)  # Zmieniliśmy na Text, większe pole
    details_text.pack(pady=5)
    
    # Priorytet
    tk.Label(add_task_window, text="Priorytet:").pack(pady=5)
    priority_var = tk.StringVar(value="low")  # Domyślny priorytet
    tk.Radiobutton(add_task_window, text="Low", variable=priority_var, value="low").pack(anchor="w")
    tk.Radiobutton(add_task_window, text="Medium", variable=priority_var, value="medium").pack(anchor="w")
    tk.Radiobutton(add_task_window, text="High", variable=priority_var, value="high").pack(anchor="w")

    # Data do kiedy
    tk.Label(add_task_window, text="Data do kiedy (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(add_task_window, width=30)
    due_date_entry.pack(pady=5)
    
    # Przyciski w formularzu
    submit_button = tk.Button(add_task_window, text="Dodaj zadanie", command=submit_task)
    submit_button.pack(pady=10)

def remove_task(idx):
    # Usuń zadanie na podstawie indeksu
    if 0 <= idx < len(tasks):
        tasks.pop(idx)  # Usuwamy zadanie z listy
        show_active_tasks()  # Po usunięciu zadania pokazujemy aktywne zadania

def update_task_status(var, task):
    # Funkcja zmieniająca status zadania i odświeżająca listę
    task["completed"] = var.get()  # Ustawiamy status zadania na podstawie zmiennej checkboxa
    if show_all.get():  # Jeśli jesteśmy w trybie "Historia", pokazujemy wszystkie zadania
        show_history()
    else:  # Jeśli jesteśmy w trybie "Zadania", pokazujemy tylko te nieukończone
        show_active_tasks()

def edit_task(idx):
    # Funkcja umożliwiająca edycję zadania
    def submit_edit():
        task_title = title_entry.get()  # Tytuł zadania
        task_details = details_text.get("1.0", "end-1c")  # Szczegóły zadania z pola Text
        task_priority = priority_var.get()  # Priorytet zadania
        task_due_date = due_date_entry.get()  # Data do kiedy

        # Walidacja daty
        try:
            task_due_date = datetime.strptime(task_due_date, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Błąd", "Proszę podać poprawny format daty (YYYY-MM-DD).")
            return

        if not task_title or not task_details:
            messagebox.showwarning("Błąd", "Tytuł i szczegóły są wymagane!")
        else:
            tasks[idx] = {"title": task_title, "details": task_details, "completed": tasks[idx]["completed"], 
                          "priority": task_priority, "due_date": task_due_date}
            edit_task_window.destroy()
            show_active_tasks()

    # Tworzymy okno formularza do edytowania zadania
    task = tasks[idx]  # Pobieramy zadanie na podstawie indeksu
    edit_task_window = tk.Toplevel(root)
    edit_task_window.title("Edytuj zadanie")
    
    # Etykiety i pola do edytowania tytułu i szczegółów zadania
    tk.Label(edit_task_window, text="Tytuł zadania:").pack(pady=5)
    title_entry = tk.Entry(edit_task_window, width=30)
    title_entry.insert(0, task["title"])  # Wstawiamy aktualny tytuł
    title_entry.pack(pady=5)
    
    tk.Label(edit_task_window, text="Szczegóły zadania:").pack(pady=5)
    details_text = tk.Text(edit_task_window, width=30, height=6)  # Zmieniliśmy na Text, większe pole
    details_text.insert("1.0", task["details"])  # Wstawiamy aktualne szczegóły
    details_text.pack(pady=5)
    
    # Priorytet
    tk.Label(edit_task_window, text="Priorytet:").pack(pady=5)
    priority_var = tk.StringVar(value=task["priority"])  # Ustawiamy aktualny priorytet
    tk.Radiobutton(edit_task_window, text="Low", variable=priority_var, value="low").pack(anchor="w")
    tk.Radiobutton(edit_task_window, text="Medium", variable=priority_var, value="medium").pack(anchor="w")
    tk.Radiobutton(edit_task_window, text="High", variable=priority_var, value="high").pack(anchor="w")

    # Data do kiedy
    tk.Label(edit_task_window, text="Data do kiedy (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = tk.Entry(edit_task_window, width=30)
    due_date_entry.insert(0, task["due_date"].strftime("%Y-%m-%d"))  # Wstawiamy aktualną datę
    due_date_entry.pack(pady=5)
    
    # Przyciski w formularzu
    submit_button = tk.Button(edit_task_window, text="Zapisz zmiany", command=submit_edit)
    submit_button.pack(pady=10)

def render_tasks(include_all=False):
    # Funkcja renderująca listę zadań
    for widget in scrollable_frame.winfo_children():
        widget.grid_forget()  # Usuwamy wszystkie poprzednie widgety
    
    checkbox_vars.clear()  # Czyszczymy listę zmiennych dla checkboxów
    
    # Filtrujemy zadania do wyświetlenia
    tasks_to_display = tasks if include_all else [task for task in tasks if not task["completed"]]
    
    # Sortujemy zadania według daty
    tasks_to_display.sort(key=lambda x: x["due_date"])

    for index, task in enumerate(tasks_to_display):
        var = tk.BooleanVar(value=task["completed"])

        # Ustalamy szerokość dla kolumn w gridzie (w procentach)
        scrollable_frame.grid_columnconfigure(0, weight=3, minsize=200)  # Tytuł zadania - szerokość 3
        scrollable_frame.grid_columnconfigure(1, weight=1, minsize=100)  # Szczegóły
        scrollable_frame.grid_columnconfigure(2, weight=1, minsize=100)  # Usuń
        scrollable_frame.grid_columnconfigure(3, weight=1, minsize=100)  # Modyfikuj

        # Tytuł zadania w pierwszej kolumnie
        checkbox = tk.Checkbutton(scrollable_frame, text=task["title"], variable=var, anchor="w")
        checkbox.grid(row=index, column=0, sticky="w", padx=10, pady=5)

        # Zmieniamy kolor tytułu w zależności od priorytetu
        if task["priority"] == "low":
            checkbox.config(fg="green")
        elif task["priority"] == "medium":
            checkbox.config(fg="yellow")
        elif task["priority"] == "high":
            checkbox.config(fg="red")
        
        # Zmieniamy status zadania przy zmianie stanu checkboxa
        var.trace("w", lambda *args, var=var, task=task: update_task_status(var, task))
        
        # Przyciski umieszczamy w trzech osobnych kolumnach
        details_button = tk.Button(scrollable_frame, text="Details", command=lambda t=task: show_details(t))
        details_button.grid(row=index, column=1, padx=5, pady=5, sticky="ew")

        remove_button = tk.Button(scrollable_frame, text="Usuń", command=lambda idx=index: remove_task(idx))
        remove_button.grid(row=index, column=2, padx=5, pady=5, sticky="ew")

        edit_button = tk.Button(scrollable_frame, text="Modyfikuj", command=lambda idx=index: edit_task(idx))
        edit_button.grid(row=index, column=3, padx=5, pady=5, sticky="ew")

    # Aktualizujemy regiony w canvasie, aby umożliwić przewijanie
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Tworzymy główną aplikację
root = tk.Tk()
root.title("Checklist z Zadaniami")

# Ustawienie rozmiaru okna
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

# Lista zadań
tasks = [
    {"title": "Zadanie 1", "details": "Szczegóły zadania 1", "completed": False, "priority": "low", "due_date": datetime(2024, 12, 1).date()},
    {"title": "Zadanie 2", "details": "Szczegóły zadania 2", "completed": False, "priority": "medium", "due_date": datetime(2024, 12, 5).date()},
    {"title": "Zadanie 3", "details": "Szczegóły zadania 3", "completed": True, "priority": "high", "due_date": datetime(2024, 11, 20).date()}
]

checkbox_vars = []  # Zmienna do trzymania zmiennych checkboxów
show_all = tk.BooleanVar(value=False)  # Zmienna przechowująca, czy widzimy wszystkie zadania

# Ramka na dolne przyciski
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x", pady=10)

# Przycisk Dodaj
add_button = tk.Button(bottom_frame, text="Dodaj", command=add_task)
add_button.pack(side="left", padx=10)

# Przycisk Historia
history_button = tk.Button(bottom_frame, text="All", command=toggle_history)
history_button.pack(side="left", padx=10)

# Przycisk Zadania
active_button = tk.Button(bottom_frame, text="Zadania", command=show_active_tasks)
active_button.pack(side="left", padx=10)

# Przycisk Zamknij
close_button = tk.Button(bottom_frame, text="Zamknij", command=on_closing)
close_button.pack(side="right", padx=10)

# Zdarzenie zamknięcia okna
root.protocol("WM_DELETE_WINDOW", on_closing)

# Początkowo pokazujemy tylko aktywne zadania (status False)
show_active_tasks()

# Uruchamiamy aplikację
root.mainloop()
