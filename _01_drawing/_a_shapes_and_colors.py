import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
anagha = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
anagha.shape('turtle')
# Set your turtle's speed using .speed(2)
anagha.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
anagha.color('green')
anagha.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
anagha.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
anagha.left(90)
for i in range(4):
    anagha.left(90)
    anagha.forward(100)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
anagha.goto(5, 4)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
anagha.begin_fill()
anagha.circle(30, steps=30)
anagha.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!
anagha.begin_fill()
for i in range(2):
    anagha.right(90)
    anagha.forward(100)
    anagha.right(90)
    anagha.forward(200)
anagha.end_fill()

anagha.forward(60)

anagha.begin_fill()
anagha.circle(45, steps=30)
anagha.end_fill()

anagha.forward(60)

anagha.begin_fill()
anagha.circle(60, steps=30)
anagha.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
