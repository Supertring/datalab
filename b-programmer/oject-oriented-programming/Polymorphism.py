# python inheritance and polymporphism
class Vehicle:
    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def getColor(self):  # getColor() function is accessible to class car
        return self.__color

    def setColor(self, color):  # setColor() is accessible outside the class
        self.__color = color

    def getName(self):  # is accessible outside the class
        return self.__name


class Car(Vehicle):
    def __init__(self, name, color, model):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def getInformation(self):
        # getName(), getColor() are accessible to child class through inheritance
        return self.getName() + self.__model + "in" + self.getColor() + "color"


c = Car('BMW', 'Black', 'B-racer')
print(c.getInformation())
# Car has no method getName(), but is accessible through derived class
print(c.getName())
