import PySimpleGUI as sg
import datetime
sg.theme("DarkBrown3")

layout = [
    [sg.T("00:00:00",font=("Arial",40),k="txt1")],
    [sg.ML(font=("Arial",18),size=(40,12),k="txt2")]
]
win = sg.Window("TimeTable",layout,
                font=(None,14),size=(450,450),
                keep_on_top=True)

sch=[
    ["1st",8,50],
    ["2nd",10,30],
    ["break",12,40],
    ["3rd",13,20],
    ["4th",15,10],
    ["5th",17,00],
    ["6th",18,50],
]

def execute():
    now=datetime.datetime.now()
    win["txt1"].update(f"{now:%H:%M:%S}")
    txt2=""
    for s in sch:
        dt = now.replace(hour=s[1],minute=s[2],second=0)-now
        if dt.total_seconds() > 0:
            txt2+=f"{s[0]}【{s[1]:02d}:{s[2]:02d}】あと{dt}です\n"
        else:
            txt2+=f"{s[0]}【{s[1]:02d}:{s[2]:02d}】---\n"
    win["txt2"].update(txt2)

while True:
    e,v = win.read(timeout=500)
    if e == None:
        break
    execute()
win.close()
