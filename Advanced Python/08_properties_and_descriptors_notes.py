# ============================================================
# INTERMEDIATE PYTHON — PROPERTIES & DESCRIPTORS BASICS
# Standalone notes + runnable quick revision reference
# ============================================================
# A property lets an attribute access (object.value) run method logic.
# This is useful for validation, computed values, and controlled updates.
# Descriptors are the lower-level protocol behind properties.


# ============================================================
# 1. Why use a property?
# ============================================================
# A plain public attribute can be assigned any value with no validation.
# Properties let us keep natural attribute syntax while enforcing rules.


class Temperature:
    def __init__(self, celsius: float):
        self._celsius = 0.0  # _name means "internal use" by convention.
        self.celsius = celsius  # Uses the setter below for validation.

    @property
    def celsius(self) -> float:
        """Getter: runs when code reads temperature.celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Setter: runs when code assigns temperature.celsius = value."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value


temperature = Temperature(25)
print("1. @property getter and setter")
print("Celsius:", temperature.celsius)
temperature.celsius = 30
print("Updated Celsius:", temperature.celsius)

try:
    temperature.celsius = -300
except ValueError as error:
    print("Rejected invalid value:", error)


# ============================================================
# 2. Computed read-only property
# ============================================================
# A property without a setter is read-only. Its value is calculated whenever
# it is accessed, so there is no separate stored fahrenheit attribute.


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2


circle = Circle(3)
print("\n2. Read-only computed property")
print(f"Area: {circle.area:.2f}")

# circle.area = 100  # AttributeError: property has no setter.


# ============================================================
# 3. Property deleter (less common)
# ============================================================


class CachedReport:
    def __init__(self, content: str):
        self._content = content

    @property
    def content(self) -> str:
        return self._content

    @content.deleter
    def content(self) -> None:
        print("Clearing cached report content")
        del self._content


report = CachedReport("Monthly summary")
print("\n3. Property deleter")
print(report.content)
del report.content


# ============================================================
# 4. Descriptor concept
# ============================================================
# A descriptor is an object stored as a CLASS attribute that defines one or
# more of __get__, __set__, and __delete__. Python calls these methods when
# an attribute is read, written, or deleted. `property` is a descriptor.


class PositiveNumber:
    """Reusable descriptor that accepts only positive numbers."""

    def __set_name__(self, owner, name) -> None:
        # Runs when Python creates the owner class. Store a private name.
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        # Accessed through class: Product.price -> return descriptor itself.
        if instance is None:
            return self
        # Accessed through instance: product.price -> return stored value.
        return getattr(instance, self.private_name)

    def __set__(self, instance, value: float) -> None:
        if value <= 0:
            raise ValueError(f"{self.private_name[1:]} must be positive")
        setattr(instance, self.private_name, value)


class Product:
    # One descriptor can validate this attribute for every Product instance.
    price = PositiveNumber()
    weight = PositiveNumber()

    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price    # Calls PositiveNumber.__set__.
        self.weight = weight  # Calls PositiveNumber.__set__.


product = Product("Laptop", 75_000, 1.5)
print("\n4. Descriptor")
print(f"{product.name}: price={product.price}, weight={product.weight}")

try:
    product.weight = 0
except ValueError as error:
    print("Descriptor validation:", error)


# ============================================================
# QUICK REVIEW
# ============================================================
# @property              -> getter; runs when obj.attribute is read
# @name.setter           -> setter; runs when obj.attribute = value
# @name.deleter          -> runs when del obj.attribute is used
# _attribute             -> internal-use convention, not true privacy
# computed property      -> calculated on read; often has no setter
# descriptor             -> class attribute defining __get__/__set__/__delete__
# property               -> built-in descriptor for getter/setter/deleter logic
# __set_name__           -> descriptor hook receiving its attribute name
