import PySimpleGUI as sg

# 画面のレイアウト部分
layout = [
    [sg.Input("Futaba", key="in")],
    [sg.Button("DO", key="btn")],
    [sg.Text(key="txt")]
]
window = sg.Window("test", layout)

# //////////////////////////////////////////

# 実行部分
def execute():

    txt = "Hello" + values["in"] + "san!"
    window["txt"].update(txt)

while True:

    # event と value にボタンを押された情報を渡す
    # "btn" は event に入り、それ以外は values へ
    event, values = window.read()

    if event == "btn":
        execute()
    if event == None:
        break

window.close()
