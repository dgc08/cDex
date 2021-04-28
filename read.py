from dex import Dex, atime
from display import dis, infout

def main():
    fn = input("Name of the indexfile: ")
    if fn.endswith(".ixf"):
        pass
    else:
        fn += ".ixf"
    print("Loading index...")
    f = open(fn, "rb")
    obj = Dex.load(f)
    print("Index loaded.\nDisplaying info...\n")
    tup = obj.info()
    print(infout(tup))
    istrue = True
    print("\nTo stop displaying the indexprice, use CTRL-C.")
    print("Start displaying indexprice...")
    try:
        erg = dis(tup)
        if erg == None:
            erg = ""
        print(erg)
    except KeyboardInterrupt:
        istrue = False
    except:
        print("yfinance-Error. Don't worry, that could happen. We are retrying...")
    while istrue:
        try:
            erg = dis(obj.info())
            if erg == None:
                erg = ""
            print(erg)
        except KeyboardInterrupt:
            istrue = False
        except:
            print("yfinance-Error. Don't worry, that could happen. We are retrying...")
    print("Displaying stopped.")