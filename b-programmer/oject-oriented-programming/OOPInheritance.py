# Base class/Parent class
class Test:
    def __init__(self, action, value):
        self.action = action
        self.value = value

    def doAction(self):
        print(f"Perform {self.action} with value {self.value}")


# Derived class/Child class
class WebTest(Test):
    def __init__(self, url, action, value):
        self.url = url
        Test.__init__(self, action, value)

    def goto(self):
        print(f"Go to {self.url}")


class MobileTest(Test):
    def __init__(self, appname, action, value):
        self.appname = appname
        super().__init__(action, value)

    def openApp(self):
        print(f"Open App {self.appname}")


wt = WebTest('www.string.com', 'Insert', 20)
wt.goto()
wt.doAction()

mt = MobileTest('string.apk', 'Insert', 19.2)
mt.openApp()
mt.doAction()
