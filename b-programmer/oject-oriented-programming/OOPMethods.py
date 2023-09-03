class Land:
    length = 0.0
    width = 0.0

    def area(self):
        print("Are of the land is :", self.length * self.width)


lan = Land()
lan.area()

# Set new values
Land.width = 12.0
Land.length = 13.5
lan.area()
