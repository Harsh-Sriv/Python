# ============================================================
#                  OBJECT FUNCTIONS IN PYTHON
# ============================================================

# Python provides several built-in functions that work
# with objects.


# ============================================================
# 1. type() - Find the type of an object
# ============================================================

x = 10
name = "Python"

print(type(x))        # int
print(type(name))     # str


# ============================================================
# 2. id() - Get object's identity
# ============================================================

x = 10

print(id(x))

# Every object has a unique identity during its lifetime.


# ============================================================
# 3. isinstance() - Check object's type
# ============================================================

x = 10

print(isinstance(x, int))       # True
print(isinstance(x, str))       # False


# ============================================================
# 4. len() - Get size/length
# ============================================================

numbers = [10, 20, 30]

print(len(numbers))             # 3

name = "Python"

print(len(name))                # 6


# ============================================================
# 5. str() - Convert object to string
# ============================================================

number = 100

text = str(number)

print(text)
print(type(text))


# ============================================================
# 6. dir() - Show available attributes and methods
# ============================================================

numbers = [1, 2, 3]

print(dir(numbers))

# Useful for discovering what functions/methods
# an object provides.


# ============================================================
# 7. getattr() - Get an object's attribute
# ============================================================

class Student:

    def __init__(self):
        self.name = "Harsh"


student = Student()

print(getattr(student, "name"))


# ============================================================
# 8. setattr() - Set an object's attribute
# ============================================================

setattr(student, "age", 22)

print(student.age)


# ============================================================
# 9. hasattr() - Check if an attribute exists
# ============================================================

print(hasattr(student, "name"))    # True
print(hasattr(student, "marks"))   # False


# ============================================================
# 10. delattr() - Delete an attribute
# ============================================================

delattr(student, "age")

print(hasattr(student, "age"))     # False


# ============================================================
# 11. vars() - Show object's attributes
# ============================================================

student = Student()

student.age = 22
student.marks = 90

print(vars(student))

# Output:
# {'name': 'Harsh', 'age': 22, 'marks': 90}


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
type(obj)
-> Get object's type

id(obj)
-> Get object's identity

isinstance(obj, type)
-> Check object's type

len(obj)
-> Get length

str(obj)
-> Convert object to string

dir(obj)
-> Show available attributes/methods

getattr(obj, "attribute")
-> Get an attribute

setattr(obj, "attribute", value)
-> Set an attribute

hasattr(obj, "attribute")
-> Check if attribute exists

delattr(obj, "attribute")
-> Delete an attribute

vars(obj)
-> Get object's __dict__
"""