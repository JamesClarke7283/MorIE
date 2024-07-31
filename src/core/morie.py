from .logging import setup_logger

logger = setup_logger(__name__)

class MorIE:
    def __init__(self):
        self.reset()
        logger.info("MorIE instance created")

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
        logger.debug("MorIE instance reset")

    def calculate(self):
        logger.info("Starting moral value calculation")
        
        # Step 1: Calculate C and C2
        c = self.n1 - self.b1
        c2 = self.n2 - self.b2
        logger.debug(f"C = {c}, C2 = {c2}")

        # Step 2: Calculate DG(F), IG(F), DB(F), and IB(F)
        dg_f = self.dg_i * c
        ig_f = self.ig_i * c2
        db_f = self.db_i * self.b1
        ib_f = self.ib_i * self.b2
        logger.debug(f"DG(F) = {dg_f}, IG(F) = {ig_f}, DB(F) = {db_f}, IB(F) = {ib_f}")

        # Step 3: Calculate total good and total bad
        total_good = dg_f + ig_f
        total_bad = db_f + ib_f
        logger.debug(f"Total good = {total_good}, Total bad = {total_bad}")

        # Step 4: Calculate moral value
        moral_value = self.intent + total_good + total_bad
        logger.info(f"Calculated moral value: {moral_value}")

        return moral_value

    def get_result_text(self, moral_value, threshold=0):
        if moral_value == 0:
            result = "NEUTRAL"
        elif moral_value > threshold:
            result = "NET POSITIVE"
        else:
            result = "NET NEGATIVE"
        logger.info(f"Result text for moral value {moral_value}: {result}")
        return result

    def get_scale_position(self, moral_value, min_value=-10, max_value=10):
        position = (moral_value - min_value) / (max_value - min_value)
        logger.debug(f"Scale position for moral value {moral_value}: {position}")
        return position