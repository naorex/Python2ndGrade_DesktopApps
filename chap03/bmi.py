import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [
    [sg.T("身長と体重を入力")],
    [sg.T("身長cm"),sg.I("170",k="in1")],
    [sg.T("体重kg"),sg.I("70",k="in2")],
    [sg.B("実行",k="btn"),sg.T(k="txt")]
]
win = sg.Window("BMI計算アプリ",layout,
                font=(None,14),size=(320,150))

def execute():
    in1=float(v["in1"])
    in2=float(v["in2"])
    bmi=in2/(in1*in1)
    txt=f"BMIは {bmi:.2f}円です"
    win["txt"].update(txt)

while True:
    e,v=win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
