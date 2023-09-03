# Example 1

class Bird:
    # class variables/attributes
    name = ""
    age = 0


# create an object for class Bird
b1 = Bird()
b1.name = 'Sparrow'
b1.age = 10

# create another object for class Bird
b2 = Bird()
b2.name = "WoodPeeker"
b2.age = 5

# Display the attributes
print(f"{b1.name} is {b1.age} years old")
print(f"{b2.name} is {b2.age} years old")
