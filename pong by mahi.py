import turtle
import winsound 
win = turtle.Screen()
win.title('pong by mahi')
win.bgcolor('brown')
win.setup(width = 800,height = 600)
win.tracer(0)

#score
score_a = 0
score_b = 0

#paddle A
Paddle_a = turtle.Turtle()
Paddle_a.speed(0)
Paddle_a.shape("square")
Paddle_a.color("white")
Paddle_a.shapesize(stretch_wid=5,stretch_len=1)
Paddle_a.penup()
Paddle_a.goto(-350,0)

#Paddle B
Paddle_b = turtle.Turtle()
Paddle_b.speed(0)
Paddle_b.shape("square")
Paddle_b.color("white")
Paddle_b.shapesize(stretch_wid=5,stretch_len=1)
Paddle_b.penup()
Paddle_b.goto(350,0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.09
ball.dy = -0.09

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))



#Function
def paddle_a_up():
    y = Paddle_a.ycor()
    y += 20
    Paddle_a.sety(y)

def paddle_a_down():
    y = Paddle_a.ycor()
    y -= 20
    Paddle_a.sety(y)

def paddle_b_up():
    y = Paddle_b.ycor()
    y += 20
    Paddle_b.sety(y)

def paddle_b_down():
    y = Paddle_b.ycor()
    y -= 20
    Paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")
#main loop
while True:
    win.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24, "normal"))

    #paddle collision
    if (ball.xcor() > 340 and ball.xcor() <350)and (ball.ycor() < Paddle_b.ycor() + 40 and ball.ycor()> Paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() >- 350)and (ball.ycor() < Paddle_a.ycor() + 40 and ball.ycor()> Paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
