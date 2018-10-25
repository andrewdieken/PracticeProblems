#===========================================
# The Queue class is created using an empty list
# Items are inserted into the first position of the Queue
# Items are removed from the last position of the queue
#===========================================

class Queue:

    #===========================================
    # when class is called an empty list 'items' gets initiated
    #===========================================
    def __init__(self):
        self.items = []
        self.head = -1

    #===========================================
    # returns 'True' when the 'items' list is empty & 'False' otherwise
    #===========================================
    def isEmpty(self):
        return self.items == []

    #===========================================
    # returns the number of elemets in the list 'items'
    #===========================================
    def size(self):
        return len(self.items)

    #===========================================
    # inserts a new item, 'item', into the first position of 'items'
    #===========================================
    def enqueue(self, item):
        self.items.insert(0, item)
        self.head+=1

    #===========================================
    # removes the last item in the list 'items'
    #===========================================
    def dequeue(self):
        self.items.pop()
        self.head-=1

    #===========================================
    # prints every item in the list 'items'
    #===========================================
    def printQueue(self):
        for item in self.items:
            print(item)

    #===========================================
    # prints the last item in the list 'items'
    #===========================================
    def peek(self):
        return self.items[self.head]
