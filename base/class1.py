class class1:


    def __str__(self) -> str:
        return super().__str__()

    def __init__(self):
        pass

    def say(self):
        print("class1 say")



c = class1()
c.say()
print(c)