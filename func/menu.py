import os
import ppd
from time import sleep

pd = None

def main(args=None):
    global pd

    pd = ppd.PPD()

    while(True):
        #display clear
        os.system("clear")

        #menu display
        print("="*50)
        print("Welcome to PPD!!\nSelect the below Menus.")
        print("="*50)
        print("1. Show list")
        print("2. Add Data")
        print("3. Modify Data")
        print("4. Delete Data")
        print("0. Exit.")
        print("menu>", end=' ')
        
        menu = int(input())

        if(menu >=1 and menu <= 4):
            menuFunc(menu)
        elif(menu == 0):
            break
        else:
            print("You Enter the wrong number")
            sleep(1)
        
        
def menuFunc(num):
    global pd

    if num == 1:
        pd.showList()
    elif num == 2:
        pd.addData()
    elif num == 3:
        pd.modifyData()
    elif num == 4:
        pd.deleteData()
    else:
        print("%d selected" % num)

    #keyboard interrupt
    keyInput = input()

if __name__ == "__main__":
    main()