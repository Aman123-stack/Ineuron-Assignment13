q1>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_linked_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Initialize pointers
    ptr1 = list1
    ptr2 = list2

    # Create a dummy node to track the head of the merged list
    merged_head = Node()

    # Pointer to the last node of the merged list
    merged_ptr = merged_head

    while ptr1 is not None and ptr2 is not None:
        # Compare the values of the current nodes
        if ptr1.data >= ptr2.data:
            merged_ptr.next = Node(ptr1.data)
            ptr1 = ptr1.next
        else:
            merged_ptr.next = Node(ptr2.data)
            ptr2 = ptr2.next
        merged_ptr = merged_ptr.next

    # Add any remaining nodes from list1
    while ptr1 is not None:
        merged_ptr.next = Node(ptr1.data)
        ptr1 = ptr1.next
        merged_ptr = merged_ptr.next

    # Add any remaining nodes from list2
    while ptr2 is not None:
        merged_ptr.next = Node(ptr2.data)
        ptr2 = ptr2.next
        merged_ptr = merged_ptr.next

    # Return the head of the merged linked list (excluding the dummy node)
    return merged_head.next
q2>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if head is None:
        return head

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
q3>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverseKNodes(head, k):
    if head is None or k == 1:
        return head

    dummy = Node(0)
    dummy.next = head

    prev = dummy
    curr = head
    counter = 0

    while curr is not None:
        counter += 1
        if counter % k == 0:
            prev = reverseGroup(prev, curr.next)
            curr = prev.next
        else:
            curr = curr.next

    return dummy.next

def reverseGroup(prev, nxt):
    last = prev.next
    curr = last.next

    while curr is not nxt:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = last.next

    return last
q4>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverseAlternateKNodes(head, k):
    if head is None or k <= 1:
        return head

    curr = head
    prev = None
    next = None
    count = 0

    # Reverse k nodes
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # Skip k nodes
    while curr is not None and count < 2 * k:
        curr = curr.next
        count += 1

    # Recursively call for the remaining list
    if curr is not None:
        head.next = reverseAlternateKNodes(curr, k)

    return prev
q5>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if head is None:
        return head

    # Find the last occurrence of the key and its previous node
    last_occurrence = None
    prev = None
    current = head

    while current is not None:
        if current.data == key:
            last_occurrence = current
        current = current.next

    if last_occurrence is None:
        # Key not found, return the original linked list
        return head

    # If the last occurrence is the head node, update the head
    if last_occurrence == head:
        head = head.next
    else:
        # Update the pointers of the previous node
        current = head
        while current.next != last_occurrence:
            current = current.next
        current.next = last_occurrence.next

    return head
q6>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def mergeSortedLists(head1, head2):
    dummy = Node()
    current = dummy

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Attach the remaining nodes from the first list, if any
    if head1 is not None:
        current.next = head1

    # Attach the remaining nodes from the second list, if any
    if head2 is not None:
        current.next = head2

    return dummy.next
q7>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def reverseDoublyLinkedList(head):
    if head is None or head.next is None:
        return head

    current = head
    temp = None

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    # Update the head of the reversed doubly linked list
    if temp is not None:
        head = temp.prev

    return head
q8>class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def deleteNodeAtPosition(head, position):
    if head is None:
        return head

    # If the position is 0, delete the head node
    if position == 0:
        if head.next is not None:
            head.next.prev = None
        head = head.next
        return head

    current = head
    count = 0

    # Traverse to the node at the given position
    while current is not None and count < position:
        current = current.next
        count += 1

    # If the position is beyond the length of the list, return the original list
    if current is None:
        return head

    # Update the pointers of the adjacent nodes to skip the node to be deleted
    current.prev.next = current.next

    # If the node to be deleted is not the last node, update the previous and next pointers
    if current.next is not None:
        current.next.prev = current.prev

    return head
