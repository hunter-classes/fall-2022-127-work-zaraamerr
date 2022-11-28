import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()

# move turtle forward on the screen to capture the entire path on the screen
pirate.penup()
pirate.forward(100)

# the drunk pirate's path
pirate.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
  # positive angles are counterclockwise and
  # negative angles are clockwise
    pirate.left(angle)
    pirate.forward(100)

# the current heading of the drunk pirate
print("The drunk pirate's final heading was", pirate.heading())

wn.exitonclick()