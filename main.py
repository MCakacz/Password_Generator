import tkinter as tk
import tkinter.messagebox as messagebox
import random
import string

def generate_password():
    special_characters = "!@#$%^&*()_-+=<>?/"
    use_special = special_var.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    
    password_length_str = length_var.get()
    
    # Sprawdź, czy długość hasła zawiera tylko cyfry
    if not password_length_str.isdigit():
        messagebox.showerror("Błąd", "Długość hasła musi być liczbą całkowitą.")
        return
    
    password_length = int(password_length_str)
    
    if not use_special and not use_letters and not use_numbers:
        result.set("Wybierz co najmniej jedną opcję (specjalne/litery/cyfry)")
        return
    
    all_chars = ""
    if use_special:
        all_chars += special_characters
    if use_letters:
        all_chars += string.ascii_letters
    if use_numbers:
        all_chars += string.digits
    
    if len(all_chars) == 0:
        result.set("Brak dostępnych znaków do generowania hasła.")
        return
    
    password = ''.join(random.choice(all_chars) for _ in range(password_length))
    result.set(password)

# Inicjalizacja GUI
root = tk.Tk()
root.title("Generator Hasła")
root.geometry("500x300")

# Zmienna wynikowa - definiuj po utworzeniu głównego okna
result = tk.StringVar()

# Ustawienie okna na środku ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2
y = (screen_height - 300) // 2
root.geometry(f"500x300+{x}+{y}")

# Górna ramka na checkboxy i pole do wprowadzenia długości hasła
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Checkboxy do wyboru opcji
special_var = tk.BooleanVar()
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()

special_checkbox = tk.Checkbutton(top_frame, text="Specjalne znaki", variable=special_var)
letters_checkbox = tk.Checkbutton(top_frame, text="Litery", variable=letters_var)
numbers_checkbox = tk.Checkbutton(top_frame, text="Cyfry", variable=numbers_var)

special_checkbox.pack(side=tk.LEFT)
letters_checkbox.pack(side=tk.LEFT)
numbers_checkbox.pack(side=tk.LEFT)

# Długość hasła
length_label = tk.Label(top_frame, text="Długość hasła:")
length_label.pack(side=tk.LEFT)
length_var = tk.Entry(top_frame)
length_var.pack(side=tk.LEFT)

# Dolna ramka na pole tekstowe z hasłem
bottom_frame = tk.Frame(root)
bottom_frame.pack(expand=True, fill='both')

# Przycisk generowania hasła
generate_button = tk.Button(root, text="Generuj Hasło", command=generate_password)
generate_button.pack()

# Pole tekstowe do wyświetlania hasła (w dolnej ramce)
password_display = tk.Entry(bottom_frame, textvariable=result, state='readonly')
password_display.pack(expand=True, fill='both')

root.mainloop()
