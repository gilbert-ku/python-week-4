class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

#  instance of the Person class
gilbert = Person("Gilbert Kutoto", 26, "male")
# Calling the introduce method to display the person's information
gilbert.introduce()
