import turtle
bars = turtle.Turtle()
data = [100,120,144,173]
def turtleProg(height):
    bars.left(90)
    bars.forward(height)
    bars.right(90)
    bars.forward(25)
    bars.right(90)
    bars.forward(height)
    bars.left(90)  

for num in data:
    turtleProg(num)
