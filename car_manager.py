from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            color = COLORS[random.randint(0,5)]
            car.color(color)
            car.shapesize(stretch_len=2)
            ypos = random.randint(-250,250)   
            car.penup()  
            car.goto(x=300,y=ypos)     
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        




