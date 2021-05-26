import tkinter as tk

root =tk.Tk()

v=tk.InVar()

V.set(1)

languages = [

    ("python",1),

    ("prtl",2),

    ("java",3),

    ("c++",4),

    ("c",5)

    ]

def showChoice():

    print(v.get())



tk.Label(root,

         text="""Choose your favourite

programming language:""",

         justify=tk.LEFT,

         padx=20).pack()



for val, language in enumerate(languages):

    tk.Radiobutton(root,

                   text=language,

                   padx=20,

                   variable=v,

                   command=ShowChoice,

                   value=val).pack(anchor=tk.W)

root.mainloop()
