# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/14
# @Time: 17:42
# @url: http://www.lintcode.com/zh-cn/problem/identical-binary-tree/
# @Description: 检查两棵二叉树是否等价。等价的意思是说，首先两棵二叉树必须拥有相同的结构，并且每个对应位置上的节点上的数都相等。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # write your code here
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print (s.isIdentical({1, 2, 2, 4}, {1, 2, 2, 4}))
