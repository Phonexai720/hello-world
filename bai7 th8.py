import tkinter

import ramdom

colours =['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']

score =0

timeleft =30

def startGame(evnt):

    if timeleft ==30:

        countdown()

        nextColour()

def nextColour():

    global score

    global timeleft

    if timeleft>0:

        e.focus_set()

        if e.get().lower()==colours[1].lower():

            score+=1

        e.delete(0, tkinter.END)

        ramdom.shuffle(colours)

        label.config(fg=str(colours[1], text = str(colours[0]))

        scoreLabel.config(text="Score: "+str(score))

def countdown():

    global timeleft

    if timeleft>0:

        timeleft-=1

        timelabel.config(text="Time left:" + str(timeleft))

        timeLabel.after(1000, countdown)

root=tkinter.Tk()

root.title("COLORGAME")

toot.geometry("375*200")

instructions=tkinter.LAbel(root,text="type in the colour"

                           font=('helvetica'12))

instructions.pack()

label.pack()

e=tkinter.Entry(root)

root.bind('<Return>', startGame)

e.pack()

e.focus_set()

root.mainloop()
