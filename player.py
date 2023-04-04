from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start_player()

    def start_player(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)


    def next_level(self):
        self.start_player()

    def is_player_crossed(self):
        if self.ycor() > 280:
            return True
        else:
            return False


