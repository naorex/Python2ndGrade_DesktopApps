import PySimpleGUI as sg
from pathlib import Path
import chardet
sg.theme("DarkBrown3")

layout = [
    [sg.B("Open File",k="btn1"),sg.T(k="txt1")],
    [sg.B("Save FIle",k="btn2")],
    [sg.ML(k="txt2",font=(None,14),size=(80,15))]
]
win=sg.Window("Save text file", layout,
              resizable=True)

loadname=None
enc="UTF=8"
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

def savetext():
    global loadname,enc
    savename=sg.popup_get_file("Save as",
                               default_path=loadname, #ファイル保存ダイアログを開く
                               save_as=True)
    # ファイル名がなかったらアラートを出す
    if not savename:
        sg.PopupTimed("Input File Name")
        return

    # 拡張子が無ければ.txtを付ける
    if savename.find(".")==-1:
        savename=savename+".txt"
    p=Path(savename)
    p.write_text(v["txt2"],encoding=enc)
    win["txt1"].update(savename)
    loadname=savename

while True:
    e,v=win.read()
    if e=="btn1":
        loadtext()
    if e=="btn2":
        savetext()
    if e==None:
        break
win.close()
