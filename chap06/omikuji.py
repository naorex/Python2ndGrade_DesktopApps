import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [
    [sg.T("Let's start omikuji")],
    [sg.Im("futaba0.png")],
    [sg.T(k="txt")],
    [sg.B("Do omikuji", k="btn")]
]
win = sg.Window("Omikuji App",layout,
                font=(None,14))

def omikuji():
    kuji=["大吉","中吉","小吉","凶"]
    res=random.choice(kuji)
    txt=f"resutl was {res}"
    win["txt"].update(txt)

while True:
    e,v=win.read()
    if e=="btn":
        omikuji()
    if e==None:
        break
win.close()
