import sys
import time

def inportAndGo():
    check = True
    while check:
        try:
            a = int (input("how many?  "))
            check = False

        except:
                print("that's not a number you idiot")
    return a
def bomb  (a):
    nameCount = 0
    while nameCount < a:
        nameCount +=1
        fileName = str(nameCount)+'.txt'
        f = open(fileName, 'w')
        time.sleep(0.1)

a= inportAndGo()
bomb (a)
