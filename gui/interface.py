import tkinter as tk
from tkinter import ttk, messagebox
from config.styles import configure_styles
from core.autopress import AutoPressController


class AutoPressUI:
    def __init__(self, root):
        configure_styles()
        self.root = root
        self.controller = AutoPressController(self.update_status)
        self.setup_ui()

    def setup_ui(self):
        self.root.title("AutoPress")
        self.root.geometry("400x250")

        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Название окна:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.window_entry = ttk.Entry(main_frame, width=30)
        self.window_entry.grid(row=0, column=1, padx=5, pady=5)
        self.window_entry.insert(0, 'Genshin Impact')

        ttk.Label(main_frame, text="Клавиша:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.key_entry = ttk.Entry(main_frame, width=5)
        self.key_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.key_entry.insert(0, 'F')

        ttk.Label(main_frame, text="Интервал (сек):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.interval_entry = ttk.Entry(main_frame, width=5)
        self.interval_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.interval_entry.insert(0, '0.2')

        self.control_btn = ttk.Button(main_frame, text="Старт", command=self.toggle_auto_press, style='Start.TButton')
        self.control_btn.grid(row=3, column=0, columnspan=2, pady=15)

        self.status_var = tk.StringVar(value="Готов к работе")
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=4, column=0, columnspan=2)

    def toggle_auto_press(self):
        if self.controller.is_running:
            self.controller.stop()
            self.control_btn.config(text="Старт", style='Start.TButton')
        else:
            params = {
                'window_title': self.window_entry.get(),
                'key': self.key_entry.get().lower(),
                'interval': self.interval_entry.get()
            }
            errors = self.controller.validate(params)
            if errors:
                messagebox.showerror("Ошибка", "\n".join(errors))
            else:
                self.controller.start(params)
                self.control_btn.config(text="Стоп", style='Stop.TButton')

    def update_status(self, message):
        self.status_var.set(message)