import os
import slist as sl
from time import sleep

def main(args=None):
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

    if num == 1:
        sl.showList()
    else:
        print("%d selected" % num)

    #keyboard interrupt
    keyInput = input()

if __name__ == "__main__":
    main()