import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [
    [sg.B("Open File",k="btn1"),sg.T(k="txt1")],
    [sg.B("Save File",k="btn2")],
    [sg.Im(k="img")]
]
win=sg.Window("Convert image fine to MONO", layout,
              size=(320,400))

def loadimage():
    global img
    loadname = sg.popup_get_file("Choose image file")

    # ファイルが選択されなければ戻る
    if not loadname:
        return

    try:
        img=Image.open(loadname).convert("L") # モノクロへ変換
        img2=img.copy()
        img2.thumbnail((300,300)) # 300px以下に圧縮
        bio=io.BytesIO()

        # バイナリデータを画像データへ変換
        img2.save(bio,format="PNG")
        win["img"].update(data=bio.getvalue())
        win["txt1"].update(loadname)

    except:
        win["img"].update()
        win["txt"].update("failed")

img=None
def saveimage():

    # 画像が指定されていない場合はreturn
    if img==None:
        return
    savename=sg.popup_get_file("Save file with name")

    if not savename:
        sg.PopupTimed("Input name of image")
        return

    # ファイル名の最後が.pngでなければ追加
    if savename.endswith(".png") == False:
        savename=savename+".png"

    try:
        img.save(savename)
        win["txt1"].update(savename+" is saved")
    except:
        win["txt1"].update("faild")

while True:
    e,v=win.read()
    if e=="btn1":
        loadimage()
    if e=="btn2":
        saveimage()
    if e==None:
        break
win.close()
