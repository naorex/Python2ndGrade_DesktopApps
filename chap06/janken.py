import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [
    [sg.T("Let's start Janken")],
    [sg.Im("futaba0.png",k="img1"), sg.Im(k="img2")],
    [sg.T(k="txt")],
    [sg.B("Rock", k="btn0"),
     sg.B("Paper", k="btn1"),
     sg.B("Scissors", k="btn2")]
]
win = sg.Window("Janken App",layout,
                font=(None,14))

handimg=["h0.png","h1.png","h2.png"]
message=["aiko","you win!! ><","you lose ^^"]
faceimg=["futaba0.png","futaba1.png","futaba2.png"]

def janken(mynum):
    comnum=random.randint(0,2)
    win["img2"].update(handimg[comnum])
    judge=(comnum-mynum)%3
    win["txt"].update(message[judge])
    win["img1"].update(faceimg[judge])

while True:
    e,v=win.read()
    if e=="btn0":
        janken(0)
    if e=="btn1":
        janken(1)
    if e=="btn2":
        janken(2)
    if e==None:
        break
win.close()
