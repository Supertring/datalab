class A:
    def __init__(self):
        self.__x = 1

    def show(self):
        print("from class A")


class B(A):
    def __init__(self):
        self.__y = 1

    def show(self):
        print('from class B')


c = B()
c.show()
