import turtle

def position_turtle(t,x,y,w,color):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()

def square(t,x,y,w,color,sidelen):
  """
  Parameters:
  t- a turtle
  x,y- location
  w- width of side
  color- color of drawing
  sidelen- length of each side
  Returns:
  nothing
  """
   # set the location, color, width of square
  position_turtle(t,x,y,w,color)
    # draw a square
  for i in range(4):
      t.forward(sidelen)
      t.right(90)

def triangle(t, x, y, w, color, sidelen):
  """
  Parameters:
  t- a turtle
  x,y- location
  w- width of side
  color- color of drawing
  sidelen- length of each side
  Returns:
  nothing
  """
   # set the location, color, width of triangle
  position_turtle(t,x,y,w,color)
   #draw a triangle
  for i in range(3):
    t.forward(sidelen)
    t.right(120)

def hexagon(t,x,y,w, color, sidelen):
  """
  Parameters:
  t- a turtle
  x,y- location
  w- width of side
  color- color of drawing
  sidelen- length of each side
  Returns:
  nothing
  """
   # set the location, color, width of hexagon
  position_turtle(t,x,y,w,color)
   # draw hexagon
  for i in range(6):
    t.forward(sidelen)
    t.right(60)

def ngon(t,numsides,x,y,w,color,sidelen):
  """
  Parameters:
  t- a turtle
  x,y- location
  w- width of side
  color- color of drawing
  sidelen- length of each side
  Returns:
  nothing
  """
   # set the location, color, width of ngon
  position_turtle(t,x,y,w,color)
   # draw any polygon
  for i in range(numsides):
    t.forward(sidelen)
    t.right(360/numsides)
    
wn=turtle.Screen()

crush = turtle.Turtle()

square(crush,0,20,1,"green",50)

squirt = turtle.Turtle()

#test trials

square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)

crush.setheading(45)
square(crush,150,30,2,"blue",60)

triangle(crush, 105, 105, 4, "green", 40)

hexagon(crush,-30,30,3,"brown", 60)

ngon(squirt,8, 150, 75,3, "pink", 40)
ngon(crush,5, -130, 74, 2, "light green", 30)
ngon(crush, 9, -130, 97, 3, "grey", 55)
ngon (crush, 10, -145, -60, 4, "purple", 40)

wn.exitonclick()
wn.mainloop()