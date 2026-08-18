# ============================================================
# INTERMEDIATE PYTHON — MAGIC / DUNDER METHODS
# Runnable notes + quick revision reference
# ============================================================
# Dunder means "double underscore". These special methods let Python
# know how your objects should behave with built-in syntax/functions.


# ============================================================
# 1. __init__, __str__, and __repr__
# ============================================================


class Book:
    def __init__(self, title: str, pages: int):
        # __init__ runs when we create an object: Book(...)
        self.title = title
        self.pages = pages

    def __str__(self) -> str:
        # Used by print(object) and str(object): user-friendly text.
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self) -> str:
        # Used in lists/debugging: unambiguous developer-friendly text.
        return f"Book(title={self.title!r}, pages={self.pages})"


book = Book("Python Basics", 300)
print("1. __init__, __str__, __repr__")
print(book)          # Calls book.__str__()
print(repr(book))    # Calls book.__repr__()
print([book])        # A list uses __repr__ for its items.


# ============================================================
# 2. Comparison methods: __eq__, __lt__, __gt__
# ============================================================


class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        # Return NotImplemented for an unsupported comparison type.
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __lt__(self, other: object) -> bool:
        # Enables < and lets sorted() order Product objects by price.
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other: object) -> bool:
        # Enables >.
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __repr__(self) -> str:
        return f"Product({self.name!r}, {self.price})"


mouse = Product("Mouse", 800)
same_mouse = Product("Mouse", 800)
keyboard = Product("Keyboard", 2_500)

print("\n2. Comparison methods")
print("Equal values?", mouse == same_mouse)       # Calls __eq__
print("Mouse cheaper?", mouse < keyboard)         # Calls __lt__
print("Keyboard costlier?", keyboard > mouse)     # Calls __gt__
print("Sorted:", sorted([keyboard, mouse]))


# ============================================================
# 3. __len__ and __contains__
# ============================================================


class Playlist:
    def __init__(self, songs: list[str]):
        self.songs = songs

    def __len__(self) -> int:
        # Enables len(playlist).
        return len(self.songs)

    def __contains__(self, song: object) -> bool:
        # Enables: "song name" in playlist
        return song in self.songs


playlist = Playlist(["Sky", "Focus", "Code"])
print("\n3. __len__ and __contains__")
print("Number of songs:", len(playlist))
print("Is 'Focus' included?", "Focus" in playlist)


# ============================================================
# 4. __getitem__ and __setitem__
# ============================================================


class Scores:
    def __init__(self):
        self._scores = {"Alice": 90, "Bob": 85}

    def __getitem__(self, name: str) -> int:
        # Enables scores["Alice"].
        return self._scores[name]

    def __setitem__(self, name: str, score: int) -> None:
        # Enables scores["Charlie"] = 95.
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self._scores[name] = score


scores = Scores()
scores["Charlie"] = 95
print("\n4. __getitem__ and __setitem__")
print("Alice:", scores["Alice"])
print("Charlie:", scores["Charlie"])


# ============================================================
# 5. __iter__ and __next__: making an object an iterator
# ============================================================


class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        # iter(countdown) calls this. An iterator returns itself.
        return self

    def __next__(self) -> int:
        # next(countdown) calls this.
        if self.current <= 0:
            # Tells a for-loop that there are no more values.
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("\n5. __iter__ and __next__")
for number in Countdown(3):
    print(number)


# ============================================================
# 6. __call__: making an object callable like a function
# ============================================================


class Greeter:
    def __init__(self, greeting: str):
        self.greeting = greeting

    def __call__(self, name: str) -> str:
        # Enables greeter("Asha").
        return f"{self.greeting}, {name}!"


say_hello = Greeter("Hello")
print("\n6. __call__")
print(say_hello("Asha"))


# ============================================================
# QUICK REVIEW: syntax -> special method
# ============================================================
# Book(...)             -> __init__
# print(book)           -> __str__
# repr(book), [book]    -> __repr__
# a == b, a < b, a > b  -> __eq__, __lt__, __gt__
# len(obj)              -> __len__
# item in obj           -> __contains__
# obj[key], obj[key]=x  -> __getitem__, __setitem__
# iter(obj), next(obj)  -> __iter__, __next__
# obj(...)              -> __call__
