import chardet

def loadtext(filename):
    with open(filename, "rb") as f:
        b = f.read()
        enc=chardet.detect(b)["encoding"]
        print(f"{filename}は、{enc}")
loadtext("utest.txt")
loadtext("stest.txt")
