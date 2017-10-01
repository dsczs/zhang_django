"""
TIP:函数传可变变量和传不可变变量的区别
"""


def change(b):
    b += 2

b = 4
print(b)
change(b)
print(b)


def changeList(myList):
    myList.append([2,4]);

myList = [1,3]
print(myList)
changeList(myList)
print(myList)