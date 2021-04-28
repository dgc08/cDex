from dex import Dex, atime
def infout(objinfo):
    a = "Index made @ "+str(objinfo[1])+", Namelist:\n"
    for i in objinfo[2]:
        a += i.upper()+" "
    return a
def dis(objinfo):
    return ("Indexprice "+str(objinfo[0])+" @ "+atime())
if __name__ == "__main__":
    b = Dex(["bayn.de", "sie.de"])
    print(infout(b.info()))
    print(dis(b.info()))