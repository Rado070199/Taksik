import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Funkcja generująca klucz szyfrujący
def generate_key():
    return Fernet.generate_key()

# Funkcja szyfrująca tekst
def encrypt_text():
    try:
        key = key_entry.get().encode()
        fernet = Fernet(key)
        text = text_entry.get("1.0", "end-1c")
        encrypted_text = fernet.encrypt(text.encode())
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_text.decode())
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować tekstu: {e}")

# Funkcja deszyfrująca tekst
def decrypt_text():
    try:
        key = key_entry.get().encode()
        fernet = Fernet(key)
        encrypted_text = text_entry.get("1.0", "end-1c").encode()
        decrypted_text = fernet.decrypt(encrypted_text).decode()
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się odszyfrować tekstu: {e}")

# Funkcja ustawiająca nowy klucz
def set_new_key():
    new_key = generate_key().decode()
    key_entry.delete(0, tk.END)
    key_entry.insert(tk.END, new_key)
    messagebox.showinfo("Nowy klucz", f"Nowy klucz wygenerowany: {new_key}")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Szyfrowanie i Odszyfrowanie Tekstu")
root.geometry("600x400")

# Stylizacja
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 10)
button_font = ("Helvetica", 10, "bold")

# Nagłówek
header_label = tk.Label(root, text="Aplikacja Szyfrująca", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

# Pole klucza szyfrującego
key_frame = tk.Frame(root)
key_frame.pack(pady=10)
key_label = tk.Label(key_frame, text="Klucz szyfrujący:", font=label_font)
key_label.grid(row=0, column=0, padx=5)
key_entry = tk.Entry(key_frame, font=entry_font, width=40)
key_entry.grid(row=0, column=1, padx=5)
generate_key_button = tk.Button(key_frame, text="Generuj klucz", font=button_font, command=set_new_key)
generate_key_button.grid(row=0, column=2, padx=5)

# Pole wprowadzenia tekstu
text_label = tk.Label(root, text="Tekst do zaszyfrowania/odszyfrowania:", font=label_font)
text_label.pack()
text_entry = tk.Text(root, font=entry_font, height=5, width=60)
text_entry.pack(pady=5)

# Przycisk szyfruj i odszyfruj
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
encrypt_button = tk.Button(button_frame, text="Szyfruj", font=button_font, command=encrypt_text, width=15)
encrypt_button.grid(row=0, column=0, padx=5)
decrypt_button = tk.Button(button_frame, text="Odszyfruj", font=button_font, command=decrypt_text, width=15)
decrypt_button.grid(row=0, column=1, padx=5)

# Pole wyniku
result_label = tk.Label(root, text="Wynik:", font=label_font)
result_label.pack()
result_text = tk.Text(root, font=entry_font, height=5, width=60, state="normal")
result_text.pack(pady=5)

# Uruchomienie pętli głównej
root.mainloop()
