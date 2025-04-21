import random
from tkinter import Tk, ttk, messagebox

root = Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

password_length = tk.StringVar()
generated_password = tk.StringVar()

input_frame = ttk.LabelFrame(root, text="Settings")
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Password Length:").grid(row=0, column=0)
Entry = ttk.Entry(input_frame, textvariable=password_length).grid(row=0, column=1)

include_numbers = tk.BooleanVar()
tk.Checkbutton(input_frame, text="Include Numbers", variable=include_numbers).grid(row=1, column=0, sticky=tk.W)
include_letters = tk.BooleanVar()
tk.Checkbutton(input_frame, text="Include Letters", variable=include_letters).grid(row=1, column=1, sticky=tk.W)
include_symbols = tk.BooleanVar()
tk.Checkbutton(input_frame, text="Include Symbols", variable=include_symbols).grid(row=1, column=2, sticky=tk.W)

def generate_password():
    characters = []
    if include_numbers.get():
        characters.extend(list('0123456789'))
    if include_letters.get():
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
    if include_symbols.get():
        characters.extend(list('!@#$%^&*()_+{}[];:?><,./`~'))
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    try:
        length = int(password_length.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
