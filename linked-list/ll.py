'''
Linked Lists

- similar to an array

- contains a list of nodes
    - each node has a next pointer


- can remove any ele at O(1) unless you iterate starting from head

- no random access like array (linkedlist[0])

- addition or removal is O(1) if we know the pointer
'''


'''
Structure of a linked list
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)

one.next = two
head = one

print(head.val, head.next.val) # 1, 2

'''
Pointers in linked lists
'''
pointer = head ## still at head
head = head.next
head = None

head = 1
head = head.next.next ## 3

'''
Traversing linked list
'''
# iteraive approach
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head.next
    return ans

# recursive approach
def get_sum(head):
    if not head:
        return 0
    return head.val + get_sum(head.next)


'''
Singly Linked List

- Most common
- can only move forward

'''
# adding a node to a singly linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

## ex

# 1 - 2 - 3
# add_node(2, 6)
# 1 - 2 - 6 - 3

## essentially we set both nodes in the same position then make the previous node's next value be the node to add so it slides in


## deleting node
# as simple as skipping a node
# O(1) if you know the previous position
def delete_node(prev_node):
    prev_node.next = prev_node.next.next


'''
Doubly Linked List

- contains a pointer to the previous node called prev
- can go forwards or backwards

'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next =  node_to_add
    node.prev = node_to_add

def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node


'''
Full linked list with head and tail nodes sentinal nodes

'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head