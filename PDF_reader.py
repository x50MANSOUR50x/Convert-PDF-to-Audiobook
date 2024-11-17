import time
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import messagebox
import os

class PDF_READER():
    def __init__(self):
        self.program = TkinterDnD.Tk()
        self.program.minsize(width=400, height=300)
        self.program.title("PDF Reader")

        self.welcome_label = tk.Label(self.program, text="Welcome to PDF Reader App :)", font=("Arial", 14, "bold"), padx=10, pady=10)
        self.welcome_label.place(x=50, y=0)

        self.label = tk.Label(self.program, text="Drag a PDF file here to see its absolute path", font=("Arial", 10, "bold"), padx=3, pady=3, wraplength=300)
        self.label.place(x=55, y=150)

        self.program.drop_target_register(DND_FILES)
        self.program.dnd_bind('<<Drop>>', self.on_drop)

        self.program.mainloop()

    def on_drop(self, event):
        self.file_path = event.data

        if os.path.isfile(self.file_path):
            if self.file_path.lower().endswith(".pdf"):
                abs_path = os.path.abspath(self.file_path)
                self.label.config(text=f"Absolute Path:\n{abs_path}")
                messagebox.showinfo("PDF Loaded", f"PDF loaded from:\n{abs_path}")
                time.sleep(3)
                self.program.destroy()
            else:
                self.label.config(text="Please drop a valid PDF file.")
        else:
            self.label.config(text="Please drop a valid file.")

