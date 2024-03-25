from ClassAndObjects.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        # calling parent class const from child class
        Vehicle.__init__(self)
        print("This is default const from Car class..")


    def engine(self):
        self.lights()
        print("This is Engine method from Car class...")


    def wheels(self):
        print("I have 4 wheels..")


obj1 = Car()
obj1.lights()
obj1.engine()
obj1.wheels()
