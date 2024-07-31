# src/core/morie.py

class MorIE:
    def __init__(self):
        self.reset()

    def reset(self):
        self.intent = 0
        self.n1 = 0
        self.n2 = 0
        self.b1 = 0
        self.b2 = 0
        self.dg_i = 0
        self.ig_i = 0
        self.db_i = 0
        self.ib_i = 0

    def calculate(self):
        db_f = self.db_i * self.b1
        ib_f = self.ib_i * self.b2
        dg_f = self.dg_i * (self.n1 - self.b1)
        ig_f = self.ig_i * (self.n2 - self.b2)

        moral_value = self.intent + (dg_f - db_f) + (ig_f - ib_f)
        return moral_value

    def get_result_text(self, moral_value, threshold):
        if moral_value > threshold:
            return "NET POSITIVE"
        elif moral_value < threshold:
            return "NET NEGATIVE"
        else:
            return "NEUTRAL"

    def get_scale_position(self, moral_value, min_value=-10, max_value=10):
        return (moral_value - min_value) / (max_value - min_value)