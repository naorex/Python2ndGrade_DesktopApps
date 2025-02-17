import PySimpleGUI as sg
import io
import qrcode
sg.theme("DarkBrown3")

layout = [
    [sg.T("URL"),sg.I(k="in1")],
    [sg.B("Make QRcode",k="btn1")],
    [sg.B("Save QRcode",k="btn2"),sg.T(k="txt")],
    [sg.Im(k="img")]
]
win=sg.Window("QRcode Maker", layout,
              size=(320,420))

img=None
def execute():
    global img
    if not v["in1"]:
        sg.PopupTimed("Input URL")
        return
    img=qrcode.make(v["in1"])  # make QRcode
    img.thumbnail((300,300))
    bio=io.BytesIO()
    img.save(bio,format="PNG")
    win["img"].update(data=bio.getvalue())

def saveimage():
    if img==None:
        return
    savename=sg.popup_get_file("Naming and save png file",
                               save_as=True)
    if not savename:
        sg.PopupTimed("Input name for png file")
        return
    if savename.endswith(".png")==False:
        savename=savename+".png"
    try:
        img.save(savename)
        win["txt"].update(savename+" was saved.")
    except:
        win["txt"].update("Failed")

while True:
    e,v = win.read()
    if e=="btn1":
        execute()
    if e=="btn2":
        saveimage()
    if e==None:
        break
win.close()
