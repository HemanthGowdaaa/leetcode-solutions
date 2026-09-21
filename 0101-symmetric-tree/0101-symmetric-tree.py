# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def dfs(left,right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            return (left.val == right.val and dfs(left.right, right.left) and dfs(left.left,right.right))
        return dfs(root.left,root.right)




        # def dfsl(node):
        #     if not node:
        #         return None
        #     dfsl(node.left)
        #     val = node.val
        #     dfsl(node.right)
        #     return val
        # def dfsr(node):
        #     if not node:
        #         return None
        #     dfsr(node.right)
        #     val = node.val
        #     dfsr(node.left)
        #     return val
        # if dfsl(root.left) != dfsr(root.right):
        #     return False
        # else:
        #     return True
        