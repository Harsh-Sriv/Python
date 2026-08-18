# ============================================================
#              MULTI-DIMENSIONAL LISTS IN PYTHON
# ============================================================

# A 2D list is a list containing other lists.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


# ============================================================
# 1. Accessing elements
# ============================================================

print(matrix[0])       # First row
print(matrix[0][0])    # First row, first column
print(matrix[1][2])    # Second row, third column

# matrix[row][column]


# ============================================================
# 2. Changing an element
# ============================================================

matrix[1][1] = 50

print(matrix)


# ============================================================
# 3. Traversing a 2D list
# ============================================================

for row in matrix:
    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 4. Using indexes
# ============================================================

rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")

    print()


# ============================================================
# 5. Creating a 2D list
# ============================================================

rows = 3
columns = 4

matrix = [[0 for j in range(columns)] for i in range(rows)]

print(matrix)

# Output:
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]]


# ============================================================
# 6. Taking a matrix as input
# ============================================================

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

print(matrix)


# ============================================================
# 7. Practical example - Sum of all elements
# ============================================================

total = 0

for row in matrix:
    for value in row:
        total += value

print("Sum:", total)


# ============================================================
# 8. Finding an element
# ============================================================

target = 5

for i in range(len(matrix)):
    for j in range(len(matrix[i])):

        if matrix[i][j] == target:
            print("Found at:", i, j)


# ============================================================
# 9. 3D List
# ============================================================

# A list can contain lists which contain lists.

cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(cube[0][1][0])

# cube[layer][row][column]


# ============================================================
# IMPORTANT
# ============================================================

"""
2D list:

matrix[row][column]

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[0][1] -> 2
matrix[1][2] -> 6


3D list:

cube[layer][row][column]


Common DSA uses:

- Matrix
- 2D arrays
- Grids
- Graph representations
- Dynamic programming tables
- Game boards
"""