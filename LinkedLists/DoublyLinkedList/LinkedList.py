#===================================================
# Doubly Linkedlist
#===================================================

class node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class linked_list():

    def __init__(self):
        self.head = node()

    def display(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
