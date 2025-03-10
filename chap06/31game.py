import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [
    [sg.T("Let's start Janken")],
    [sg.Im(k="img1"), sg.T(k="txt1")],
    [sg.T("Input a int number.", k="txt2")],
    [sg.I("1", k="in1", size=(15)),
     sg.B("Input", k="btn", bind_return_key=True)]
]
win = sg.Window("31game App",layout,
                font=(None,14),
                finalize=True)

def getnextnums(n):
    global nextnums, choicemsg
    nextnums=list(range(n+1,min(32,n+4)))
    choicemsg=f"Choose from {nextnums}."
    win["txt2"].update(choicemsg)

def question():
    global playflag
    getnextnums(0)
    win["txt1"].update("Let's start game.")
    win["img1"].update("futaba0.png")
    playflag=True

def com_turn(comnum):
    keynums=[2,6,10,14,22,26,30]
    getnextnums(comnum)
    comnum+=1
    for n in nextnums:
        if n in keynums:
            comnum=n
    if random.randint(0,1)>0:
        comnum=nextnums[0]
    win["txt1"].update(f"I guess {comnum} for my number.")
    getnextnums(comnum)

def my_turn():
    global playflag
    if v["in1"].isdecimal()==False:
        win["txt1"].update("Input int number.")
    else:
        mynum=int(v["in1"])
        if mynum in nextnums:
            if mynum==31:
                win["txt1"].update("You lose")
                win["img1"].update("futaba2.png")
                win["txt2"].update("Push buttom then next")
                playflag=False
            elif mynum==30:
                win["txt1"].update("You win")
                win["img1"].update("futaba1.png")
                win["txt2"].update("Push buttom then next")
                playflag=False
            else:
                com_turn(mynum)
        else:
            win["txt1"].update(choicemsg)

question()
while True:
    e,v=win.read()
    if e=="btn":
        if playflag==False:
            question()
        else:
            my_turn()
    if e==None:
        break
win.close()
