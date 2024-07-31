# src/components/result_frame.py

import customtkinter as ctk

class ResultFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.moral_value_label = ctk.CTkLabel(self, text="Moral Value: ", font=("Arial", 16, "bold"))
        self.moral_value_label.grid(row=0, column=0, padx=5, pady=5)

        self.result_label = ctk.CTkLabel(self, text="Result: ", font=("Arial", 16, "bold"))
        self.result_label.grid(row=1, column=0, padx=5, pady=5)

    def update_results(self, moral_value, result_text):
        self.moral_value_label.configure(text=f"Moral Value: {moral_value:.2f}")
        self.result_label.configure(text=f"Result: {result_text}")