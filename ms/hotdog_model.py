import random

class HotdogModel():
    def predict(self, X=[1, 0]):
        return random.choice([0, 1])