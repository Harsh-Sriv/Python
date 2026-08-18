# ============================================================
#                  CLASSES AND OBJECTS
# ============================================================

# CLASS
# A class is a blueprint/template for creating objects.

# OBJECT
# An object is an actual instance of a class.


# ============================================================
# 1. Basic Class and Object
# ============================================================

class Student:

    # Constructor
    # __init__() runs automatically when an object is created.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    # A function defined inside a class.
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Creating objects

student1 = Student("Harsh", 22)
student2 = Student("Rahul", 21)

student1.introduce()
student2.introduce()


# ============================================================
# 2. Accessing and modifying attributes
# ============================================================

print(student1.name)

student1.age = 23

print(student1.age)


# ============================================================
# 3. Class Variable
# ============================================================

class Employee:

    # Class variable
    # Shared by all objects.
    company = "Accenture"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Harsh")
emp2 = Employee("Aman")

print(emp1.name)
print(emp1.company)

print(emp2.name)
print(emp2.company)


# ============================================================
# 4. Instance vs Class Variables
# ============================================================

class Car:

    wheels = 4                 # Class variable

    def __init__(self, brand):
        self.brand = brand     # Instance variable


car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.brand)
print(car2.brand)

print(car1.wheels)
print(car2.wheels)


# ============================================================
# 5. Instance Method
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(10, 20))
print(calc.multiply(5, 4))


# ============================================================
# 6. Inheritance
# ============================================================

# A child class can inherit attributes and methods
# from a parent class.

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


dog = Dog()

dog.speak()       # Inherited from Animal
dog.bark()        # Dog's own method


# ============================================================
# 7. Method Overriding
# ============================================================

class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Woof!")


dog = Dog()

dog.speak()

# Dog's speak() overrides Animal's speak().


# ============================================================
# 8. Encapsulation - Basic Example
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

print(account.get_balance())

# __balance is treated as a private attribute.
# Direct access like account.__balance will not work normally.


# ============================================================
# 9. Class Method
# ============================================================

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.change_school("XYZ School")

print(Student.school)


# ============================================================
# 10. Static Method
# ============================================================

class Math:

    @staticmethod
    def square(x):
        return x * x


print(Math.square(5))


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
CLASS
-> Blueprint for creating objects.

OBJECT
-> Instance of a class.

ATTRIBUTE
-> Variable belonging to an object/class.

METHOD
-> Function inside a class.

CONSTRUCTOR
-> __init__()
-> Runs automatically when object is created.

self
-> Refers to the current object.

CLASS VARIABLE
-> Shared by all objects.

INSTANCE VARIABLE
-> Belongs to a particular object.

INHERITANCE
-> Child class gets features from parent class.

METHOD OVERRIDING
-> Child class provides its own version of a method.

ENCAPSULATION
-> Restricting/directing access to data.

@classmethod
-> Method that works with the class.

@staticmethod
-> Method that doesn't need self or cls.
"""