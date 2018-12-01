class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(data)
            temp = temp.next
            temp.data = data
            temp.next = None

    def display(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print temp.data
                temp = temp.next
        else:
            print "Q is empty"

    def reverse(self):
        prev = self.head
        curr = prev.next
        prev.next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


l1 = LinkedList()
l2 = LinkedList()
data = [1, 9, 0]

for i in data:
    l1.insert(i)
data = [9]
for i in data:
    l2.insert(i)
l1.reverse()
l2.reverse()


def add_linked_lists(l1, l2):
    t1 = l1.head
    t2 = l2.head
    l3 = LinkedList()
    borrow = 0

    while t1 is not None or t2 is not None:
        curr_sum = borrow
        if t1 is not None:
            curr_sum += t1.data
        if t2 is not None:
            curr_sum += t2.data
        if curr_sum < 10:
            l3.insert(curr_sum)
            borrow = 0
        else:
            borrow = 1
            l3.insert(curr_sum-10)
        if t1 is not None:
            t1 = t1.next
        if t2 is not None:
            t2 = t2.next
    if borrow == 1:
        l3.insert(borrow)
    return l3


result = add_linked_lists(l1, l2)

result.reverse()
result.display()