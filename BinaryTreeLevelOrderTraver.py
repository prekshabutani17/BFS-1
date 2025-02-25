"""
Time Complexity : O(n)
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        if not root:
            return self.result
        self.dfs(root, 0)
        return self.result
    def dfs(self, root, level):
        # Base case
        if not root:
            return
        # Logic
        if level == len(self.result):
            self.result.append([])
        self.result[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)