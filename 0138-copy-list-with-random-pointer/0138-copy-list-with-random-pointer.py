"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapcopy = {None:None}

        cur = head
        while cur:
            mapcopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = mapcopy[cur]
            copy.next = mapcopy[cur.next]
            copy.random = mapcopy[cur.random]
            cur = cur.next

        return mapcopy[head]
        