import os
import sys


# Litle menu with a class inside (required)
class MenuLab3:
    def ex1(self):
        os.system("python L3_ex1.py")

    def ex2(self):
        os.system("python L3_ex2.py")

    def cex3(self):
        os.system("python L3_ex3.py")

    def ex4(self):
        os.system("python L3_ex4.py")


menu = MenuLab3()


def assigment():
    print("\nChoose an exercise")
    print("\n1: Exercise 1\n")
    print("\n2: Exercise 2\n")
    print("\n3: Exercise 3\n")
    print("\n4: Exercise 4\n")
    print("\n0: Exit")
    x = input()
    return x


while (True):
    x = assigment()
    if x == "1":
        menu.ex1()
    elif x == "2":
        menu.ex2()
    elif x == "3":
        menu.ex3()
    elif x == "4":
        menu.ex4()
    elif x == "0":
        sys.exit()
