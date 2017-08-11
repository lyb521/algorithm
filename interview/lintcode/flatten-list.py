# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/10
# @Time: 18:29
# @url: http://www.lintcode.com/zh-cn/problem/flatten-list/
# @Description:给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表

class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]
        result = []
        while len(nestedList) != 0:
            tmp = nestedList.pop(0)
            if isinstance(tmp, int):
                result.append(tmp)
            else:
                #反转list后遍历
                for i in tmp[::-1]:
                    nestedList.insert(0, i)
        return result


if __name__ == '__main__':
    s = Solution()
    print (s.flatten([[1,1],2,[1,1]]))