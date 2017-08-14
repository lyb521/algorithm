# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/14
# @Time: 15:22
# @url: http://www.lintcode.com/zh-cn/problem/minimum-depth-of-binary-tree/
# @Description: 给定一个二叉树，找出其最小深度。


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            left = sys.maxint
        if right == 0:
            right = sys.maxint
        if left < right :
            return left + 1
        else:
            return right + 1


if __name__ == '__main__':
    s = Solution()
    print (s.minDepth({}))