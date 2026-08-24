# ============================================================
#                  PYTHON DOUBLY LINKED LIST
# ============================================================

# A Doubly Linked List is a linked list where each Node stores:
#
# 1. Data
# 2. Reference to the previous Node
# 3. Reference to the next Node
#
# Structure:
#
# None <- [10] <-> [20] <-> [30] -> None
#
# Each node can move in BOTH directions.


# ============================================================
# 1. Creating a Node
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.prev = None
        self.next = None


# Create nodes

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

# Structure:
#
# None <- 10 <-> 20 <-> 30 -> None


# ============================================================
# 2. Creating a Doubly Linked List
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None


# head -> first node
# tail -> last node


# ============================================================
# 3. Insert at Beginning
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_beginning(self, data):

        new_node = Node(data)

        # Empty list

        if self.head is None:

            self.head = new_node
            self.tail = new_node
            return

        # Connect new node to current head

        new_node.next = self.head
        self.head.prev = new_node

        # Update head

        self.head = new_node


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# insert_beginning(5)
#
# After:
# 5 <-> 10 <-> 20 <-> 30


# Time Complexity:
# O(1)


# ============================================================
# 4. Insert at End
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_end(self, data):

        new_node = Node(data)

        # Empty list

        if self.head is None:

            self.head = new_node
            self.tail = new_node
            return

        # Connect new node after tail

        new_node.prev = self.tail
        self.tail.next = new_node

        # Update tail

        self.tail = new_node


# Example:
#
# Before:
# 10 <-> 20
#
# insert_end(30)
#
# After:
# 10 <-> 20 <-> 30


# Time Complexity:
# O(1)
#
# Because we maintain a tail pointer.


# ============================================================
# 5. Traverse Forward
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def display_forward(self):

        current = self.head

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.next

        print("None")


# Output:
#
# 10 <-> 20 <-> 30 <-> None


# Time Complexity:
# O(n)


# ============================================================
# 6. Traverse Backward
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def display_backward(self):

        current = self.tail

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.prev

        print("None")


# Output:
#
# 30 <-> 20 <-> 10 <-> None


# Time Complexity:
# O(n)


# ============================================================
# 7. Search
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def search(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                return True

            current = current.next

        return False


# Example:
#
# 10 <-> 20 <-> 30
#
# search(20) -> True
# search(50) -> False


# Time Complexity:
# O(n)


# ============================================================
# 8. Delete from Beginning
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def delete_beginning(self):

        # Empty list

        if self.head is None:
            return

        # Only one node

        if self.head == self.tail:

            self.head = None
            self.tail = None
            return

        # Move head forward

        self.head = self.head.next

        # Remove previous reference

        self.head.prev = None


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# After:
# 20 <-> 30


# Time Complexity:
# O(1)


# ============================================================
# 9. Delete from End
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def delete_end(self):

        # Empty list

        if self.tail is None:
            return

        # Only one node

        if self.head == self.tail:

            self.head = None
            self.tail = None
            return

        # Move tail backward

        self.tail = self.tail.prev

        # Remove next reference

        self.tail.next = None


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# After:
# 10 <-> 20


# Time Complexity:
# O(1)


# ============================================================
# 10. Delete a Node by Value
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def delete_value(self, value):

        current = self.head

        while current is not None:

            if current.data == value:

                # Node is head

                if current == self.head:

                    self.delete_beginning()
                    return

                # Node is tail

                if current == self.tail:

                    self.delete_end()
                    return

                # Node is in the middle

                current.prev.next = current.next
                current.next.prev = current.prev

                return

            current = current.next


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# delete_value(20)
#
# After:
# 10 <-> 30


# Time Complexity:
# O(n)


# ============================================================
# 11. Insert at a Specific Position
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_at(self, data, position):

        new_node = Node(data)

        # Position 0

        if position == 0:

            if self.head is None:

                self.head = new_node
                self.tail = new_node

            else:

                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            return

        current = self.head

        # Move to required position

        for _ in range(position):

            if current is None:
                return

            current = current.next

        # Insert at end

        if current is None:

            self.insert_end(data)
            return

        # Connect new node

        new_node.prev = current.prev
        new_node.next = current

        current.prev.next = new_node
        current.prev = new_node


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# insert_at(15, 1)
#
# After:
# 10 <-> 15 <-> 20 <-> 30


# Time Complexity:
# O(n)


# ============================================================
# 12. Reverse a Doubly Linked List
# ============================================================

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def reverse(self):

        current = self.head

        while current is not None:

            # Swap prev and next

            current.prev, current.next = \
                current.next, current.prev

            # Move using the new prev

            current = current.prev

        # Swap head and tail

        self.head, self.tail = self.tail, self.head


# Example:
#
# Before:
# 10 <-> 20 <-> 30
#
# After:
# 30 <-> 20 <-> 10


# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)


# ============================================================
# 13. Complete Doubly Linked List
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node

    def insert_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node

        self.tail = new_node

    def insert_at(self, data, position):

        if position == 0:

            self.insert_beginning(data)
            return

        current = self.head

        for _ in range(position):

            if current is None:
                self.insert_end(data)
                return

            current = current.next

        new_node = Node(data)

        new_node.prev = current.prev
        new_node.next = current

        current.prev.next = new_node
        current.prev = new_node

    def delete_beginning(self):

        if self.head is None:
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):

        if self.tail is None:
            return

        if self.head == self.tail:

            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def delete_value(self, value):

        current = self.head

        while current is not None:

            if current.data == value:

                if current == self.head:

                    self.delete_beginning()

                elif current == self.tail:

                    self.delete_end()

                else:

                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next

    def search(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                return True

            current = current.next

        return False

    def display_forward(self):

        current = self.head

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.next

        print("None")

    def display_backward(self):

        current = self.tail

        while current is not None:

            print(current.data, end=" <-> ")

            current = current.prev

        print("None")

    def reverse(self):

        current = self.head

        while current is not None:

            current.prev, current.next = \
                current.next, current.prev

            current = current.prev

        self.head, self.tail = self.tail, self.head


# ============================================================
#                  QUICK REFERENCE
# ============================================================

"""
Node:
    data + prev + next

Head:
    First node

Tail:
    Last node


Common Operations:

insert at beginning     -> O(1)

insert at end           -> O(1)

insert at position      -> O(n)

delete beginning        -> O(1)

delete end              -> O(1)

delete by value         -> O(n)

search                  -> O(n)

forward traversal       -> O(n)

backward traversal      -> O(n)

reverse                 -> O(n)


Main Difference from Singly Linked List:

Singly:
    Node -> next

Doubly:
    Node -> prev + next


Advantages:
    - Can traverse in both directions
    - Easier deletion of a known node
    - Fast insertion/deletion at both ends

Disadvantages:
    - Uses extra memory for prev
    - More references must be maintained
"""