import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key =="Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")

    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/5.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()