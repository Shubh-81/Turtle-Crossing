from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(y=270,x=50)
        self.update_board()
        

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
    
    def show_game_over(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write(f"Game Over",align="center",font=FONT)
