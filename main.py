from turtle import Turtle, Screen
import paddle
import ball
import time
import score
import winsound
import pygame

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load('ConstSound.wav')
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))

balls = ball.Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

Scores= score.Score()
border1 = Turtle()
border1.pencolor("White")
border1.left(90)
while border1.ycor() < 230:
    border1.forward(10)
    border1.penup()
    border1.forward(10)
    border1.pendown()
    border1.forward(10)
border1.hideturtle()
border = Turtle()
border.pencolor("White")
border.right(90)
while border.ycor() > -250:
    border.forward(10)
    border.penup()
    border.forward(10)
    border.pendown()
    border.forward(10)
border.hideturtle()


game_is_on = True
while game_is_on:
    if balls.xcor() > 410:
        game_is_on = False
    else:
        screen.update()
        time.sleep(.1)
        balls.move()
        # print(f"Ball:{balls.pos()} paddle: {l_paddle.pos()}")
        # print(balls.distance(r_paddle))
        ##Code for bouncing Longer method(May contain some bugs)
        # up_collision = False
        # down_collision = 0
        # if balls.ycor() > 270:
        #     up_collision = True
        #     while up_collision:
        #         screen.update()
        #         time.sleep(.1)
        #         newX = balls.xcor() + 10
        #         newY = balls.ycor() - 10
        #         balls.goto(newX, newY)
        if balls.ycor() > 270 or balls.ycor() < -270:
            screen.update()
            time.sleep(.1)
            balls.bounce_y()
        if balls.distance(r_paddle) < 50 and balls.xcor() > 320:
            balls.bounce_x()
        elif balls.distance(l_paddle) <50 and balls.xcor() < -320:
            balls.bounce_x()
        if balls.xcor() >380:
            winsound.PlaySound('Boom.wav', winsound.SND_ASYNC)
            balls.reset_position()
            Scores.l_point()
            # score.Score().update_scoreboard()

        elif balls.xcor() < -380:
            winsound.PlaySound('Boom.wav', winsound.SND_ASYNC)
            balls.reset_position()
            Scores.r_point()
            # score.Score().update_scoreboard()

screen.exitonclick()
