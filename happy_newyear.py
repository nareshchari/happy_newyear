import random
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.speed(0)

screen.title("Happy New Year!!")
t.color("yellow")
def draw_star():
    turns =5
    t.begin_fill()
    while turns >0:
        t.forward(25)
        t.left(145)
        turns=turns-1
    t.end_fill()
num_stars = 0
while num_stars <80:
    x=random.randint(-700,700)
    y=random.randint(-700,700)
    draw_star()
    t.penup()
    t.goto(x,y)
    t.pendown()
    num_stars = num_stars+1

for i in range(10):
    x= random.randint(-700, 500)
    y= random.randint(-300, 100)

    t.penup()
    t.goto(x,y)
    t.pendown()
    size = random.randint(50,200)
    ls=["yellow","red","blue","green","purple","grey","orange","pink","magenta","brown","royalblue"]
    r = random.choice(ls)
    t.color(r)

    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)

t.penup()
t.setposition(-300,200)
t.pendown()
t.write("Happy",font=("Arial",80))
t.penup()
t.setposition(150,200)
t.pendown()
t.write("New Year!!",font=("Arial",80))
t.penup()
t.pendown()

t.hideturtle()

screen.exitonclick()
