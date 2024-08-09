import turtle
import random

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=200)
screen.title("1D Random Walk")
screen.setworldcoordinates(-300, -50, 300, 50)

# Create a Turtle for the walker
walker = turtle.Turtle()
walker.penup()
walker.speed(0)  # Fastest animation speed

# Define parameters
num_steps = 1000000  # Number of steps in the random walk

# Perform the random walk
for _ in range(num_steps):
    # Randomly choose the direction of the step
    direction = random.choice([-1, 1])
    # Move the walker
    walker.setheading(0 if direction == 1 else 180)  # Face right (0) or left (180)
    walker.pendown()
    walker.forward(10)  # Move forward by 10 units (adjust as needed for visualization)
    walker.penup()

# Keep the window open until manually closed
screen.mainloop()
