import turtle
import random

# Setup the window
wn = turtle.Screen()
wn.title("Bricks Game homework ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0, -250)
paddle.dx = 2

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
brick_width = 60
brick_height = 20
rows = 6
cols = 12

for row in range(rows):
    for col in range(cols):
        brick = turtle.Turtle()
        brick.speed(20)
        brick.shape("square")
        brick.color(colors[row % len(colors)])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-290 + col * (brick_width + 5), 250 - row * (brick_height + 5))
        bricks.append(brick)

# Score
score = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddle left
def paddle_left():
    x = paddle.xcor()
    if x > -300:
        x -= 50
    paddle.setx(x)

# Function to move paddle right
def paddle_right():
    x = paddle.xcor()
    if x < 300:
        x += 50
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
    
    if ball.ycor() < -250:
        ball.goto(0, 0)
        ball.dy *= -1
    
    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1
    
    if ball.xcor() < -350:
        ball.setx(-350)
        ball.dx *= -1
    
    # Paddle and ball collision
    if (ball.dy < 0 and paddle.ycor() - 10 < ball.ycor() < paddle.ycor() + 10 and
            paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(paddle.ycor() + 10)
        ball.dy *= -1
    
    # Ball and brick collisions
    for brick in bricks:
        if brick.isvisible() and brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10 and \
                brick.xcor() - 30 < ball.xcor() < brick.xcor() + 30:
            ball.dy *= -1
            brick.hideturtle()
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Game over when the ball hits the bottom of the screen
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dx = 0.15
        ball.dy = -0.15
        for brick in bricks:
            brick.showturtle()
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
