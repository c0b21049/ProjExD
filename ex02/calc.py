import tkinter as tk
import tkinter.messagebox as tkm
import webbrowser

url = "https://www.amazon.co.jp/"

def click_num(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def click_equal(event):
    eq = entry.get()
    ans = eval(eq)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def click_Clear(event):
    entry.delete(0, tk.END)

def click_amazon(event):
    webbrowser.open(url)

def click_percent(event):
    per = entry.get()
    ans = eval(f"{per}/100")
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=("", 40), justify="right")
entry.grid(row=0, column=0, columnspan=10)

r=1
c=0
L1 = list(range(9, 6, -1))
L2 = list(range(6, 3, -1))
L3 = list(range(3, 0, -1))
for i, num in enumerate(L1+["+"]+L2+["-"]+L3+["*"]+["/", "0"], 1):
    button = tk.Button(root, text=f"{num}", font=("", 30), width=3, height=1)
    button.bind("<1>", click_num)
    button.grid(row=r, column=c)
    c += 1
    if i%4 == 0:
        r+=1
        c=0

button = tk.Button(root, text="C", font=("", 30), width=3, height=1)
button.bind("<1>", click_Clear)
button.grid(row=r, column=c)
r=4
c=3

button = tk.Button(root, text="=", font=("", 30), width=3, height=1, bg = "#87cefa")
button.bind("<1>", click_equal)
button.grid(row=r, column=c)
r+=1
c=0

button = tk.Button(root, text="%", font=("", 30), width=3, height=1)
button.bind("<1>", click_percent)
button.grid(row=r, column=c)
c+=1

button = tk.Button(root, text="a", font=("", 30), width=3, height=1, bg = "#ffa500")
button.bind("<1>", click_amazon)
button.grid(row=r, column=c)


root.mainloop()