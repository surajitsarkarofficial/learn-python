class Demo:
    num = 100




    def __init__(self,a,b):
        print("I am a parameterised constructor with values ", a , b)
        print("The sum is  ", a+b)

obj = Demo(10,20)


class Demo2:
    def __init__(self):
        print("I am default constructor of Demo2...")

obj2 = Demo2()


