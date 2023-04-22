import turtle
import random


player_one = turtle.Turtle() # makes first turtle
player_two = turtle.Turtle() #makes second turtle.
circle1 = turtle.Turtle() #makes first circle
circle2 = turtle.Turtle() #makes second circle


#change color of turtle to green and blue
player_one.color("green")
player_two.color("blue")


#makes each player into a turtle shape using the turtle.shape() method
player_one.shape("turtle")
player_two.shape("turtle")


#makes sure the turtle doesn't draw a line when its moving to a new position
player_one.penup()
player_two.penup()


#moves the turtle to the edge of the screen.
player_one.goto(-200,-100)
player_two.goto(-200,100)


#moves to position to draw circle
circle1.penup()
circle2.penup()
circle1.goto(300,60)
circle2.goto(300,-140)


#draws circle shape
circle1.pendown()
circle2.pendown()
circle1.circle(40) #40 is the radius in pixels
circle2.circle(40)


#creates a die
die = [10,20,30,40,50,60]


for i in range(20):
   #Step 1: Check to see if the turtle has reached the circle.
   if turtle.pos == circle1.pos:
      
   #(add an if and elif statement)

   #Step 2: if they havent reached the circle enter the else block that allows the turtle to race.
   #in each iteration, "roll the die" by randomly picking a number from the die list.
  
   #Step 3: make each turtle move forward by the number rolled in the die list.