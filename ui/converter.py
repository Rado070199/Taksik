import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from docx import Document
import fitz  # PyMuPDF

# Funkcja do konwersji PDF na DOCX
def pdf_to_word(pdf_path, output_path):
    try:
        doc = Document()
        pdf = fitz.open(pdf_path)
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text = page.get_text()
            doc.add_paragraph(text)
        pdf.close()
        doc.save(output_path)
        return True
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się przekonwertować PDF na DOCX: {e}")
        return False

# Funkcja do konwersji obrazów JPG na PNG
def jpg_to_png(image_path, output_path):
    try:
        img = Image.open(image_path)
        img.save(output_path, "PNG")
        return True
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się przekonwertować JPG na PNG: {e}")
        return False

# Funkcja do konwersji PNG na JPG
def png_to_jpg(image_path, output_path):
    try:
        img = Image.open(image_path)
        rgb_im = img.convert("RGB")
        rgb_im.save(output_path, "JPEG")
        return True
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się przekonwertować PNG na JPG: {e}")
        return False

# Funkcja obsługująca konwersje
def convert_file():
    input_file = filedialog.askopenfilename(title="Wybierz plik")
    if not input_file:
        return

    # Pobieramy format wejściowy i wyjściowy
    output_format = output_format_var.get()

    if input_file.endswith(".pdf") and output_format == "DOCX":
        output_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
        if output_file:
            if pdf_to_word(input_file, output_file):
                messagebox.showinfo("Sukces", "Plik PDF został pomyślnie przekonwertowany na DOCX.")
    elif input_file.endswith(".jpg") and output_format == "PNG":
        output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if output_file:
            if jpg_to_png(input_file, output_file):
                messagebox.showinfo("Sukces", "Plik JPG został pomyślnie przekonwertowany na PNG.")
    elif input_file.endswith(".png") and output_format == "JPG":
        output_file = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
        if output_file:
            if png_to_jpg(input_file, output_file):
                messagebox.showinfo("Sukces", "Plik PNG został pomyślnie przekonwertowany na JPG.")
    else:
        messagebox.showwarning("Błąd", "Wybrana konwersja nie jest obsługiwana.")

# Tworzymy GUI aplikacji
root = tk.Tk()
root.title("Konwerter plików")
root.geometry("300x200")

# Etykiety i pola wyboru
input_label = tk.Label(root, text="Wybierz format wejściowy i wyjściowy:")
input_label.pack(pady=10)

output_format_var = tk.StringVar()
output_format_var.set("Wybierz format")

# Menu rozwijane dla formatu wyjściowego
output_format_menu = tk.OptionMenu(root, output_format_var, "DOCX", "PNG", "JPG")
output_format_menu.pack(pady=5)

# Przycisk konwersji
convert_button = tk.Button(root, text="Konwertuj plik", command=convert_file)
convert_button.pack(pady=20)

# Przycisk zamknięcia
exit_button = tk.Button(root, text="Wyjdź", command=root.quit)
exit_button.pack(pady=5)

# Uruchomienie głównej pętli aplikacji
root.mainloop()
