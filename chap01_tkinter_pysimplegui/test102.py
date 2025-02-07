import PySimpleGUI as sg

layout = [[sg.T(k="txt")],
          [sg.B("実行", k="btn")]]
win = sg.Window("Hello TEST", layout, size=(200, 100))

def execute():
    win["txt"].update("Hello")

while True:
    e,v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
