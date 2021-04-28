import read
import build
while True:
    option = input("Do you want to create an index, open an index or recive a list of your indices?(c/o/l): ")
    if option == "c":
        build.main()
    elif option == "o":
        read.main()
    elif option == "l":
        with open("il.ini") as il:
            li = il.readlines()
        for i in li:
            print(i.replace(".ifx", ""))