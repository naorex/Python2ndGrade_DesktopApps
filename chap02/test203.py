import PySimpleGUI as sg

# 画面のレイアウト部分
layout = [
    [sg.I("Futaba", key="in")],
    [sg.B("DO", key="btn")],
    [sg.T(key="txt")]
]
win = sg.Window("test", layout)

# //////////////////////////////////////////

# 実行部分
def execute():

    txt = "Hello" + v["in"] + "san!"
    win["txt"].update(txt)

while True:

    # e と value にボタンを押された情報を渡す
    # "btn" は e に入り、それ以外は v へ
    e, v = win.read()

    if e == "btn":
        execute()
    if e == None:
        break

win.close()
