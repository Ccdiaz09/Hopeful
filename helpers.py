import random
import sys
import math


def chooseItemFromNamedList(list, prompt):
    print(prompt)
    counter = 0
    for item in list:
        counter += 1
        print(str(counter) + ":" + item.name)
    c = getInt("Choice: ", list.__len__())
    return list[c-1]


def getInt(prompt, max, min=1):
    while True:
        try:
            i = int(input(prompt))
            if max >= i >= min:
                return i
            else:
                print("Too small/Too big")

        except:
            print("It must be an integer")


def getFloat(prompt, max, min):
    while True:
        try:
            i = float(input(prompt))
            if max >= i >= min:
                return i
            else:
                print("Too small/Too big")
        except:
            print("It must be a number")


def getLetters(prompt):
    i = str(input(prompt))
    return i
