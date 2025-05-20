import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(1000,1100)
polygon = turtle.Turtle()
polygon.speed(0)
num_sides = 4
side_length = 50
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
