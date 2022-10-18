from re import X
import sys
import tkinter as tk
import maze_maker as mm
import random
import tkinter.messagebox as tkm

# def count_up():
#     global tmr, jid
#     tmr = tmr + 1
#     label["text"] = tmr
#     jid = root.after(1000, count_up)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    # jid = root.after(1000, count_up)

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, mx2, my2
    global cx, cy, cx2, cy2
    #こうかとんの挙動の設定
    if key == "Up":
        my -= 1
    if key =="Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key =="Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    #エネミー(ナイフ)の挙動設定
    l = [-1, 1]
    if key == "Up" or key =="Down" or key == "Left" or key == "Right":
        x = random.choice(l)
        y = random.choice(l)
        mx2 += x
        my2 += y
    if maze_lst[my2][mx2] == 0:
        cx2, cy2 = mx2*100+50, my2*100+50
    else:
        my2 -= y
        mx2 -= x

    canv.coords("tori", cx, cy)
    canv.coords("knife", cx2, cy2)
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15,9) #1:壁, 0:床
    #迷路の生成
    mm.show_maze(canv, maze_lst)
    #スタートとゴールの設定
    canv.create_rectangle(100, 100, 200, 200, fill= 'blue')
    canv.create_rectangle(1300, 700, 1400, 800, fill= 'orange')

    #エネミー(ナイフ)の設定
    knife = tk.PhotoImage(file="ex03/knife.png")
    mx2, my2= 1,1
    cx2, cy2 = mx2*200+50, my2*200+50
    canv.create_image(cx2, cy2, image=knife, tag="knife")
    
    #こうかとんの設定
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100
    canv.create_image(cx, cy, image=tori, tag="tori")   
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()