import Queue

if __name__ == '__main__':

    #create instance of Queue class
    q = Queue.Queue()
    print(q.isEmpty())
    print('\n')
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print('head: ',q.peek())
    print(q.isEmpty())
    print('\n')
    print('size: ',q.size())
    q.printQueue()
    print('\n')
    q.dequeue()
    print('size: ',q.size())
    q.printQueue()
    print('\n')
    q.dequeue()
    print('size: ',q.size())
    q.printQueue()
    print('head: ',q.peek())
