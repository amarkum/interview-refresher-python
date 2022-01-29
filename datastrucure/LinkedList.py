# Linked List class
class LinkedList:

    # Function to initialize the LinkedList object
    def __init__(self):
        self.head = None
        self.size = 0

    # This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Returns if the LinkedList is empty or not
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
