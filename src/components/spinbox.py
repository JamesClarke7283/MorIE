# src/components/spinbox.py

import customtkinter as ctk

class SpinBox(ctk.CTkFrame):
    def __init__(self, *args, width=100, height=32, step_size=0.1, command=None, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                             command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, justify="center")
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                        command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, f"{value:.1f}")
            self.update_command()
        except ValueError:
            return

    def subtract_button_callback(self):
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, f"{value:.1f}")
            self.update_command()
        except ValueError:
            return

    def update_command(self):
        if self.command is not None:
            self.command()

    def get(self):
        try:
            return float(self.entry.get())
        except ValueError:
            return 0

    def set(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, f"{float(value):.1f}")