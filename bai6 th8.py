from tkinter import*



def newFile():

    print("new File!")

    def About():

        print("This is a simple example of a menu")

root=TK()

menu=Menu(root)

root.config(menu=menu)

filemenu=Menu(menu)

menu.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New", command=NewFile)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

helpmenu=Menu(menu)

menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About...", command=About)



mainloop()
