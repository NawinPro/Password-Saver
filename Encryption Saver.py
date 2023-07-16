import tkinter as tk
import csv
from tkinter import filedialog, messagebox

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)

def save_password():
    file_name = file_entry.get()
    password = password_entry.get()

    if file_name == "":
        messagebox.showerror("Error", "Please choose a file.")
        return

    if password == "":
        messagebox.showerror("Error", "Please enter a password.")
        return

    # Open the CSV file and append the data
    with open(file_name + ".csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([file_name, password])

    messagebox.showinfo("Success", "Password saved successfully.")

# Create the main window
window = tk.Tk()
window.title("Password Saver")
window.configure(background="#333333")

# Create labels
file_label = tk.Label(window, text="File Name:", bg="#333333", fg="#ffffff")
file_label.grid(row=0, column=0, padx=10, pady=10)
password_label = tk.Label(window, text="Password:", bg="#333333", fg="#ffffff")
password_label.grid(row=1, column=0, padx=10, pady=10)

# Create entry fields
file_entry = tk.Entry(window)
file_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create choose file button
choose_file_button = tk.Button(window, text="Choose File", command=choose_file)
choose_file_button.grid(row=0, column=2, padx=10, pady=10)

# Create save button
save_button = tk.Button(window, text="Save", command=save_password)
save_button.grid(row=1, column=2, padx=10, pady=10)

# Run the main window loop
window.mainloop()
