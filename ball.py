from turtle import Turtle,Screen
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(2)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX,newY)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)