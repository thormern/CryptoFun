class Balance:
    def __init__(self, dict):
        self.asset = dict["asset"]
        self.free = dict["free"]
        self.locked = dict["locked"]