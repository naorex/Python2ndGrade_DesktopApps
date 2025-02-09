import PySimpleGUI as sg
import datetime

layout = [
    [sg.T(font=("Arial",40),k="txt",
          size=(20,1),justification="center")]
]
win = sg.Window("時計テスト",layout,
                size=(320,80),
                keep_on_top=True)

c=0

while True:
    e,v = win.read(timeout=500)
    c=c+1
    win["txt"].update(f"{c}")
    if e == None:
        break
win.close()
