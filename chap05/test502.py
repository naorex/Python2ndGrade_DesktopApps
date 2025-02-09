from pathlib import Path
import chardet

def loadtext(filename):
    with open(filename, "rb") as f:
        b = f.read()
        enc=chardet.detect(b)["encoding"]
        p = Path(filename)
        txt=p.read_text(encoding=enc)
        print(f"{filename} : {txt}")
loadtext("utest.txt")
loadtext("stest.txt")
