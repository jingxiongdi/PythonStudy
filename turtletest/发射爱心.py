#2.14
import turtle
import time


def go_to(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()

def head(x,y,r):
    go_to(x,y)
    turtle.speed(1)
    turtle.circle(r)
    leg(x,y)

def leg(x,y):

    turtle.right(90)
    turtle.forward(180)
    turtle.right(30)
    turtle.forward(100)
    turtle.left(120)
    go_to(x,y-180)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.left(120)
    hand(x,y)


def hand(x,y):
    go_to(x,y-60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    go_to(x, y - 90)
    turtle.right(60)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(60)
    eye(x,y)

def eye(x,y):
    go_to(x-50,y+130)
    turtle.right(90)
    turtle.forward(50)
    go_to(x+40,y+130)
    turtle.forward(50)
    turtle.left(90)


def big_Circle(size):
   turtle.speed(20)
   for i in range(150):
       turtle.forward(size)
       turtle.right(0.3)
def line(size):
   turtle.speed(1)
   turtle.forward(51*size)

def small_Circle(size):
   turtle.speed(10)
   for i in range(210):
       turtle.forward(size)
       turtle.right(0.786)



def heart(x, y, size):
   go_to(x, y)
   turtle.left(150)
   turtle.begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   turtle.left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   turtle.end_fill()

def main():
    turtle.pensize(2)
    turtle.color('red', 'pink')
    head(-120, 100, 100)
    heart(250, -80, 1)
    go_to(200, -300)
    turtle.write("To: 智慧与美貌并存的", move=True, align="left", font=("楷体", 20, "normal"))
    turtle.done()


main()
turtle.mainloop()
