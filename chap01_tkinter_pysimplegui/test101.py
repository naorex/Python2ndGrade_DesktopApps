import tkinter as tk

def execute():
    txt = "hello"
    lbl.configure(text=txt)

root = tk.Tk()
root.title("Hello TEST")
root.geometry("200x100")

lbl = tk.Label(text="")
btn = tk.Button(text="実行", command=execute)

lbl.pack()
btn.pack()
tk.mainloop()
