import tkinter as tk
import tkinter.messagebox as tkm
import webbrowser #URLからサイトへ飛ぶためのwebbrowserをインポート

url = "https://www.amazon.co.jp/" #amazonのURL

def click_num(event): #数字を入力した場合
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def click_equal(event): #=を入力した場合
    eq = entry.get()
    ans = eval(eq)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def click_Clear(event): #Cを入力した場合
    entry.delete(0, tk.END)

def click_amazon(event): #aを入力した場合
    webbrowser.open(url)

def click_percent(event): #%を入力した場合
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
BUTTON=[
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "%", "/"]
]#ボタンを生成するための配置(リスト)
for i in BUTTON:
    for j in range(len(i)):
        num = i[j]    
        btn = tk.Button(root, text=f"{num}", font=("", 30), width=3, height=1)
        if (num == "C"):
            btn.bind("<1>", click_Clear)
        elif (num == "%"):
            btn.bind("<1>", click_percent)
        else:
            btn.bind("<1>", click_num)
        btn.grid(row=r, column=c)
        c += 1
        if j == 3:
            r += 1
            c = 0

button = tk.Button(root, text="a", font=("", 30), width=3, height=1, bg = "#ffa500") #ボタンaを配置
button.bind("<1>", click_amazon)
button.grid(row=r, column=c)
c = 3

button = tk.Button(root, text="=", font=("", 30), width=3, height=1, bg = "#87cefa") #ボタン=を配置
button.bind("<1>", click_equal)
button.grid(row=r, column=c)

root.mainloop()