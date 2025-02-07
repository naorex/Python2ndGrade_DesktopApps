import PySimpleGUI as sg
sg.theme("DarkBrown3")

# 画面のレイアウト部分
layout = [
    [sg.T("ABCDE",size=(30,1), justification="left")],
    [sg.T("ABCDE",size=(30,1), justification="center")],
    [sg.I("ABCDE",size=(30,1), justification="right")],
]
win = sg.Window("test", layout,
                font=(None,14),
                size=(300,300))

# //////////////////////////////////////////

# 実行部分

while True:

    # e と value にボタンを押された情報を渡す
    # "btn" は e に入り、それ以外は v へ
    e, v = win.read()

    if e == None:
        break
    else:
        break

win.close()
