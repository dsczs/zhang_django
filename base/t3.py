#!/usr/local/python3/bin/python3

v1 = (2, 4, 5)
print(v1[1:])
# v1[1] = 44

v2 = {"name":"a", "age":26}
print(v2['name'])

"""
Tip:
    由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
    可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，
    表示只有两个条件同时成立的情况下，判断条件才成功。
"""
v3 = 5
v4 = 4
if v3 > 4 and v4 == 4:
    print(1)
elif v3 > 5:
    print(2)
else:
    print(3)

v5 = 10
while v5 < 15:
    print(v5)
    v5 = v5 + 1
else:
    print("over")

for i in range(10):
    print(i)

