import tkinter as ui
import time

window = ui.Tk()

def update_clock():
    hours = time.strftime ("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":"+ minutes + ":" + seconds + ":" + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000,update_clock)


digital_clock_lbl= ui.Label(window, text = "00:00:00",font="Helvetica 72 bold")

digital_clock_lbl.pack()

update_clock()

import turtle
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Simple Analog Clock")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock (pen):
    pen.up()
    pen.goto(0,210)
    pen.setheading(100)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    pen.penup(0,0)
    pen.setheading(90)
    

    for _ in range(17):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(38)


    


draw_clock(pen)   














wn.mainloop()


window.mainloop()