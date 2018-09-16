import random
import numpy as np
from actions import Action
from gridlet import Gridlet

def create_gridlet():
    return Gridlet(1, 0.25, [1, 0, 0])

class Grid:
    def __init__(self, dimensions, p_organism):
        self.dimensions = dimensions
        self.num_cells = dimensions[0] * dimensions[1]
        self.cell_colour = np.array([0.1, 0.1, 0.1])

        self.gridlets = self.build_organisms(create_gridlet, p_organism)

    def place_creature(self, creature, p_organism):
        if random.uniform(0, 1) < p_organism:
            return creature()
        return None

    def build_organisms(self, creature, p_organism):
        return np.array([self.place_creature(creature, p_organism) for _ in range(self.num_cells)]) \
            .reshape(self.dimensions)

    def clear_dead_gridlets(self):
        self.gridlets = [[None if gridlet is None or gridlet.is_dead() else gridlet
                         for gridlet in row] for row in self.gridlets]

    def step(self):
        self.clear_dead_gridlets()
        for i, row in enumerate(self.gridlets):
            for j, gridlet in enumerate(row):
                if not gridlet:
                    continue
                curr_pos = np.array([i, j])
                new_pos = self.step_gridlet(gridlet, curr_pos)
                self.gridlets[curr_pos[0]][curr_pos[1]] = None
                self.gridlets[new_pos[0]][new_pos[1]] = gridlet

    def wrap_pos(self, pos):
        return np.array([max(min(pos[i], self.dimensions[i] - 1), 0) for i in [0, 1]])

    def get_cell(self, pos, orientation):
        pos_infront = self.wrap_pos(pos + np.array(orientation.value))
        cell_infront = self.gridlets[pos_infront[0]][pos_infront[1]]
        return pos_infront, cell_infront

    def move_gridlet(self, curr_pos, direction):
        pos_new, cell_new = self.get_cell(curr_pos, direction)
        return pos_new if not cell_new else curr_pos

    def step_gridlet(self, gridlet, curr_pos):
        action = gridlet.get_action()

        if action is Action.TURN_LEFT:
            gridlet.orientation = gridlet.orientation.left()
            return curr_pos
        if action is Action.TURN_RIGHT:
            gridlet.orientation = gridlet.orientation.right()
            return curr_pos

        if action is Action.MOVE_FORWARD:
            return self.move_gridlet(curr_pos, gridlet.orientation)
        if action is Action.MOVE_LEFT:
            return self.move_gridlet(curr_pos, gridlet.orientation.left())
        if action is Action.MOVE_RIGHT:
            return self.move_gridlet(curr_pos, gridlet.orientation.right())
        if action is Action.MOVE_BACKWARD:
            return self.move_gridlet(curr_pos, gridlet.orientation.behind())

        if action is Action.INSULT:
            _, cell_infront = self.get_cell(curr_pos, gridlet.orientation)
            if cell_infront:
                gridlet.insult(cell_infront)
            return curr_pos
        return curr_pos

    def start(self):
        while True:
            self.step()
