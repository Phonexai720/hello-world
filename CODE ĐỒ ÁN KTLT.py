from tkinter import *
import time
import random

#tao hình bóng, hướng bóng và tốc độ bóng chạy, xử lý khi va chạm
class Ball:
    def __init__(seft, canvas, color, thanh, thanh1):
        seft.canvas = canvas
        seft.thanhtruot = thanh;
        seft.thanhtruot1 = thanh1
        seft.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        seft.canvas.move(seft.id, 100, 200)
        start = [-3, -2, -2, 1, 2, 3]
        random.shuffle(start)
        seft.x = start[0];
        seft.y = 1;
        seft.canvas_height = 600
        seft.canvas_width = 400
        seft.over = False
        seft.diem = 0
        seft.text_diem = seft.canvas.create_text(90, 550, text="Duy manh dzai: " + str(seft.diem), fill="#4169e1",
                                                 font=('cooper black', 15))

        seft.diem1 = 0
        seft.text_diem1 = seft.canvas.create_text(310, 50, text="Diem doi thu: " + str(seft.diem1), fill="#4169e1",
                                                 font=('cooper black', 15))

    #bóng va chạm với thanh trượt dưới
    def vatram(seft, pos):
        pos_thanhtruot = seft.canvas.coords(seft.thanhtruot.id)
        if pos[0] >= pos_thanhtruot[0] and pos[2] <= pos_thanhtruot[2]:
            if pos[1] >= pos_thanhtruot[1] and pos[3] <= pos_thanhtruot[3]:
                seft.diem += 1
                seft.canvas.itemconfig(seft.text_diem, text="Mạnh dzai: " + str(seft.diem))
                return True
        return False
#bóng va chạm với thanh trượt trên
    def vacham(seft, pos):
        pos_thanhtruot1 = seft.canvas.coords(seft.thanhtruot1.id1)
        if pos[0] >= pos_thanhtruot1[0] and pos[2] <= pos_thanhtruot1[2]:
            if pos[1] >= pos_thanhtruot1[1] and pos[3] <= pos_thanhtruot1[3]:
                seft.diem1 += 1
                seft.canvas.itemconfig(seft.text_diem1, text="Điểm đối thủ: " + str(seft.diem1))
                return True
        return False
#bóng chạy trong canvas
    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        pos = seft.canvas.coords(seft.id)
        if pos[1] <= 0:
            seft.over = True
        if pos[3] >= seft.canvas_height:
            seft.over = True
        if seft.vatram(pos) == True:
            seft.y = -3;
        if seft.vacham(pos) == True:
            seft.y = 3;
        if pos[0] <= 0:
            seft.x = 3;
        if pos[2] >= seft.canvas_width:
            seft.x = -3;

#thanh trượt dưới
class thanhtruot:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id, 300, 500)


        seft.canvas.bind_all('<KeyPress-Left>', seft.trai)
        seft.canvas.bind_all('<KeyPress-Right>', seft.phai)



        seft.x = 0
        seft.y = 0

    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        poss = seft.canvas.coords(seft.id)
        if poss[0] <= 0:
            seft.x = 0
        if poss[2] >= 400:
            seft.x = 0;


    def trai(seft, event):
        seft.x = -2

    def phai(seft, event):
        seft.x = 2

#thanh tren
class thanhtruot1:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id1 = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id1, 300,70)

        seft.canvas.bind_all('<KeyPress-a>', seft.trai)
        seft.canvas.bind_all('<KeyPress-d>', seft.phai)

        seft.x = 0
        seft.y = 0

    def draw(seft):
        seft.canvas.move(seft.id1, seft.x, seft.y)
        posss = seft.canvas.coords(seft.id1)
        if posss[0] <= 0:
            seft.x = 0
        if posss[2] >= 400:
            seft.x = 0;
    def trai(seft, event):
        seft.x = -2

    def phai(seft, event):
        seft.x = 2



t = tk = Tk()
tk.title("đỡ bóng 2 người")
tk.resizable(0, 0)
can = Canvas(tk, width=400, height=600)
can.pack()
thanh = thanhtruot(can, "#ff7f50")
thanhtren = thanhtruot1(can, '#ff7f50',)
bong = Ball(can, "#7b68ee", thanh, thanhtren)
#?????????
while 1:
    if bong.over != True:
        bong.draw()
        thanh.draw()
        thanhtren.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break
gameoverr = can.create_text(200, 300, text="GAME OVER: " , fill="red",
                                                 font=('cooper black', 30))
t.mainloop()