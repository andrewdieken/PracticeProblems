import LinkedList


if __name__ == '__main__':
    my_list = LinkedList.linked_list()

    my_list.display()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.display()
    print(my_list.get(0))
    my_list.remove(2)
    my_list.display()

    #prepend
    my_list.prepend(9)
    my_list.display()

    #remove head
    my_list.remove_head()
    my_list.display()
