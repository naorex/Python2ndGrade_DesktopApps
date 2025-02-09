import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [
    [sg.T("指定された年の干支を調べる")],
    [sg.T("西暦"),sg.I("2025",k="in1")],
    [sg.B("実行",k="btn"),sg.T(k="txt")]
]
win = sg.Window("干支調べアプリ",layout,
                font=(None,14),size=(320,150))

def execute():
    eto=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    in1=int(v["in1"])
    etonum=(in1-4)%12
    txt=f"{in1}年は、{eto[etonum]}年です"
    win["txt"].update(txt)

while True:
    e,v=win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
