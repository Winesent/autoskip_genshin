from tkinter import ttk


def configure_styles():
    style = ttk.Style()
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
    style.configure('TButton', font=('Arial', 10), padding=5)
    style.configure('TEntry', font=('Arial', 10), padding=5)
    style.configure('Start.TButton', foreground='white', background='#4CAF50')
    style.configure('Stop.TButton', foreground='white', background='#F44336')