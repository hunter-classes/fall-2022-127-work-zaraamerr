import turtle

def sample_function():
  print ("This is a function!")
  print ("This can be used multiple times.")
wn= turtle.Screen()

# create the first turtle
# into the variable crush
#and make crush draw a square

crush= turtle.Turtle()
crush.up()
crush.goto(100,100)
crush.down()

for i in range(4):
  crush.forward(50)
  crush.right(90)  
  
#create a second turtle
#into the variable squirt
#and make squirt draw a triangle

squirt= turtle.Turtle()

squirt.up()
squirt.goto(50,100)
squirt.down()
squirt.color("red")
squirt.width(5)

for i in range(3):
  squirt.forward(30)
  squirt.right(120)


sample_function()
wn.exitonclick()
wn.mainloop()
