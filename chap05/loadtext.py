import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("DarkBrown3")

layout = [
    [sg.B("Open File",k="btn1"),sg.T(k="txt1")],
    [sg.ML(k="txt2",font=(None,14),size=(80,15))]
]
win=sg.Window("Read text file", layout)

def loadtext():
    global loadname, enc
    loadname = sg.popup_get_file("Choose text file")

    # ファイルが選択されなければ戻る
    if not loadname:
        return

    #読み込む処理
    with open(loadname, "rb") as f:
        b=f.read()
        #encode方式を調べる
        enc=chardet.detect(b)["encoding"]
        p=Path(loadname)
        txt=p.read_text(encoding=enc)
        win["txt1"].update(loadname)
        win["txt2"].update(txt)

while True:
    e,v=win.read()
    if e=="btn1":
        loadtext()
    if e==None:
        break
win.close()
