import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Renderer:
    def __init__(self, grid):
        self.fig = plt.figure()
        self.grid = grid
        self.im = plt.imshow(self.get_grid_image(), animated=True)

    def update_grid_image(self, _):
        self.im.set_array(self.get_grid_image())
        return self.im,

    def get_colour(self, organism):
        return self.grid.cell_colour if organism is None else organism.colour

    def get_grid_image(self):
        self.grid.step()
        return [[self.get_colour(cell) for cell in row] for row in self.grid.gridlets]

    def start(self, step_time):
        self.ani = animation.FuncAnimation(self.fig, self.update_grid_image, interval=step_time, blit=True)
        plt.show()