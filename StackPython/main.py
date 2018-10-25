import Stack

if __name__ == '__main__':
    s=Stack.Stack()
    print(s.isEmpty())
    s.push(6)
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.isEmpty())
    print('stack size: ',s.size())
    s.printStack()
