import sys
import os
import shutil

def leave():
    sys.exit("You are leaving the Text Editor: Appen")
def read():
    try:
        filename = input("Enter the file name: ")
        target = open(filename, "r")
        readfile = target.read()
        print(readfile)
    except Exception as e:
        print("There was a problem: %s" % (e))
def delete():
    filename = input("Enter file name: ")
    try:
        os.unlink(filename)
    except Exception as e:
        print("There was a problem: %s" % (e))
def write():
    try:
        filename = input("Enter file name: ")
        target = open(filename, "a")
        while True:
            append = input()
            target.write(append)
            target.write("\n")
            if append.lower() == "menu":
                break
    except Exception as e:
        print("There was a problem: %s" % (e))
def cwd():
    try:
        print(os.getcwd())
        change = input("Change Y/N: ")
        if change.startswith("y"):
            path = input("New CWD: ")
            os.chdir(path)
    except Exception as e:
        print("There was a problem: %s" % (e))
def rename():
    try:
        filename = input("Enter current file name: ")
        new = input("Enter new file name: ")
        shutil.move(filename, new)
    except Exception as e:
        print("There was a problem: %s" % (e))
while True:
    print("Options: write, read, cwd, exit, delete, rename")
    do = input("What would you like to do today: ")
    if do.lower() == "write":
        write()
    elif do.lower() == "read":
        read()
    elif do.lower() == "delete":
        delete()
    elif do.lower() == "exit":
        leave()
    elif do.lower() == "cwd":
        cwd()
    elif do.lower() == "rename":
        rename()
