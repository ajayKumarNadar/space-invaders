from turtle import Turtle


class SpaceCrab(Turtle):
    def __init__(self, pos: tuple, shape: str):
        super().__init__()
        self.penup()
        self.shape(f"images/{shape}")
        self.goto(pos[0], pos[1])
        self.destroy = False

    # for ufo in alien_ufo:
    #     time.sleep(0.03)
    #     if not ufo.destroy:
    #         for action_beam in beam_list:
    #             action_beam.forward(15)
    #             if action_beam.ycor() > 290:
    #                 action_beam.goto(spaceship.xcor(), -160)
    #                 action_beam.visible()
    #             if action_beam.beam:
    #                 if action_beam.hit(ufo.xcor(), ufo.ycor()):
    #                     ufo.destroy = True
    #                     ufo.shape(f"images/explosion.gif")
    #             if not ufo.destroy:
    #                 ufo.shape(f"images/spacecrab{int(number)}.gif")
    #                 if number:
    #                     number = False
    #                 else:
    #                     number = True
    #                 screen.update()
    #     else:
    #         ufo.hideturtle()

    # for action_beam in beam_list:
    #     print(1)
    #     action_beam.forward(15)
    #     print(action_beam.ycor())
    #     if action_beam.ycor() > 290:
    #         print(2)
    #         action_beam.goto(spaceship.xcor(), -160)
    #         action_beam.visible()
    #     for ufo in alien_ufo:
    #         if not ufo.destroy:
    #
    #             if action_beam.beam:
    #                 if action_beam.hit(ufo.xcor(), ufo.ycor()):
    #                     ufo.destroy = True
    #                     ufo.shape(f"images/explosion.gif")
    #             if not ufo.destroy:
    #                 ufo.shape(f"images/spacecrab{int(number)}.gif")
    #                 if number:
    #                     number = False
    #                 else:
    #                     number = True
    #                 screen.update()
    #         else:
    #             ufo.hideturtle()
