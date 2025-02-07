import PySimpleGUI as sg

# 画面のレイアウト部分
layout = [
    [sg.Input("Futaba")],
    [sg.Button("DO")],
    [sg.Text("Hello")]
]
window = sg.Window("test", layout)

# event と value にボタンを押された情報を渡す
event, values = window.read()

# 画面を閉じる
window.close()
