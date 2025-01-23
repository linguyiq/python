class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now siting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('Willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()