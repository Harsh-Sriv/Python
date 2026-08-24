# ============================================================
#                  PYTHON CIRCULAR LINKED LIST
# ============================================================

# A Circular Linked List is a linked list where the last node
# points back to the first node instead of pointing to None.
#
# Structure:
#
#        ┌─────────────────────────┐
#        ↓                         │
#     [10] -> [20] -> [30] --------┘
#
# Last node:
#     30.next = 10
#
# Therefore, there is NO None at the end.


# ============================================================
# 1. Creating a Node
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# Create nodes

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes

node1.next = node2
node2.next = node3
node3.next = node1

# Circular structure:
#
# 10 -> 20 -> 30
# ↑            ↓
# └────────────┘


# ============================================================
# 2. Creating a Circular Linked List
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None


# Empty circular linked list:
#
# head -> None


# ============================================================
# 3. Insert at Beginning
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def insert_beginning(self, data):

        new_node = Node(data)

        # Empty list

        if self.head is None:

            self.head = new_node
            new_node.next = self.head
            return

        # Find last node

        current = self.head

        while current.next != self.head:
            current = current.next

        # Connect new node

        new_node.next = self.head
        current.next = new_node

        # Update head

        self.head = new_node


# Example:
#
# Before:
# 10 -> 20 -> 30 -> back to 10
#
# insert_beginning(5)
#
# After:
# 5 -> 10 -> 20 -> 30 -> back to 5


# Time Complexity:
# O(n)


# ============================================================
# 4. Insert at End
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def insert_end(self, data):

        new_node = Node(data)

        # Empty list

        if self.head is None:

            self.head = new_node
            new_node.next = self.head
            return

        # Find last node

        current = self.head

        while current.next != self.head:
            current = current.next

        # Connect new node

        current.next = new_node
        new_node.next = self.head


# Example:
#
# 10 -> 20 -> 30 -> back to 10


# Time Complexity:
# O(n)


# ============================================================
# 5. Traversing a Circular Linked List
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def display(self):

        if self.head is None:
            print("Empty List")
            return

        current = self.head

        while True:

            print(current.data, end=" -> ")

            current = current.next

            # Stop when we reach head again

            if current == self.head:
                break

        print("(back to head)")


# Example output:
#
# 10 -> 20 -> 30 -> (back to head)


# IMPORTANT:
#
# We cannot use:
#
# while current is not None
#
# because current NEVER becomes None.


# Time Complexity:
# O(n)


# ============================================================
# 6. Searching
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def search(self, value):

        if self.head is None:
            return False

        current = self.head

        while True:

            if current.data == value:
                return True

            current = current.next

            if current == self.head:
                break

        return False


# Example:
#
# 10 -> 20 -> 30 -> back to 10
#
# search(20) -> True
# search(50) -> False


# Time Complexity:
# O(n)


# ============================================================
# 7. Delete from Beginning
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def delete_beginning(self):

        # Empty list

        if self.head is None:
            return

        # Only one node

        if self.head.next == self.head:

            self.head = None
            return

        # Find last node

        current = self.head

        while current.next != self.head:
            current = current.next

        # Move head

        self.head = self.head.next

        # Last node points to new head

        current.next = self.head


# Example:
#
# Before:
# 10 -> 20 -> 30 -> back to 10
#
# After:
# 20 -> 30 -> back to 20


# Time Complexity:
# O(n)


# ============================================================
# 8. Delete from End
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def delete_end(self):

        # Empty list

        if self.head is None:
            return

        # Only one node

        if self.head.next == self.head:

            self.head = None
            return

        current = self.head

        # Find second-last node

        while current.next.next != self.head:
            current = current.next

        # Remove last node

        current.next = self.head


# Example:
#
# Before:
# 10 -> 20 -> 30 -> back to 10
#
# After:
# 10 -> 20 -> back to 10


# Time Complexity:
# O(n)


# ============================================================
# 9. Delete by Value
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def delete_value(self, value):

        if self.head is None:
            return

        # Value is at head

        if self.head.data == value:

            self.delete_beginning()
            return

        current = self.head

        while current.next != self.head:

            if current.next.data == value:

                # Skip the target node

                current.next = current.next.next
                return

            current = current.next


# Example:
#
# Before:
# 10 -> 20 -> 30 -> back to 10
#
# delete_value(20)
#
# After:
# 10 -> 30 -> back to 10


# Time Complexity:
# O(n)


# ============================================================
# 10. Count Nodes
# ============================================================

class CircularLinkedList:

    def __init__(self):

        self.head = None

    def length(self):

        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:

            count += 1
            current = current.next

            if current == self.head:
                break

        return count


# Example:
#
# 10 -> 20 -> 30 -> back to 10
#
# length() -> 3


# Time Complexity:
# O(n)


# ============================================================
# 11. Complete Circular Linked List
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):

        self.head = None

    def insert_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node

        self.head = new_node

    def insert_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete_beginning(self):

        if self.head is None:
            return

        if self.head.next == self.head:

            self.head = None
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        self.head = self.head.next

        current.next = self.head

    def delete_end(self):

        if self.head is None:
            return

        if self.head.next == self.head:

            self.head = None
            return

        current = self.head

        while current.next.next != self.head:
            current = current.next

        current.next = self.head

    def delete_value(self, value):

        if self.head is None:
            return

        if self.head.data == value:

            self.delete_beginning()
            return

        current = self.head

        while current.next != self.head:

            if current.next.data == value:

                current.next = current.next.next
                return

            current = current.next

    def search(self, value):

        if self.head is None:
            return False

        current = self.head

        while True:

            if current.data == value:
                return True

            current = current.next

            if current == self.head:
                break

        return False

    def length(self):

        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:

            count += 1
            current = current.next

            if current == self.head:
                break

        return count

    def display(self):

        if self.head is None:

            print("Empty List")
            return

        current = self.head

        while True:

            print(current.data, end=" -> ")

            current = current.next

            if current == self.head:
                break

        print("(back to head)")


# ============================================================
# 12. Example Usage
# ============================================================

cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()

# 10 -> 20 -> 30 -> (back to head)


cll.insert_beginning(5)

cll.display()

# 5 -> 10 -> 20 -> 30 -> (back to head)


print(cll.search(20))

# True


print(cll.length())

# 4


cll.delete_value(20)

cll.display()

# 5 -> 10 -> 30 -> (back to head)


# ============================================================
#                  QUICK REFERENCE
# ============================================================

"""
Circular Linked List:

Last node points back to head.

Normal Linked List:

10 -> 20 -> 30 -> None

Circular:

10 -> 20 -> 30
↑            ↓
└────────────┘


Important Difference:

Normal traversal:

while current is not None:
    current = current.next


Circular traversal:

while True:

    # process node

    current = current.next

    if current == head:
        break


Common Operations:

insert beginning     -> O(n)

insert end           -> O(n)

delete beginning     -> O(n)

delete end           -> O(n)

delete by value      -> O(n)

search               -> O(n)

traversal            -> O(n)

length               -> O(n)


IMPORTANT:

A circular linked list does NOT end with None.

You must detect when you reach the head again.


Advantages:

- Can continuously traverse the list
- Useful for cyclic processes
- No NULL/None at the end
- Useful for round-robin scheduling


Disadvantages:

- Traversal logic is slightly more complicated
- Easy to create infinite loops
- Need to explicitly check when we return to head
"""