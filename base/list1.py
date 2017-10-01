t1 = [2,3,4]
for t in t1:
    print(t)

print(min(t1))

t2 = ['a','ac','b'];
print(max(t2))

t3 = {"name":"a","name":"b","age":34};
print(t3['name'])

# dict遍历
for (d,x) in t3.items():
    print("key:"+d+",value:"+str(x))

print(t3.keys())

for k in t3.keys():
    print(type(k))
    print("key:" + str(k))
    print(t3[''+k])