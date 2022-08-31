import turtle

t = turtle.Turtle()
t.speed(10)

def square(length, count):
  for i in range(count):
    for i in range(4):
      t.forward(length)
      t.left(90)
    t.penup()
    t.forward(length + 50)
    t.pendown()

square(100, 3)

turtle.mainloop()
turtle.bye()