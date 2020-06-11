import turtle
bars = turtle.Turtle()
bars.color("blue")
data = [100,120,144,173] #increments of 20%
def turtleProg(height):
    bars.left(90)         #face upward
    bars.forward(height)   #go as high has number in the data list
    bars.right(90)         #turn right
    bars.forward(25)       #creates the thickness of the graph
    bars.right(90)         #turn right 
    bars.forward(height)   #go down the same number as line 6
    bars.left(90)  
#Every number in the data list will replace height one by one, hence making the bar graph.
for num in data:
    turtleProg(num)
