# ============================================================
# INTERMEDIATE PYTHON — ADVANCED OOP
# Runnable notes + quick revision reference
# ============================================================

from abc import ABC, abstractmethod


# ============================================================
# 1. Class variables vs instance variables
# ============================================================


class Student:
    # Class variable: shared by every Student object.
    school_name = "Python Academy"

    def __init__(self, name: str, score: int):
        # Instance variables: each object has its own values.
        self.name = name
        self.score = score


alice = Student("Alice", 92)
bob = Student("Bob", 85)

print("1. Class and instance variables")
print(Student.school_name)  # Access a class variable through the class.
print(alice.name, alice.score)
print(bob.name, bob.score)

# Changing the class variable affects lookups for all instances.
Student.school_name = "AI Academy"
print(alice.school_name, bob.school_name)


# ============================================================
# 2. Inheritance and super()
# ============================================================


class Employee:
    """Parent/base class: common behaviour for all employees."""

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def introduce(self) -> str:
        return f"I am {self.name}."


class Developer(Employee):
    """Child/subclass: inherits Employee and adds a new attribute."""

    def __init__(self, name: str, salary: int, language: str):
        # super() calls the parent class method.
        super().__init__(name, salary)
        self.language = language

    def introduce(self) -> str:
        # Reuse the parent implementation, then extend it.
        return f"{super().introduce()} I write {self.language}."


dev = Developer("Riya", 90_000, "Python")
print("\n2. Inheritance and super()")
print(dev.introduce())
print(dev.salary)  # Inherited instance variable.


# ============================================================
# 3. Polymorphism
# ============================================================
# Same method name, different behaviour depending on the object.


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        """Every concrete Animal must provide its own sound."""


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


def make_animal_speak(animal: Animal) -> None:
    # This function works with any Animal subclass.
    print(animal.speak())


print("\n3. Polymorphism")
for animal in [Dog(), Cat()]:
    make_animal_speak(animal)


# ============================================================
# 4. Abstraction (ABC + @abstractmethod)
# ============================================================
# An abstract class defines a required interface. It is a blueprint,
# so you cannot create a PaymentProcessor directly.


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CardPayment(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Paid Rs. {amount:.2f} by card"


print("\n4. Abstraction")
processor = CardPayment()
print(processor.pay(499.0))


# ============================================================
# 5. Encapsulation and properties
# ============================================================
# _balance means "internal use" by convention. A property controls
# reading/writing while keeping the nice account.balance syntax.


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner
        self._balance = 0.0
        self.balance = opening_balance  # Uses the setter for validation.

    @property
    def balance(self) -> float:
        """Getter: runs when code reads account.balance."""
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        """Setter: runs when code assigns account.balance = amount."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount


account = BankAccount("Aman", 1_000)
account.deposit(250)
print("\n5. Encapsulation and @property")
print(f"{account.owner}'s balance: Rs. {account.balance:.2f}")


# ============================================================
# 6. @classmethod and @staticmethod
# ============================================================


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        # cls is the class (Temperature), useful for alternate constructors.
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        # No self and no cls: a related utility function.
        return celsius <= 0


temp = Temperature.from_fahrenheit(68)
print("\n6. Class methods and static methods")
print(f"68 F is {temp.celsius:.1f} C")
print("Is -2 C freezing?", Temperature.is_freezing(-2))


# ============================================================
# QUICK REVIEW
# ============================================================
# class variable     -> shared by the class/instances
# instance variable  -> belongs to one object (self.attribute)
# inheritance        -> child reuses parent functionality
# super()            -> access parent implementation
# polymorphism       -> same interface, different object behaviour
# abstraction        -> define required methods with ABC/@abstractmethod
# encapsulation      -> protect/control internal state
# @property          -> attribute-style access with getter/setter logic
# @classmethod       -> method that receives the class (cls)
# @staticmethod      -> related helper; receives neither self nor cls
