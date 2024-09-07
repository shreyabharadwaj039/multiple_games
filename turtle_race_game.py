from turtle import Turtle ,Screen
import random

screen= Screen()
screen.setup(width=500,height=400)
choice= screen.textinput(title="Make your bet",prompt="Which Turtle will win? Enter a colour: ")
y_position=[-70,-40,-10,20,50,80]
colour=["red","orange","yellow","green","blue","purple"]
flag=False
all=[]
for i in range(0,6):
  new_turtle= Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.goto(x=-240,y=y_position[i])
  new_turtle.color(colour[i])
  all.append(new_turtle)

if choice:
  flag=True
  
while flag==True:
  for turtle in all:
    if turtle.xcor()>240:
      flag=False
      win_colour=turtle.pencolor()
      if win_colour==choice:
        print("YOU WIN!!")
      else:
        print("you lost")
    random_distance=random.randint(0,10)
    turtle.forward(random_distance)
    
screen.exitonclick()

