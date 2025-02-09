import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

layout = [
    [sg.T("AM 00:00:00",font=("Arial",40),
     k="txt1",size=(20,1),justification="center")]
]
win = sg.Window("時計",layout,
                size=(400,80),
                keep_on_top=True)

def execute():
    now=datetime.datetime.now()
    win["txt1"].update(f"{now:%H:%M:%S}")

while True:
    e,v = win.read(timeout=500)
    execute()
    if e == None:
        break
win.close()
