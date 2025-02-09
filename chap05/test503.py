from pathlib import Path

def savetext(filename):
    p=Path(filename)
    txt="書き出しテスト用テキストデータ"
    p.write_text(txt,encoding="UTF-8")

savetext("output.txt")
