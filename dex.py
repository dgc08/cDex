from ins import Ins
import time
import pickle as pck
def atime():
    return time.strftime("%d.%m.%Y %H:%M:%S")
class Dex:
    def __init__(self, namelist):
        self.nl = namelist
        self.st = time.strftime("%d.%m.%Y %H:%M:%S")
        self.obl = []
        lol = True
        for i in namelist:
            try:
                x=Ins(i)
            except:
                lol = False
            if lol:
                self.obl.append()
            else:
                print("Can't create because one of the markets is close.")
                del(self)
                return
    def ret(self):
        su = 0
        tl = []
        vg = 0
        for i in self.obl:
            obj = i.ret()
            vg += obj[1]
            tl.append(obj)
        for i in tl:
            a = i[1]*i[0]*1000
            b = vg*i[2]
            if b == 0:
                return "(Market is closed.)"
            su += a/b
        if su == 0.0:
            return "(Market is closed.)"
        return su
    def info(self):
        return (self.ret(), self.st, self.nl)
    def __str__(self):
        su = 0
        tl = []
        vg = 0
        for i in self.obl:
            obj = i.ret()
            vg += obj[1]
            tl.append(obj)
        for i in tl:
            a = i[1]*i[0]*1000
            b = vg*i[2]
            if b == 0:
                return "(Market is closed.)"
            su += a/b
        if su == 0.0:
            return "(Market is closed.)"
        return su
    def save(self, fileobj):
        pck.dump(self, fileobj)
    @classmethod
    def load(cls, fileobj):
        return pck.load(fileobj)

if __name__ == "__main__":
    import time
    print("This can take a moment!")
    obj = Dex(["aapl", "msft", "fb"])
    for i in range(10):
        print("Time: "+str(atime())+" info-tuple: "+str(obj.info()))
    f = open("testdex.ixf", "wb")
    obj.save(f)