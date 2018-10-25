#===========================================
# The Stack class is created using a python list
# The front of the Stack is equal to the last element in the Stack
# The back of the Stack is equal to the first element in the Stack
#===========================================
class Stack:

    #===========================================
    # when class is called, an empty list 'items' get initiated
    #===========================================
    def __init__(self):
        self.items = []

    #===========================================
    # returns 'True' if list 'items' is empty & 'False' otherwise
    #===========================================
    def isEmpty(self):
        return self.items == []

    #===========================================
    # adds new element 'item' to the end of the list 'items' using the .append function
    #===========================================
    def push(self, item):
        self.items.append(item)

    #===========================================
    # removes the last elemet in the list 'items' using the .pop function
    #===========================================
    def pop(self):
        self.items.pop()

    #===========================================
    # returns the number of elemets in the list 'items'
    #===========================================
    def size(self):
        return len(self.items)

    #===========================================
    # prints all items in the list 'items' starting from the last position
    #===========================================
    def printStack(self):
        print('printStack() func called')
        for item in reversed(self.items):
            print(item)

if __name__ == '__main__':

  s=Stack()

  print(s.isEmpty())
  s.push(6)
  s.push(5)
  s.push(4)
  s.push(3)
  s.push(2)
  s.push(1)
  print(s.isEmpty())
  print(s.size())
  s.printStack()
