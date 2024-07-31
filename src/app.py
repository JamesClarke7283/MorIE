# src/app.py

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.core.morie import MorIE
from src.components.input_frame import InputFrame
from src.components.result_frame import ResultFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MorIE - Morality Inference Equation")
        self.geometry("900x900")

        self.morie = MorIE()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)

        self.input_frame = InputFrame(self, self.morie)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.result_frame = ResultFrame(self)
        self.result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=2, column=0, padx=10, pady=10)

    def calculate(self):
        try:
            self.input_frame.get_values()  # Update MorIE instance with current input values
            moral_value = self.morie.calculate()
            threshold = self.input_frame.get_threshold()
            
            result_text = self.morie.get_result_text(moral_value, threshold)
            
            self.result_frame.update_results(moral_value, result_text)
        except Exception as e:
            CTkMessagebox(title="Error", message=f"An error occurred: {str(e)}", icon="cancel")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()