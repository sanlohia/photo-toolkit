import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Set theme
ctk.set_appearance_mode("dark")   # "light" bhi try kar sakte ho
ctk.set_default_color_theme("blue")

def browse_folder(entry):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, "end")
        entry.insert(0, folder_selected)

def copy_selected():
    folder1 = entry_highres.get()
    folder2 = entry_lowres.get()
    folder3 = entry_output.get()

    if not (os.path.isdir(folder1) and os.path.isdir(folder2) and os.path.isdir(folder3)):
        messagebox.showerror("Error", "Please select valid folders")
        return

    copied_files = 0
    for file_name in os.listdir(folder2):
        source_file = os.path.join(folder1, file_name)
        if os.path.exists(source_file):
            shutil.copy(source_file, folder3)
            copied_files += 1

    messagebox.showinfo("Done", f"Copied {copied_files} files to {folder3}")

# Main Window
root = ctk.CTk()
root.title("Photo Toolkit - Copy Selected High-Res")
root.geometry("900x350")

# Grid config (expand properly)
root.grid_columnconfigure(1, weight=1)

# -------- High Res Folder --------
label_highres = ctk.CTkLabel(root, text="High-Res Folder:", font=("Arial", 14))
label_highres.grid(row=0, column=0, padx=20, pady=20, sticky="w")

entry_highres = ctk.CTkEntry(root, width=500, font=("Arial", 12))
entry_highres.grid(row=0, column=1, padx=10, sticky="ew")
button_highres = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(entry_highres))
button_highres.grid(row=0, column=2, padx=10)

# -------- Low Res Folder --------
label_lowres = ctk.CTkLabel(root, text="Low-Res Folder:", font=("Arial", 14))
label_lowres.grid(row=1, column=0, padx=20, pady=20, sticky="w")

entry_lowres = ctk.CTkEntry(root, width=500, font=("Arial", 12))
entry_lowres.grid(row=1, column=1, padx=10, sticky="ew")
button_lowres = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(entry_lowres))
button_lowres.grid(row=1, column=2, padx=10)

# -------- Output Folder --------
label_output = ctk.CTkLabel(root, text="Output Folder:", font=("Arial", 14))
label_output.grid(row=2, column=0, padx=20, pady=20, sticky="w")

entry_output = ctk.CTkEntry(root, width=500, font=("Arial", 12))
entry_output.grid(row=2, column=1, padx=10, sticky="ew")
button_output = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(entry_output))
button_output.grid(row=2, column=2, padx=10)

# -------- Run Button --------
run_button = ctk.CTkButton(root, text="Run Copy", command=copy_selected, fg_color="green", font=("Arial", 16, "bold"))
run_button.grid(row=3, column=0, columnspan=3, pady=40)

root.mainloop()
