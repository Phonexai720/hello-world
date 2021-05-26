from tkinter import*



window=Tk()



window.title("Welcome to likeGeeks app")



window.geometry('350*200')



lbl =label(window, text="hello")



lbl.grid(column=0, row=0)



def clicked():

    

    lbl.configure(text="button was clicked !!")



    btn=Button(window, text="Click Me", command=clicked)



    btn.grid(column=1, row=0)



    window.mainlop()
