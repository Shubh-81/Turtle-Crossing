from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.left(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_pos(self):
        self.goto(STARTING_POSITION)
