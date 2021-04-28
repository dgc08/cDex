import yfinance as yf


class Ins:
    def __init__(self, name):
        t = yf.Ticker(name)
        self.a = t.info["bid"]
        lol = True
        if self.a == 0.0:
            print("Can't create. Market is closed.")
            lol = False
        if lol:
            self.n = name
        else:
            del(self)
            raise
    def ret(self):
        t = yf.Ticker(self.n)
        return (t.info["bid"], t.info["volume"], self.a)
    def __str__(self):
        t = yf.Ticker(self.n)
        return (t.info["bid"], t.info["volume"], self.a)

if __name__ == "__main__":
    import time
    obj = Ins("bayn.de")
    print(obj.ret())
    for i in range(120):
        print(i)
        time.sleep(1)
    print(obj.ret())
