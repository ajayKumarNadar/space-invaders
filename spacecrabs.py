from turtle import Turtle


class SpaceCrab(Turtle):
    def __init__(self, pos: tuple, shape: str):
        super().__init__()
        self.penup()
        self.shape(f"images/{shape}")
        self.goto(pos[0], pos[1])
        self.destroy = False
