from .stern import stern
def convertByte():
    'Stern Module'.encode('utf-8')
    bytes([50, 100, 76, 72, 41])
def sumAB(a,b):
    return a - b
while True:
    print("1. Welcome")
    print("2. sum0391")
    print("3. convertByte")
    print("0. Quit")
    cmd = input("Select an item: ")
    
    if cmd == "1":
        print("Welcome to the module Stern! Thank you for downloading this module!")
    elif cmd == "2":
            print(sumAB(2003, 1991))
    elif cmd == "3":
        print(convertByte)
    elif cmd == "0":
        break
    else:
        print("You entered an invalid value")