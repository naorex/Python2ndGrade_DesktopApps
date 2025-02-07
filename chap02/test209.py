import PySimpleGUI as sg
sg.theme("BrightColors")

# 画面のレイアウト部分
layout = [
    [sg.T("1.1"), sg.T("1.2")],
    [sg.T("2.1"), sg.T("2.2")],
    [sg.T("3.1"), sg.B("Button")],
]
win = sg.Window("test", layout,
                font=(None,14),
                size=(300,300))

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
