# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,root,res):
        if not root:
            return None
        self.func(root.left,res)
        res.append(root.val)
        self.func(root.right,res)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        self.func(root,res)
        return res
