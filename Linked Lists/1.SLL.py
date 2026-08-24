# ============================================================
#                  PYTHON SINGLY LINKED LIST
# ============================================================

# A Linked List is a linear data structure where each element
# (called a Node) stores:
#
# 1. Data
# 2. Reference to the next Node
#
# Unlike arrays/lists, linked list elements are NOT stored
# continuously in memory.
#
# Structure:
#
#     [10 | next] -> [20 | next] -> [30 | None]
#
# The first node is called HEAD.
# The last node points to None.


# ============================================================
# 1. Creating a Node
# ============================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create individual nodes

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect the nodes

node1.next = node2
node2.next = node3

# Structure:
#
# 10 -> 20 -> 30 -> None


# ============================================================
# 2. Creating a Linked List
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None


# Create an empty linked list

ll = LinkedList()

# Initially:
#
# head -> None


# ============================================================
# 3. Inserting at the Beginning
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):

        new_node = Node(data)

        # New node points to current head

        new_node.next = self.head

        # Make new node the head

        self.head = new_node


# Example:

ll = LinkedList()

ll.insert_beginning(30)
ll.insert_beginning(20)
ll.insert_beginning(10)

# Result:
#
# 10 -> 20 -> 30 -> None


# Time Complexity:
# O(1)


# ============================================================
# 4. Inserting at the End
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_end(self, data):

        new_node = Node(data)

        # If list is empty

        if self.head is None:
            self.head = new_node
            return

        # Start from head

        current = self.head

        # Move until the last node

        while current.next is not None:
            current = current.next

        # Connect last node to new node

        current.next = new_node


# Example:

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

# Result:
#
# 10 -> 20 -> 30 -> None


# Time Complexity:
# O(n)


# ============================================================
# 5. Traversing the Linked List
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end=" -> ")

            current = current.next

        print("None")


# Example:

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.display()

# Output:
#
# 10 -> 20 -> 30 -> None


# Time Complexity:
# O(n)


# ============================================================
# 6. Searching for an Element
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                return True

            current = current.next

        return False


# Example:

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print(ll.search(20))
print(ll.search(50))

# Output:
#
# True
# False


# Time Complexity:
# O(n)


# ============================================================
# 7. Finding Length
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def length(self):

        count = 0
        current = self.head

        while current is not None:

            count += 1
            current = current.next

        return count


# Example:

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print(ll.length())

# Output:
#
# 3


# Time Complexity:
# O(n)


# ============================================================
# 8. Inserting at a Specific Position
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at(self, data, position):

        new_node = Node(data)

        # Insert at beginning

        if position == 0:

            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        # Move to node before required position

        for _ in range(position - 1):

            if current is None:
                return

            current = current.next

        # Invalid position

        if current is None:
            return

        # Insert new node

        new_node.next = current.next
        current.next = new_node


# Example:
#
# Original:
# 10 -> 20 -> 30
#
# Insert 15 at position 1
#
# Result:
# 10 -> 15 -> 20 -> 30


# Time Complexity:
# O(n)


# ============================================================
# 9. Deleting the First Node
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_beginning(self):

        if self.head is None:
            return

        # Move head to the next node

        self.head = self.head.next


# Example:
#
# Before:
# 10 -> 20 -> 30
#
# After:
# 20 -> 30


# Time Complexity:
# O(1)


# ============================================================
# 10. Deleting the Last Node
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_end(self):

        # Empty list

        if self.head is None:
            return

        # Only one node

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        # Find second-last node

        while current.next.next is not None:
            current = current.next

        # Remove last node

        current.next = None


# Example:
#
# Before:
# 10 -> 20 -> 30
#
# After:
# 10 -> 20


# Time Complexity:
# O(n)


# ============================================================
# 11. Deleting a Node by Value
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def delete_value(self, value):

        # Empty list

        if self.head is None:
            return

        # Value is in head

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        # Find node before target

        while current.next is not None:

            if current.next.data == value:

                current.next = current.next.next
                return

            current = current.next


# Example:
#
# Before:
# 10 -> 20 -> 30
#
# delete_value(20)
#
# After:
# 10 -> 30


# Time Complexity:
# O(n)


# ============================================================
# 12. Reverse a Linked List
# ============================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):

        previous = None
        current = self.head

        while current is not None:

            # Save next node

            next_node = current.next

            # Reverse the link

            current.next = previous

            # Move previous forward

            previous = current

            # Move current forward

            current = next_node

        # Previous becomes the new head

        self.head = previous


# Example:
#
# Before:
# 10 -> 20 -> 30 -> None
#
# After:
# 30 -> 20 -> 10 -> None


# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)


# ============================================================
# 13. Complete Singly Linked List
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def insert_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at(self, data, position):

        new_node = Node(data)

        if position == 0:

            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):

            if current is None:
                return

            current = current.next

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node

    def delete_beginning(self):

        if self.head is not None:
            self.head = self.head.next

    def delete_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    def delete_value(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:

            if current.next.data == value:

                current.next = current.next.next
                return

            current = current.next

    def search(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                return True

            current = current.next

        return False

    def length(self):

        count = 0
        current = self.head

        while current is not None:

            count += 1
            current = current.next

        return count

    def reverse(self):

        previous = None
        current = self.head

        while current is not None:

            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end=" -> ")

            current = current.next

        print("None")


# ============================================================
# 14. Example Usage
# ============================================================

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.display()

# 10 -> 20 -> 30 -> None


ll.insert_beginning(5)

ll.display()

# 5 -> 10 -> 20 -> 30 -> None


ll.insert_at(15, 2)

ll.display()

# 5 -> 10 -> 15 -> 20 -> 30 -> None


print(ll.search(20))

# True


print(ll.length())

# 5


ll.delete_value(15)

ll.display()

# 5 -> 10 -> 20 -> 30 -> None


ll.reverse()

ll.display()

# 30 -> 20 -> 10 -> 5 -> None


# ============================================================
#                  QUICK REFERENCE
# ============================================================

"""
Node:
    data + next

Head:
    Reference to the first node

Last Node:
    next = None


Common Operations:

insert at beginning     -> O(1)

insert at end           -> O(n)

insert at position      -> O(n)

delete beginning        -> O(1)

delete end              -> O(n)

delete by value         -> O(n)

search                  -> O(n)

traversal               -> O(n)

length                  -> O(n)

reverse                 -> O(n)


Important Pattern:

current = self.head

while current is not None:
    # use current.data
    current = current.next


Reverse Pattern:

previous = None
current = self.head

while current is not None:

    next_node = current.next
    current.next = previous

    previous = current
    current = next_node

self.head = previous
"""