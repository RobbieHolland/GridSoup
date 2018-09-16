from organism import Organism
from orientation import Orientation
from actions import Action
import random

class Gridlet(Organism):
    """Vision: [1, 0] -> Forward 1, Right 0"""

    def __init__(self, ego, insult_strength, colour):
        Organism.__init__(self, ego, insult_strength, colour)
        self.vision = [[1, 0]]
        self.orientation = random.choice(list(Orientation))

    def get_action(self):
        return random.choice(list(Action))