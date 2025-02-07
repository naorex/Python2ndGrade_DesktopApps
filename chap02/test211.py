import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [
    [sg.T("text")],
    [sg.I("input")],
    [sg.ML("multi-input 1-line\n2-line", size=(30,3))],
    [sg.Im("./futaba.png")]
]
win = sg.Window("test", layout,
                font=(None,14),
                size=(300,300))

e,v = win.read()
win.close()
