# -*- coding: utf-8 -*-
"""AI4021 - HW1 - 1 - Python Tutorial 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XXXRlNRyBJ03o3yoW1KMLK9qaN3klohU

**Question 1:** Write a Python program that asks the user for their age. If the age is greater than or equal to 18, print "You are an adult." Otherwise, print "You are a minor."
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

"""**Question 2:** Write a Python program to print the numbers from 1 to 10 using a for loop."""

for number in range(1, 11):
    print(number)

"""**Question 3:** Write a Python program to calculate the sum of all even numbers from 1 to 20 using a while loop."""

number = 1
sum_even = 0

while number <= 20:
    if number % 2 == 0:
        sum_even += number
    number += 1

print("Sum of even numbers from 1 to 20:", sum_even)

"""**Question 4:** Define a function called multiply that takes two parameters and returns their product."""

def multiply(x, y):
    return x * y

result = multiply(5, 3)
print("Result:", result)

"""**Question 5:** Create a class called Person with a constructor method that initializes the name and age attributes. Then, create an instance of the Person class and print the person's name and age."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_instance = Person(name="John", age=25)

print("Person's Name:", person_instance.name)
print("Person's Age:", person_instance.age)

"""**Question 6:** Create a subclass called `Student` that inherits from the `Person` class. Add an additional attribute called `student_id` to the `Student` class. Create an instance of the `Student` class and print the student's name, age, and student ID."""

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student_instance = Student(name="Alice", age=20, student_id="S12345")

print("Student's Name:", student_instance.name)
print("Student's Age:", student_instance.age)
print("Student ID:", student_instance.student_id)

"""**Question 7:** Write a Python program that prompts the user to enter a number and then prints whether the number is prime or not. Create a function called `is_prime` that takes an integer as an argument and returns True if it's prime, and False otherwise."""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))

if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

"""**Question 8:** Write a Python program that calculates the factorial of a given number using a recursive function. Prompt the user for an integer input and print its factorial."""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

user_input = input("Enter an integer: ")

try:
    user_number = int(user_input)
    if user_number < 0:
        print("Please enter a non-negative integer.")
    else:
        result = factorial(user_number)
        print(f"The factorial of {user_number} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

"""**Question 9:** Create a class called `Rectangle` with attributes `width` and `height`. Add a method `calculate_area` that calculates and returns the area of the rectangle. Create an instance of the `Rectangle` class and print its area."""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle_instance = Rectangle(width=5, height=8)

area = rectangle_instance.calculate_area()
print(f"The area of the rectangle is: {area}")

"""**Question 10:** Create a subclass called `Square` that inherits from the `Rectangle` class. Add a method `calculate_perimeter` to the `Square` class that calculates and returns the perimeter of the square. Create an instance of the `Square` class and print its perimeter."""

class Square(Rectangle):
    def calculate_perimeter(self):
        return 4 * self.width

square_instance = Square(width=4, height=4)

perimeter = square_instance.calculate_perimeter()
print(f"The perimeter of the square is: {perimeter}")

"""**Question 11:** Create a base class called `Animal` with attributes `name` and `species`. Provide a constructor to initialize these attributes and a method called `speak` that prints a generic message like "The animal makes a sound."
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} the {self.species} makes a sound.")

"""**Question 12:** Create a subclass called `Dog` that inherits from the `Animal` class. Add a constructor to initialize the `name`, `species`, and `breed` attributes specific to dogs. Override the `speak` method in the `Dog` class to print "Woof!"
"""

class Dog(Animal):
    def __init__(self, name, breed):

        super().__init__(name=name, species="Dog")
        self.breed = breed

    def speak(self):

        print(f"{self.name} the {self.breed} says: Woof!")

"""**Question 13:** Create another subclass called `Cat` that inherits from the `Animal` class. Add a constructor to initialize the `name`, `species`, and `color` attributes specific to cats. Override the `speak` method in the `Cat` class to print "Meow!"
"""

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name=name, species="Cat")
        self.color = color

    def speak(self):
        print(f"{self.name} the {self.color} cat says: Meow!")

"""**Question 14:** Create instances of both the `Dog` and `Cat` classes and call their `speak` methods to demonstrate polymorphism."""

dog_instance = Dog(name="Buddy", breed="Labrador Retriever")
cat_instance = Cat(name="Whiskers", color="Gray")

dog_instance.speak()
cat_instance.speak()