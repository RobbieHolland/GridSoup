from enum import Enum

class Orientation(Enum):
    NORTH = [0, 1]
    EAST = [1, 0]
    SOUTH = [0, -1]
    WEST = [-1, 0]

    def left(self):
        return self.turn(-1)

    def right(self):
        return self.turn(1)

    def behind(self):
        return self.turn(2)

    def turn(self, direction):
        return os[(os.index(self) + direction) % len(os)]

os = list(Orientation)
