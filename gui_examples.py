#####################################################################
############### Name : Sheryl Muthoni ###############################
############### Topic : GUI interface ###############################
############### Date  :  07/06/2022 #################################
#####################################################################

from tkinter import *

window =Tk()
window.title("My awesome app :)")

window.configure(bg="cyan")#configuring the background


window.geometry("400x400")#this is the default size


lbl= Label (window,text="Welcome new user!!!",font=("Rage italic",50))
f_name = Label ( window , text = "First name",font=("Vivaldi",50))
s_name = Label (window , text = "Second name",font=("Vivaldi",50))
 
lbl.grid(column= 20 , row = 20)
f_name.grid(column = 60 ,row =100)
s_name.grid(column= 60 , row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up window")
    top.configure(bg="green")
    msg = Label(top,text ="Welcome to this new app",font=("Mistral 18"), command=open_popup().pack())



btn= Button( window , text = "Click the button",bg="blue",fg="red",font="Mistral")
btn.grid(column= 100,row = 180)

f_name_box= Entry(window ,width=20)
f_name_box.grid(column = 100, row = 100)

s_name_box= Entry(window,width = 20)
s_name_box.grid ( column = 100 , row =120)



window.mainloop()



