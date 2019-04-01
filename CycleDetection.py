# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
#
# Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named head
#    that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a
#    cycle in the list. If there is a cycle, return true; otherwise, return false.
#
# Note: If the list is empty, head will be null.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = head
    fast = head
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

        if (slow == fast):
            return True

    return False


# The theory behind it: you must traverse the list using 2 pointers that we'll
# to as slow and fast. Our slow pointer moves forward 1 node at a time, and our fast
# pointer moves forward 2 nodes at a time. If at any point in time the 2 pointers refer
# to the same object, then there is a loop. Other wise the list does not contain a loop.
# IF THERE IS A LOOP OUR FAST POINTER WILL AT SOME TIME POINT TO THE SAME NODE AS OUR SLOW POINTER.
