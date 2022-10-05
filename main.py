from turtle import Screen, Turtle
from tkinter import TclError
from spacecrabs import SpaceCrab
from beams import ActionBeam
from message import Message
import time

game_over = False
game_on = True
level = 0

while game_on and level <= 5:
    level += 1
    screen = Screen()
    screen.listen()
    screen.tracer(0)

    # ---- Screen Setup ---- #
    screen.setup(height=600, width=800)
    screen.title("Space Invaders")
    screen.bgcolor("black")
    try:
        screen.bgpic("images/bg-stars.gif")
    except TclError:
        screen.bgcolor("black")
    screen.colormode(255)
    # screen.bgpic("images/bg.gif")

    # ---- Add New Shapes ---- #
    screen.addshape("images/spaceship64.gif")
    screen.addshape("images/spacecrab1.gif")
    screen.addshape("images/spacecrab0.gif")
    screen.addshape("images/explosion.gif")

    # ---- Player Spaceship ---- #
    spaceship = Turtle()
    spaceship.penup()
    spaceship.shape("images/spaceship64.gif")
    spaceship.goto(0, -200)

    # ---- Move Spaceship with Mouse ---- #
    def move_spaceship(x_val, y_val):
        if -380 < x_val < 380:
            spaceship.goto(x_val, -200)


    def move_left():
        x_val, y_val = spaceship.pos()
        if x_val > -380:
            x_val -= 10
            spaceship.goto(x_val, -200)


    def move_right():
        x_val, y_val = spaceship.pos()
        if x_val < 380:
            x_val += 10
            spaceship.goto(x_val, -200)


    spaceship.ondrag(move_spaceship)
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")

    # ---- SpaceCrabs ---- #
    x, y = 350, 260
    alien_ufo = []
    for line in range(level):
        for num in range(11):
            alien_ufo.append(SpaceCrab(pos=(x, y), shape="spacecrab1.gif"))
            time.sleep(0.05)
            screen.update()
            x -= 70
        x = 350
        y -= 70

    # ---- Action Beam ---- #
    beam_list = []
    y = -160
    for num in range(level):
        action_beam = ActionBeam(x=0, y=y)
        y += 450 / level
        beam_list.append(action_beam)

    # ---- GAME ---- #
    level_on = True
    number = False
    sec = 3
    on_time = time.time() + sec
    while level_on:
        n = 0
        for ufo in alien_ufo:
            if not ufo.destroy:
                n += 1
                ufo.shape(f"images/spacecrab{int(number)}.gif")
                if number:
                    number = False
                else:
                    number = True
            else:
                ufo.hideturtle()
        if time.time() >= on_time:
            for ufo in alien_ufo:
                ufo.goto(ufo.xcor(), ufo.ycor() - 30)
                if not ufo.destroy and ufo.ycor() - 30 < -190:
                    level_on = False
                    game_on = False
                    game_over = True

            on_time = time.time() + sec
        screen.update()
        if n == 0:
            level_on = False

        for action_beam in beam_list:
            action_beam.forward(15)
            if action_beam.ycor() > 290:
                action_beam.goto(spaceship.xcor(), -160)
                action_beam.visible()

        for action_beam in beam_list:
            for ufo in alien_ufo:
                if not ufo.destroy and action_beam.beam:
                    if action_beam.hit(ufo.xcor(), ufo.ycor()):
                        ufo.destroy = True
                        ufo.shape(f"images/explosion.gif")
                        action_beam.beam = False
                        action_beam.hideturtle()

        time.sleep(0.01)
        screen.update()
    screen.clear()

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Space Invaders")
try:
    screen.bgpic("images/bg-stars.gif")
except TclError:
    screen.bgcolor("black")
tk = Message()

if game_over:
    tk.game_over()
else:
    tk.you_won()

screen.exitonclick()
