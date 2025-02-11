import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [
    [sg.B("Open File",k="btn1"),sg.T(k="txt1")],
    [sg.Im(k="img")]
]
win=sg.Window("Open image", layout,
              size=(320,380))

def loadimage():
    loadname = sg.popup_get_file("Choose image file")

    # ファイルが選択されなければ戻る
    if not loadname:
        return

    try:
        img=Image.open(loadname)
        img.thumbnail((300,300)) # 300px以下に圧縮
        bio=io.BytesIO()

        # バイナリデータを画像データへ変換
        img.save(bio,format="PNG")
        win["img"].update(data=bio.getvalue())
        win["txt1"].update(loadname)

    except:
        win["img"].update()
        win["txt"].update("failed")

while True:
    e,v=win.read()
    if e=="btn1":
        loadimage()
    if e==None:
        break
win.close()
