#=================================================
# singly linked list
#=================================================

class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    #=================================================
    # adds a new node to the end of the linkedlist
    #=================================================
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    #=================================================
    # returns the number of nodes in the linkedlist
    #=================================================
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total

    #=================================================
    # prints all of the nodes in the linkedlist
    #=================================================
    def display(self):
        nodes = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            nodes.append(cur.data)
        print(nodes)

    #=================================================
    # returns the contents of a node given an index
    #=================================================
    def get(self, index):
        if index >= self.length():
            print("ERROR: index out of range")
            return
        cur = self.head
        cur_index = 0
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index+=1

    #=================================================
    # deletes a node given an index
    #=================================================
    def remove(self, index):
        if index >= self.length():
            print("ERROR: index out of range")
            return
        cur = self.head
        cur_index = 0
        while True:
            prev = cur
            cur = cur.next
            if cur_index == index:
                prev.next = cur.next
                return(print('deleted:',cur.data))
            cur_index+=1
