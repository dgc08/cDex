from dex import Dex, atime
def main():
    fn = input("Name of the new indexfile: ")
    if fn.endswith(".ixf"):
        pass
    else:
        fn += ".ixf"
    print("Please enter stock abbreviations like MSFT or GOOG. Something like EURUSD=X or BTCUSD=X is OK too. Continue with the abbreviation c.")
    listo = []
    wahr = True
    while wahr:
        b = input()
        if b == "c":
            wahr = False
        else:
            listo.append(b)
    print("Making Index ...")
    obj = Dex(listo)
    with open("il.ini", "a") as il:
        il.write(fn+"\n")
    f = open(fn, "wb")
    obj.save(f)
    print("Index made.")
