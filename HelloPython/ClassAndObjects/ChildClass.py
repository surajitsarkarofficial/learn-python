from ClassAndObjects.BaseClass import Base


class Child(Base):
    def __init__(self,msg):
        print("this is child class const")
        Base.__init__(self,msg)
        print("this is child class const")

obj = Child("My Custom Message")