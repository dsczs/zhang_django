class User:
    name = ""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name:"+self.name+"age:"+str(self.age)
