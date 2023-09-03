class Test:
    def __init__(self, action, value):
        self.action = action
        self.value = value

    def doAction(self):
        print(f"Perform {self.action} given value: {self.value}")


test = Test('Insert', 20)
test.doAction()
