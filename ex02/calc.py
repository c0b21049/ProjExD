import tkinter as tk
import tkinter.messagebox as tkm

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

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=("", 40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

r=1
c=0
for i, num in enumerate(list(range(9, -1, -1))+["+"], 1):
    button = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    button.bind("<1>", click_num)
    button.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r+=1
        c=0

button = tk.Button(root, text="=", font=("", 30), width=4, height=2)
button.bind("<1>", click_equal)
button.grid(row=r, column=c)

root.mainloop()