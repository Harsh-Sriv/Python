# ============================================================
#             STATIC vs NON-STATIC IN PYTHON
# ============================================================

class Student:

    # --------------------------------------------------------
    # STATIC / CLASS VARIABLE
    # --------------------------------------------------------
    # Shared by all objects of the class.

    school = "ABC School"

    def __init__(self, name, age):

        # ----------------------------------------------------
        # NON-STATIC / INSTANCE VARIABLES
        # ----------------------------------------------------
        # Each object gets its own copy.

        self.name = name
        self.age = age


    # --------------------------------------------------------
    # NON-STATIC / INSTANCE METHOD
    # --------------------------------------------------------
    # Uses self and works with a particular object.

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", self.school)


    # --------------------------------------------------------
    # STATIC METHOD
    # --------------------------------------------------------
    # Does not need self or cls.
    # It belongs to the class but doesn't access
    # instance-specific data.

    @staticmethod
    def greet():
        print("Welcome to the Student class!")


# ============================================================
#                 CREATING OBJECTS
# ============================================================

student1 = Student("Harsh", 22)
student2 = Student("Rahul", 21)


# ============================================================
# NON-STATIC / INSTANCE DATA
# ============================================================

student1.name = "Aman"

print(student1.name)     # Aman
print(student2.name)     # Rahul

# Changing student1's name does NOT affect student2.


# ============================================================
# STATIC / CLASS DATA
# ============================================================

print(student1.school)
print(student2.school)

# Both objects access the same class variable.


# Change the class variable

Student.school = "XYZ School"

print(student1.school)   # XYZ School
print(student2.school)   # XYZ School


# ============================================================
# INSTANCE METHOD
# ============================================================

student1.display()
student2.display()


# ============================================================
# STATIC METHOD
# ============================================================

Student.greet()

# Can also be called through an object:

student1.greet()