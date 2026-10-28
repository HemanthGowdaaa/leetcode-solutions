# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        curr = root
        while curr:
            if val < curr.val :
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None
        