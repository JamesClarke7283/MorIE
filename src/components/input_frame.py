# src/components/input_frame.py

import customtkinter as ctk
from src.components.spinbox import SpinBox

class InputFrame(ctk.CTkFrame):
    def __init__(self, master, morie):
        super().__init__(master)
        self.morie = morie

        self.grid_columnconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):
        questions = [
            "How good or bad was the intention? (I)",
            "How many direct effects did the action have? (N1)",
            "How many indirect effects did the action have? (N2)",
            "How many direct bad effects were there? (B1)",
            "How many indirect bad effects were there? (B2)",
            "How significant were the direct good effects? (DG(I))",
            "How significant were the indirect good effects? (IG(I))",
            "How significant were the direct bad effects? (DB(I))",
            "How significant were the indirect bad effects? (IB(I))"
        ]
        
        self.inputs = {}

        for i, question in enumerate(questions):
            if i == 0:  # Top slider
                ctk.CTkLabel(self, text=question, wraplength=300, justify="left").grid(row=i*2, column=0, padx=5, pady=5, sticky="w")
                slider = ctk.CTkSlider(self, from_=-1, to=1, number_of_steps=200, command=lambda value, q=question: self.update_value_label(q, value))
                slider.grid(row=i*2, column=1, padx=5, pady=5, sticky="ew")
                value_label = ctk.CTkLabel(self, text="0.00")
                value_label.grid(row=i*2, column=2, padx=5, pady=5)
                self.inputs[question] = {"widget": slider, "label": value_label}
            else:  # SpinBoxes
                ctk.CTkLabel(self, text=question, wraplength=300, justify="left").grid(row=i*2, column=0, padx=5, pady=5, sticky="w")
                spinbox = SpinBox(self, width=150, step_size=0.1)
                spinbox.grid(row=i*2, column=1, padx=5, pady=5, sticky="w")
                self.inputs[question] = {"widget": spinbox}

            # Separator (except after the last item)
            if i < len(questions) - 1:
                separator = ctk.CTkFrame(self, height=2, fg_color="gray30")
                separator.grid(row=i*2+1, column=0, columnspan=3, sticky="ew", padx=20, pady=5)

        # Bottom slider for threshold
        threshold_question = "What value threshold should it be to be seen as the bare minimum for it to be good?"
        ctk.CTkLabel(self, text=threshold_question, wraplength=300, justify="left").grid(row=len(questions)*2, column=0, padx=5, pady=20, sticky="w")
        threshold_slider = ctk.CTkSlider(self, from_=-10, to=10, number_of_steps=200, command=lambda value: self.update_value_label(threshold_question, value))
        threshold_slider.grid(row=len(questions)*2, column=1, padx=5, pady=20, sticky="ew")
        threshold_value_label = ctk.CTkLabel(self, text="0.00")
        threshold_value_label.grid(row=len(questions)*2, column=2, padx=5, pady=20)
        self.inputs[threshold_question] = {"widget": threshold_slider, "label": threshold_value_label}

    def update_value_label(self, question, value):
        if "label" in self.inputs[question]:
            self.inputs[question]["label"].configure(text=f"{value:.2f}")

    def get_values(self):
        for question, input_dict in self.inputs.items():
            value = input_dict["widget"].get()
            setattr(self.morie, question.split('(')[-1].strip(')').lower(), value)

    def get_threshold(self):
        threshold_question = "What value threshold should it be to be seen as the bare minimum for it to be good?"
        return self.inputs[threshold_question]["widget"].get()