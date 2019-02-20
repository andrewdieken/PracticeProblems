# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
#
# Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named head that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.
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
