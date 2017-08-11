# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/11
# @Time: 16:39
# @url: http://www.lintcode.com/zh-cn/problem/maximum-depth-of-binary-tree/
# @Description: 给定一个二叉树，找出其最大深度。


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        max_left = max_right = 0
        if not root:
            return 0
        if root.left:
            max_left = self.maxDepth(root.left)
        if root.right:
            max_right = self.maxDepth(root.right)
        if max_left > max_right:
            return max_left + 1
        else:
            return max_right + 1


if __name__ == '__main__':
    s = Solution()
    print (s.maxDepth({}))