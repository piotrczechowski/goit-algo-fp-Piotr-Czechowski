class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = SinglyLinkedList()
        right = SinglyLinkedList()

        left.head = self.head
        right.head = next_to_middle

        left.head = left.merge_sort()
        right.head = right.merge_sort()

        sorted_list = self.sorted_merge(left.head, right.head)
        self.head = sorted_list
        return self.head

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

# Function to merge two sorted singly linked lists
def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Example usage for reversing a singly linked list
llist = SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Original list:")
llist.print_list()

llist.reverse()
print("Reversed list:")
llist.print_list()

# Example usage for sorting a singly linked list using merge sort
llist = SinglyLinkedList()
llist.append(4)
llist.append(2)
llist.append(3)
llist.append(1)

print("Original list:")
llist.print_list()

llist.merge_sort()
print("Sorted list:")
llist.print_list()

# Example usage for merging two sorted singly linked lists
llist1 = SinglyLinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)

llist2 = SinglyLinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

print("First sorted list:")
llist1.print_list()

print("Second sorted list:")
llist2.print_list()

merged_list_head = merge_two_sorted_lists(llist1.head, llist2.head)

merged_list = SinglyLinkedList()
merged_list.head = merged_list_head
print("Merged sorted list:")
merged_list.print_list()
