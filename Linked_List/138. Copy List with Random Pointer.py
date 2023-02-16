
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}  # map original node to copy node

        # create a copy of each node and store it in the map
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        # set next and random pointers for the copy nodes
        curr = head
        while curr:
            if curr.next:
                mp[curr].next = mp[curr.next]
            if curr.random:
                mp[curr].random = mp[curr.random]
            curr = curr.next

        # return the copy of the head node
        return mp[head]


# create the input linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4

head.random = node3
node2.random = head
node4.random = node2

# create an instance of the Solution class
sol = Solution()

# call the copyRandomList function
copy_head = sol.copyRandomList(head)

# print the original and copy linked lists
print("Original list:")
curr = head
while curr:
    print(f"val: {curr.val}, random: {curr.random.val if curr.random else None}")
    curr = curr.next

print("Copy list:")
curr = copy_head
while curr:
    print(f"val: {curr.val}, random: {curr.random.val if curr.random else None}")
    curr = curr.next
