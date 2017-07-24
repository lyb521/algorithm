# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/24
# @Time: 18:30
# @url: http://www.lintcode.com/zh-cn/problem/min-stack/
# @Description:实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。

class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = []

    def push(self, number):
        # write yout code here
        self.stack.insert(0, number)

    def pop(self):
        # pop and return the top item in stack
        return self.stack.pop(0)

    def min(self):
        # return the minimum number in stack
        if self.stack:
            min_val = min(self.stack)
            try:
                int(min_val)
                return min_val
            except ValueError:
                return False
        return False


if __name__ == '__main__':
    s = MinStack()
    print (s.push(1))
    print (s.pop())
    print (s.push(2))
    print (s.push(3))
    print (s.min())
    print (s.push(1))
    print (s.min())
