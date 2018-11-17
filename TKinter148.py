import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Hello World!")
my_label.grid(row=2, column=2)

# Start the GUI event loop
window.mainloop()
