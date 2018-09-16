from grid import Grid
from renderer import Renderer

if __name__ == "__main__":
    dimensions = (50, 50)
    p_gridlet = 0.1
    step_time = 1

    grid = Grid(dimensions, p_gridlet)
    renderer = Renderer(grid)
    renderer.start(step_time)