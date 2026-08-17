# ============================================
# INTERMEDIATE PYTHON - RANDOM NUMBERS
# ============================================

import random


# ============================================
# 1. Random integer
# ============================================

number = random.randint(1, 10)

print("Random integer:", number)


# randint includes BOTH endpoints.

# randint(1, 10)
# can produce:
# 1, 2, 3, ..., 10


# ============================================
# 2. randrange()
# ============================================

number = random.randrange(1, 10)

print("\nRandom range:", number)

# 10 is NOT included.


# Step

number = random.randrange(0, 20, 2)

print("Random even number:", number)


# ============================================
# 3. Random float
# ============================================

number = random.random()

print("\nRandom float:", number)

# Range:
# 0.0 <= number < 1.0


# ============================================
# 4. Uniform distribution
# ============================================

number = random.uniform(10, 20)

print("\nRandom float from 10 to 20:", number)


# ============================================
# 5. Choice
# ============================================

colors = ["Red", "Green", "Blue", "Yellow"]

selected = random.choice(colors)

print("\nRandom choice:", selected)


# ============================================
# 6. Choices
# ============================================

selected = random.choices(
    colors,
    k=3
)

print("\nMultiple choices:")
print(selected)

# Duplicates are possible.


# ============================================
# 7. Weighted choices
# ============================================

colors = ["Red", "Green", "Blue"]

selected = random.choices(
    colors,
    weights=[70, 20, 10],
    k=10
)

print("\nWeighted choices:")
print(selected)


# ============================================
# 8. Sample
# ============================================

numbers = [1, 2, 3, 4, 5, 6]

selected = random.sample(
    numbers,
    3
)

print("\nSample without replacement:")
print(selected)


# Elements cannot repeat.


# ============================================
# 9. Shuffle
# ============================================

cards = [
    "A",
    "K",
    "Q",
    "J",
    "10"
]

random.shuffle(cards)

print("\nShuffled cards:")
print(cards)


# IMPORTANT:
# shuffle() modifies the original list.


# ============================================
# 10. Seed
# ============================================

random.seed(42)

print("\nSeeded numbers:")

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))


# Reset the seed

random.seed(42)

print("\nSame seed:")

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))


# The sequence will be the same.


# ============================================
# 11. Random boolean
# ============================================

random_boolean = random.choice([True, False])

print("\nRandom boolean:", random_boolean)


# ============================================
# 12. Random password-like string
# ============================================

import string

characters = string.ascii_letters + string.digits

random_string = "".join(
    random.choices(
        characters,
        k=12
    )
)

print("\nRandom string:", random_string)


# IMPORTANT:
# Don't use random.choices() for actual
# security-sensitive passwords or tokens.


# ============================================
# 13. Random matrix
# ============================================

matrix = [
    [
        random.randint(1, 100)
        for _ in range(3)
    ]
    for _ in range(3)
]

print("\nRandom matrix:")

for row in matrix:
    print(row)


# ============================================
# 14. Practical dice example
# ============================================

def roll_dice():

    return random.randint(1, 6)


print("\nDice rolls:")

for _ in range(5):
    print(roll_dice())


# ============================================
# 15. Simulating coin tosses
# ============================================

results = []

for _ in range(10):

    result = random.choice(
        ["Heads", "Tails"]
    )

    results.append(result)

print("\nCoin tosses:")
print(results)


# ============================================
# 16. Simulating probability
# ============================================

heads = 0
tails = 0

for _ in range(10000):

    result = random.choice(
        ["Heads", "Tails"]
    )

    if result == "Heads":
        heads += 1
    else:
        tails += 1


print("\nAfter 10,000 tosses:")

print("Heads:", heads)
print("Tails:", tails)

print(
    "Heads probability:",
    heads / 10000
)


# ============================================
# 17. Secrets - secure randomness
# ============================================

import secrets

secure_number = secrets.randbelow(100)

print("\nSecure random number:", secure_number)

secure_token = secrets.token_urlsafe(16)

print("Secure token:", secure_token)