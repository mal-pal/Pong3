import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wnTopLine = 300
wnBottomLine = -300
wnRightLine = 400
wnLeftLine = -400
wn.setup(width = 800, height = 600) #00 is in the center, up +300, down=300, left -400, right +400
wn.tracer(0) #stops the window from updating, so you manually update. Inc speed of game

# Create Paddle A -Left
paddle_a= turtle.Turtle()
paddle_a.speed(0) #speed of animation, set max possible. Not the speed of movement.
paddle_a.shape("square")
paddle_a.color("indian red")
#defalt shape is 20 pixels by 20 pixels
paddle_a.shapesize(stretch_wid = 5, stretch_len= 1) #factors to basic 20x20
paddle_a.penup() #Turtles draw a line, but we don't want that, so pen is up aka not drawing
paddle_a.goto(-350, 0) #set starting location

# Create Paddle B -Right
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("cornflower blue")
paddle_b.shapesize(stretch_wid = 5, stretch_len= 1) #100 tall x 20 wide
paddle_b.penup()
paddle_b.goto(350, 0)

paddle_len = 100


# Create Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("thistle")
ball.penup()
ball.goto(0, 0)
ball.dx = .02  # delta of x
ball.dy = .02  # move n pixels. play with value to change speed - depends on your compt speed

# Functions

def paddle_a_up():
    y = paddle_a.ycor()  # ycor() returns y-coordinate
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()  # ycor() returns y-coordinate
    y += -20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()  # ycor() returns y-coordinate
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()  # ycor() returns y-coordinate
    y += -20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() #tells window to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when user pressed w, call function paddle_a_up()
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")







#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
        # compare ball's y-coor with window boundary
    if ball.ycor() > (wnTopLine - 10): #if within 10 pixels of top edge reverse direction
        ball.sety(wnTopLine - 10)
        ball.dy = ball.dy * -1
    if ball.ycor() < (wnBottomLine + 10): #if within 10 pixels of top edge reverse direction
        ball.sety(wnBottomLine + 10)
        ball.dy = ball.dy * -1
    if ball.xcor() > (wnRightLine -10):
        ball.goto(0,0)
    if ball.xcor() < (wnLeftLine +10):
        ball.goto(0,0)

    # Paddle and ball collisions
    if (ball.xcor() > (paddle_b.xcor() - 10)) and (ball.ycor() < (paddle_b.ycor()+(paddle_len/2))) and (ball.ycor() > (paddle_b.ycor() - (paddle_len/2))):
        ball.goto(paddle_b.xcor() -25, ball.ycor())
        ball.dx = ball.dx * -1
    if (ball.xcor() < (paddle_a.xcor() + 10)) and (ball.ycor() < (paddle_a.ycor() + (paddle_len / 2))) and (ball.ycor() > (paddle_a.ycor() - (paddle_len / 2))):
        ball.goto(paddle_a.xcor() + 25, ball.ycor())
        ball.dx = ball.dx * -1