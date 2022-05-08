
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
2265. Count Nodes Equal to Average of Subtree
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
Binary Tree
"""

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, 0, 0

            sum1, cnt1, res1 = helper(node.left)
            sum2, cnt2, res2 = helper(node.right)

            total_cnt = cnt1+cnt2+1
            total_sum = sum1+sum2+node.val
            total_res = res1+res2

            if node.val == int(total_sum/total_cnt):
                total_res += 1

            return total_sum, total_cnt, total_res

        _, _, res = helper(root)
        return res
