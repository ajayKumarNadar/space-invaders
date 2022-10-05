from turtle import Turtle


class ActionBeam(Turtle):
    def __init__(self, x, y):
        super().__init__("square")
        self.penup()
        self.hideturtle()
        self.shapesize(0.3, 1)
        self.color("yellow")
        self.setheading(90)
        self.pencolor(255, 0, 0)
        self.goto(x, y)
        self.beam = False

    def visible(self):
        self.beam = True
        self.showturtle()

    def hit(self, x, y):
        if self.xcor() - 25 < x < self.xcor() + 25:
            if self.ycor() + 40 >= y:
                self.beam = False
                self.hideturtle()
                return True
            else:
                return False
        else:
            return False
