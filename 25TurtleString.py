
#Author:    Katherine St. John
#Date:      August 2014
#A program that uses command strings to control turtle drawing
#Modified by:  !YourNameHere!
#Date:      !DateYouModifiedTheProgram!

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'B':            #move forward
        tess.backward(50)
    elif ch == 'l':          #turn left
        tess.left(45)
    elif ch == 'r':          #turn right
        tess.right(45)
    elif ch == 'p':          #lift pen
        tess.pencolor("purple")
    elif ch == 'S':          #lower pen
        tess.stamp()
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", c)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked

