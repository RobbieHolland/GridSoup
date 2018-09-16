class Organism():
    def __init__(self, ego, insult_strength, colour):
        self.ego = ego
        self.insult_strength = insult_strength
        self.colour = colour

    def insult(self, recipient):
        recipient.ego -= self.insult_strength
        self.ego += self.insult_strength

    def is_dead(self):
        return self.ego < 0